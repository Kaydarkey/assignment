import os
import json

def handle_user_login(user):
    # Set the home directory as the base directory
    home_dir = os.path.expanduser("~")
    
    # Define the path to the user's directory within the home directory
    user_dir = os.path.join(home_dir, user['name'])

    # Check if the current working directory is the user's directory
    if os.getcwd() != user_dir:
        print(f"Current working directory is not {user_dir}. Navigating to user's directory...")

        # If the user directory doesn't exist in the home directory, create it
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
            print(f"Directory created for user: {user['name']}")
        else:
            print(f"Directory already exists for user: {user['name']}")

        # Change the current working directory to the user's directory
        os.chdir(user_dir)
        print(f"Moved to user's directory: {os.getcwd()}")
    
    # Define the path to the profile.txt file in the user's directory
    profile_path = os.path.join(user_dir, 'profile.txt')

    # Check if profile.txt exists and read its details
    if os.path.exists(profile_path):
        # Load the existing profile data
        with open(profile_path, 'r') as profile_file:
            stored_data = json.load(profile_file)

        # Check if stored details match the current user details
        if (stored_data.get("email") != user["email"] or 
                stored_data.get("phone") != user["phone"]):
            print("Profile details are outdated. Please confirm or update the details.")
            # Ask user to confirm/update details
            user_confirm = input("Do you want to update your profile? (yes/no): ").strip().lower()
            if user_confirm == 'yes':
                # Update the profile.txt with new data
                with open(profile_path, 'w') as profile_file:
                    json.dump(user, profile_file)
                print("Profile updated successfully.")
            else:
                print("Profile not updated.")
        else:
            print("Profile details are up-to-date.")
    else:
        # If profile.txt doesn't exist, create it with the current user data
        with open(profile_path, 'w') as profile_file:
            json.dump(user, profile_file)
        print(f"Profile created for user: {user['name']}")

# Example user data
user_data = {
    "name": "kafuidarkey",
    "email": "kafuid@example.com",
    "phone": "0503736391"
}

# Run the function
handle_user_login(user_data)
