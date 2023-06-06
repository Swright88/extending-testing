from faker import Faker
import os

fake = Faker('en_UK')

# Function to add target to the relevant directory
def add_target_to_directory(target, directory):
    surname = target['name'].split()[-1]  # Extract the surname
    filename = f"{surname}"
    filepath = os.path.join(directory, filename)
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist
    with open(filepath, 'a') as file:
        file.write(f"{target['name']}\n")
        file.write(f"{target['address']}\n\n")
        

# Function to add surname to allowlist
def add_surname_to_allowlist(surname):
    filepath = "allowlist"
    with open(filepath, 'a') as file:
        file.write(f"{surname}\n")

# Function to add surname to droplist
def add_surname_to_droplist(surname):
    filepath = "droplist"
    with open(filepath, 'a') as file:
        file.write(f"{surname}\n")

# Ask user for input
while True:
    print("####################")
    print("1. Create a new target")
    print("2. Add an update")
    print("3. Add surname to allowlist")
    print("4. Add surname to droplist")
    print("5. Exit")
    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

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
        original_filename = f"{original_surname}"
        original_filepath = os.path.join("originals", original_filename)
        if not os.path.exists(original_filepath):
            print("Original target not found. Please create the original target first.")
            print()
            continue

        updated_name = input("Enter the updated name: ")
        updated_address = fake.address()  # Generate a new fake address
        target = {
            'name': updated_name,
            'address': updated_address
        }
        add_target_to_directory(target, "updates")
        print("Added as an update.")
        print()

    elif choice == '3':
        # Add surname to allowlist
        surname = input("Enter the surname to add to the allowlist: ")
        add_surname_to_allowlist(surname)
        print(f"Added '{surname}' to the allowlist.")
        print()

    elif choice == '4':
        # Add surname to droplist
        surname = input("Enter the surname to add to the droplist: ")
        add_surname_to_droplist(surname)
        print(f"Added '{surname}' to the droplist.")
        print()

    elif choice == '5':
        print("####################")
        print("Goodbye")
        print("####################")
        break

    else:
        print("Invalid choice. Please try again.")
        print()