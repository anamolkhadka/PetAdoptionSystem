import os
import grpc
import petadoption_pb2
import petadoption_pb2_grpc

def run():
    # Create a gRPC channel to connect to the server
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = petadoption_pb2_grpc.PetAdoptionServiceStub(channel)
        
        while True:
            # Display the menu options
            print("\nWelcome to the Pet Adoption Service. Please select an option below:")
            print("1. Register a Pet")
            print("2. Search for a Pet")
            print("3. Exit")
            choice = input("Enter your choice: ")

            # Handle the choices
            if choice == "1":
                print("\nPet Registration:")
                name = input("Enter the pet's name: ")
                gender = input("Enter the pet's gender (M/F): ")
                age = int(input("Enter the pet's age: "))
                breed = input("Enter the pet's breed: ")
                
                # Image input and conversion to bytes
                image_path = input("Enter the image file name (inside the 'images' folder): ")
                full_image_path = os.path.join("images", image_path)
                print(f"Looking for the image at: {full_image_path}")
                
                # Read the image as bytes
                try:
                    with open(full_image_path, 'rb') as file: # Reading raw binary data of the image file.
                        image_data = file.read()
                except FileNotFoundError:
                    print("Error: The specified image file does not exist. Please try again.")
                    continue

                # Create a PetInfo message
                pet_info = petadoption_pb2.PetInfo(
                    name=name,
                    gender=gender,
                    age=age,
                    breed=breed,
                    picture=image_data
                )

                # Call the RegisterPet method
                response = stub.RegisterPet(pet_info)
                if response.success:
                    print("Pet registered successfully!")
                else:
                    print("Failed to register the pet. Please try again.")

            elif choice == "2":
                print("\nPet Search:")
                query = input("Enter a search term (name, gender, age, or breed): ")

                # Create a SearchRequest message
                search_request = petadoption_pb2.SearchRequest(query=query)

                # Call the SearchPet method
                pet_list = stub.SearchPet(search_request)
                if pet_list.pets:
                    print("\nMatching Pets Found:")
                    for pet in pet_list.pets:
                        print(f"Name: {pet.name}, Gender: {pet.gender}, Age: {pet.age}, Breed: {pet.breed}")
                        print(f"Image size (in bytes): {len(pet.picture)}")
                        print(f"Image preview (first 20 bytes): {pet.picture[:20]}\n")
                else:
                    print("No pets found matching the search criteria.")

            elif choice == "3":
                print("Exiting the Pet Adoption Service. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    run()
