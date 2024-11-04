import os
import getpass

def main():
    # Get the current user's username and home directory
    username = getpass.getuser()
    home_dir = os.path.expanduser(f"~/{username}")
    profile_file_path = os.path.join(home_dir, 'profile.txt')

    # Check if the current directory matches the user's home directory
    current_dir = os.getcwd()
    if current_dir != home_dir:
        # Create the user's directory if it doesn't match
        os.makedirs(home_dir, exist_ok=True)

    # Check if the profile file exists
    if os.path.exists(profile_file_path):
        # Open and read the existing profile
        with open(profile_file_path, 'r') as file:
            content = file.readlines()
        
        # Display the existing information to the user
        profile_info = {
            'Name': content[0].strip(),
            'Phone': content[1].strip(),
            'Email': content[2].strip()
        }
        
        print("Current Profile Information:")
        for key, value in profile_info.items():
            print(f"{key}: {value}")
        
        # Ask the user if the information is up-to-date
        update = input("Is this information up-to-date? (yes/no): ").strip().lower()
        
        if update != 'yes':
            # Prompt the user for updated information if not up-to-date
            profile_info = {
                'Name': input("Enter your name: ").strip(),
                'Phone': input("Enter your phone number: ").strip(),
                'Email': input("Enter your email: ").strip()
            }
            # Write the updated information to the profile file
            with open(profile_file_path, 'w') as file:
                for value in profile_info.values():
                    file.write(value + '\n')
            print("Profile updated successfully.")
        else:
            print("Profile is up-to-date.")
    else:
        # If profile file doesn't exist, prompt user for new profile information
        print("Profile file not found. Creating a new profile.")
        profile_info = {
            'Name': input("Enter your name: ").strip(),
            'Phone': input("Enter your phone number: ").strip(),
            'Email': input("Enter your email: ").strip()
        }
        # Write the new information to the profile file
        with open(profile_file_path, 'w') as file:
            for value in profile_info.values():
                file.write(value + '\n')
        print("Profile created successfully.")

if __name__ == "__main__":
    main()
