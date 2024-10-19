# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC Teller.Datetimeteller client."""

from __future__ import print_function

import logging
# from datetime import datetime
import grpc
import petAdoption_pb2
import petAdoption_pb2_grpc


def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        
        
        stub = petAdoption_pb2_grpc.PetAdoptionServiceStub(channel)
        while True:
            print("Welcome to Pet Adoption Service. Please Select from one of the options below")
            print("1.Register a Pet\n2.Search for a Pet\n3.Exit")
            cl_input = int(input("Enter your response:"))
            if cl_input == 1:
                print("Thank you for choosing the pet registration service, you can register your pet for adoption by adding the following details")
                name=input("Enter the pet's Name: ")
                gender=input("Enter the gender of your pet(M/F): ") 
                age=int(input("Enter the age of your pet: "))
                breed=input("Enter the breed of your dog: ")
                pic = input("Please paste the full path of the image you want to upload for you pet: ")
                with open(pic[1:-1], 'rb') as file:
                    image_data = file.read()
                pic = image_data
                response = stub.RegisterPet(petAdoption_pb2.PetInfo(name=name, gender=gender, age=age, breed=breed, picture=pic))
                if response.success:
                    print("Your pet has been registered for adoption.")
                else:
                    print("Some error, Please try again")
                    

                                                           
                #convert the path and make it into byte
                #execute the register pet service


            if cl_input == 2:
                print("You have chosen to search for a Pet (either by name, gender, age, breed)")
                query = input("Search key: ")
                pet_list = stub.SearchPet(petAdoption_pb2.SearchRequest(query=query))
                if pet_list.pets:
                    print("Match(s) found, here are the pets matching the search criteria")
                    for pet in pet_list.pets:
                        print(f"Name: {pet.name}, Gender: {pet.gender}, Age: {pet.age}, Breed: {pet.breed}, Picture: {pet.picture[:10]}", end=" ")
                else:
                    print("No results found with entered criteria, please try again")
                # execute the search method

            if cl_input == 3:
                break

# def run():
#     # NOTE(gRPC Python Team): .close() is possible on a channel and should be
#     # used in circumstances in which the with statement does not fit the needs
#     # of the code.
#     print("Will try to greet world ...")
#     with grpc.insecure_channel("localhost:50051") as channel:
#         stub = helloworld_pb2_grpc.GreeterStub(channel)
#         response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
#     print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()

# python -m grpc_tools.protoc -I "C:\Users\himan\Documents\Masters Program\First Semester\Distributed Systems\Assignments\Project Assignment 2\part3\protos" --python_out=. --pyi_out=. --grpc_python_out=. "C:\Users\himan\Documents\Masters Program\First Semester\Distributed Systems\Assignments\Project Assignment 2\part3\protos\petadoption.proto"