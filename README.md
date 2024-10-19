# Project 2 Part 3 and 4 - Pet Adoption System

## Part 3 

- Server is implemented inside backend using java startup kit.
- Client is implemented inside client_2 using python.
- Both Server and Client are using the same proto file inside the Proto directory.

*** Steps to run the program ***

### Running Server
- Open one terminal to run the Java Server.
- cd to 'backend/examples'.
- Run command './gradlew installDist'.Wait for build to be successful.
- Run command './build/install/examples/bin/pet-adoption-server' to start the Java Server.
- Expected output:
" anamolkhadka@Anamols-MacBook-Pro examples % ./build/install/examples/bin/pet-adoption-server
  Oct 19, 2024 3:42:53 PM io.grpc.examples.petadoption.PetAdoptionServer start
  INFO: Server started, listening on 50052 "

### Running Client
- Open another terminal to run the Client application.
- Note: make sure the necessary python packages like pip, grpcio, grpcio-tools are installed. Activate conda environment if you want to use package manager and install the grpc packages inside the environment.
- cd to 'client_2' folder.
- Run command 'python client.py'.
- Follow the program logic as shown in the screenShots inside screenShot folder.
- For pet information check petInfo.txt inside the client_2.
