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
        name=input("Enter the pet's Name: ")
        gender=input("Enter the gender of your pet(M/F): ") 
        age=input("Enter the age of your pet: ")
        breed=input("Enter the breed of your dog: ")
        pic = bytes('svome string of pic')
        
        stub = petAdoption_pb2_grpc.PetAdoptionStub(channel)
        response = stub.RsegisterPet(petAdoption_pb2.PetInfo(name=name, gender=gender, age=int(age), breed=breed, picture=pic))
        # response = stub.RegisterPet(petadoption_pb2.PetRequests(name='Pluto', gender='M', age='12', breed='pet'))
        if response.success:
            print(f"Pet Registered Successfully")
        else:
            print("Some error occured")
        search = 'pluto'
        pet_list = stub.SearchPet(petAdoption_pb2.SearchRequest(query='pluto'))
        for pet in pet_list:
            print(pet)
       

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