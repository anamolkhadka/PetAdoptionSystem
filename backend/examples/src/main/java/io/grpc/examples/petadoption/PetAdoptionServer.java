package io.grpc.examples.petadoption;

import io.grpc.Grpc;
import io.grpc.InsecureServerCredentials;
import io.grpc.Server;
import io.grpc.stub.StreamObserver;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;

public class PetAdoptionServer {
    private static final Logger logger = Logger.getLogger(PetAdoptionServer.class.getName());
    private Server server;

    // In-memory storage for pet records
    private static final List<PetInfo> petDatabase = new ArrayList<>();

    private void start() throws IOException {
        int port = 50052;
        server = Grpc.newServerBuilderForPort(port, InsecureServerCredentials.create()) // Here grpc is creating multi-threaded server.
            .addService(new PetAdoptionServiceImpl())
            .build()
            .start();
        logger.info("Server started, listening on " + port);
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            System.err.println("*** shutting down gRPC server since JVM is shutting down");
            try {
                PetAdoptionServer.this.stop();
            } catch (InterruptedException e) {
                e.printStackTrace(System.err);
            }
            System.err.println("*** server shut down");
        }));
    }

    private void stop() throws InterruptedException {
        if (server != null) {
            server.shutdown().awaitTermination(30, TimeUnit.SECONDS);
        }
    }

    private void blockUntilShutdown() throws InterruptedException {
        if (server != null) {
            server.awaitTermination();
        }
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        final PetAdoptionServer server = new PetAdoptionServer();
        server.start();
        server.blockUntilShutdown();
    }

    // Pet Adoption Service Implementation
    static class PetAdoptionServiceImpl extends PetAdoptionServiceGrpc.PetAdoptionServiceImplBase {
        
        // Here if the client requests for registerPet or searchPet, gRPC assigns separate thread for different clients.
        @Override
        public void registerPet(PetInfo request, StreamObserver<RegistrationResponse> responseObserver) {
            // Add the new pet to the in-memory database
            petDatabase.add(request);
            RegistrationResponse response = RegistrationResponse.newBuilder()
                    .setSuccess(true)
                    .setMessage("Pet registered successfully")
                    .build();
            responseObserver.onNext(response);
            responseObserver.onCompleted();
        }

        @Override
        public void searchPet(SearchRequest request, StreamObserver<PetList> responseObserver) {
            // Filter pets based on the search criteria
            List<PetInfo> matchingPets = new ArrayList<>();
            for (PetInfo pet : petDatabase) {
                if (pet.getName().equalsIgnoreCase(request.getQuery()) ||
                    pet.getGender().equalsIgnoreCase(request.getQuery()) ||
                    String.valueOf(pet.getAge()).equals(request.getQuery()) ||
                    pet.getBreed().equalsIgnoreCase(request.getQuery())) {
                    matchingPets.add(pet);
                }
            }

            // Build the response
            PetList response = PetList.newBuilder().addAllPets(matchingPets).build();
            responseObserver.onNext(response);
            responseObserver.onCompleted();
        }
    }
}