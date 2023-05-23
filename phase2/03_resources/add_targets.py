from faker import Faker
import os
fake = Faker('en)UK')

# Initissssssssssssalize Faker
fake = Faker('en_UK')

# Function to add target to the relevant directory
def add_target_to_directory(target, directory):
    surname = target['name'].split()[-1]  # Extract the surname
    filename = f"{surname}.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, 'a') as file:
        file.write(f"{target['name']}\n")
        file.write(f"{target['address']}\n\n")

# Ask user for input
while True:
    print("1. Create a new target")
    print("2. Add an update")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        # Generate a new target
        target = {
            'name': fake.name(),
            'address': fake.address()
        }
        print("Target:")
        print("Name:", target['name'])
        print("Address:", target['address'])
        add_target_to_directory(target, "originals")
        print("Added to originals.")
        print()

    elif choice == '2':
        # Add an update manually
        original_surname = input("Enter the surname of the original target: ")
        original_filename = f"{original_surname}.txt"
        original_filepath = os.path.join("originals", original_filename)
        if not os.path.exists(original_filepath):
            print("Original target not found. Please create the original target first.")
            print()
            continue

        updated_name = input("Enter the updated name: ")
        updated_address = input("Enter the updated address: ")

        target = {
            'name': updated_name,
            'address': updated_address
        }
        add_target_to_directory(target, "updates")
        print("Added as an update.")
        print()

    elif choice == '3':
        # Exit the program
        break

    else:
        print("Invalid choice. Please try again.")
        print()