# Project 2 Part 3 and 4 - Pet Adoption System

## Part 3 

- Server is implemented inside backend using java startup kit.
- Client is implemented inside client_2 using python.
- Both Server and Client are using the same proto file inside the Proto directory.
- The file path for the PetAdoptionServer source code is /backend/examples/src/main/java/io/grpc/examples/petadoption/PetAdoptionServer.java. 
  It is the same directory where helloworld java server is located.

### *** Steps to run the program ***

### Running Server
- Open one terminal to run the Java Server.
- cd to 'backend/examples'.
- Run command './gradlew installDist'.Wait for build to be successful.
- Run command './build/install/examples/bin/pet-adoption-server' to start the Java Server.
- Expected output:
" anamolkhadka@Anamols-MacBook-Pro examples % ./build/install/examples/bin/pet-adoption-server
  Oct 19, 2024 3:42:53 PM io.grpc.examples.petadoption.PetAdoptionServer start
  INFO: Server started, listening on 50052 "
- See the Backend screenshot in the screenshot folder.

### Running Client
- Open another terminal to run the Client application.
- Note: make sure the necessary python packages like pip, grpcio, grpcio-tools are installed. Activate conda environment if you want to use package manager and install the grpc packages inside the environment.
- cd to 'client_2' folder.
- Run command 'python client.py'.
- Follow the program logic as shown in the screenShots inside screenShot folder.
- For pet information check petInfo.txt inside the client_2.
- For images file name look at the images directory inside th client_2 and provide those corresponding image names as shown in the petInfo.txt examples.
- Note the image preview of the first 20 bytes might look the same for different dog's images due to the fact that both are same file format and the first bytes are the meta data.
- However, the total size of each of the pictures in bytes are different to distinguish that the images are different.

### Database
- The server is using in-memory database using an Array List of type PetInfo.


## Part 4

### Write 5 different test cases for your developed pet adoption system.
- The test cases are in the test.py python file inside the client_2 directory.
- To run the test cases, first exit the server to clear the in-memory storage for avoiding duplicates.
- The run the java backend server in one terminal like mentioned above, open another terminal cd to 'client_2' folder.
- Run command 'python test.py' same as running 'client.py' as described above.
- See the TestCases screenshot in the screenshots directory.
- For details about the test cases open the test.py file and read different test cases comments.
