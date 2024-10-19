import grpc
import petadoption_pb2
import petadoption_pb2_grpc

def test_register_pet(stub, name, gender, age, breed, image_path):
    print(f"\nTest: Register Pet - {name}")
    try:
        # Read the image file as bytes if the path is provided
        image_data = b''
        if image_path:
            with open(image_path, 'rb') as file:
                image_data = file.read()
        
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
        print(f"Response: {response.message}")
        return response.success
    except Exception as e:
        print(f"Error during registration: {e}")
        return False

def test_search_pet(stub, query):
    print(f"\nTest: Search Pet - Query: {query}")
    # Create a SearchRequest message
    search_request = petadoption_pb2.SearchRequest(query=query)
    
    # Call the SearchPet method
    pet_list = stub.SearchPet(search_request)
    if pet_list.pets:
        print("\nMatching Pets Found:")
        for pet in pet_list.pets:
            print(f"Name: {pet.name}, Gender: {pet.gender}, Age: {pet.age}, Breed: {pet.breed}")
            print(f"Image preview (first 10 bytes): {pet.picture[:10]}\n")
    else:
        print("No pets found matching the search criteria.")
    return len(pet_list.pets)

def run_tests():
    # Connect to the gRPC server
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = petadoption_pb2_grpc.PetAdoptionServiceStub(channel)

        # Test Case 1: Register a New Pet Successfully
        print("\nRunning Test Case 1: Register a New Pet Successfully")
        test_register_pet(stub, "Buddy", "Male", 3, "Labrador Retriever", "images/buddy.jpg")

        # Test Case 2: Search for a Registered Pet by Name
        print("\nRunning Test Case 2: Search for a Registered Pet by Name")
        test_search_pet(stub, "Buddy")

        # Test Case 3: Register a Pet with Missing Information
        print("\nRunning Test Case 3: Register a Pet with Missing Information")
        # Attempt to register a pet with missing gender
        success = test_register_pet(stub, "Max", "", 2, "German Shepherd", "images/max.jpg")
        if not success:
            print("Test Case 3 Passed: Registration failed as expected due to missing information.")
        else:
            print("Test Case 3 Failed: Registration succeeded when it should have failed.")

        # Test Case 4: Search for a Non-Existent Pet
        print("\nRunning Test Case 4: Search for a Non-Existent Pet")
        test_search_pet(stub, "Charlie")

        # Test Case 5: Register Multiple Pets and Perform a Complex Search
        print("\nRunning Test Case 5: Register Multiple Pets and Perform a Complex Search")
        test_register_pet(stub, "Daisy", "Female", 2, "Beagle", "images/daisy.jpg")
        test_register_pet(stub, "Bella", "Female", 4, "Poodle", "images/bella.jpg")
        test_register_pet(stub, "Max", "Male", 1, "German Shepherd", "images/max.jpg")
        test_search_pet(stub, "Female")

if __name__ == "__main__":
    run_tests()
