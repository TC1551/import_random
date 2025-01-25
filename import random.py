import random
import string

# Pre-defined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Quick", "Smart", "Bright", "Lucky", "Silent", "Brave", "Crazy", "Gentle"]
nouns = ["Tiger", "Dragon", "Eagle", "Panda", "Shark", "Wolf", "Fox", "Hawk", "Bear", "Lion"]

# Function to generate random usernames
def generate_username(include_numbers=True, include_special_chars=True, username_length=None):
    # Base username creation
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    # Add numbers
    if include_numbers:
        username += str(random.randint(10, 99))

    # Add special characters
    if include_special_chars:
        username += random.choice("!@#$%^&*")

    # Adjust to custom length if specified
    if username_length and username_length > len(username):
        extra_chars = random.choices(string.ascii_letters + string.digits, k=(username_length - len(username)))
        username += ''.join(extra_chars)

    return username[:username_length] if username_length else username

# Function to save usernames to a file
def save_usernames_to_file(usernames, file_name="usernames.txt"):
    try:
        with open(file_name, "w") as file:
            for username in usernames:
                file.write(username + "\n")
        print(f"Usernames saved to {file_name}")
    except Exception as e:
        print(f"Error saving usernames: {e}")

# Main program
def main():
    print("Welcome to the Random Username Generator!")
    
    # User preferences
    num_usernames = int(input("How many usernames would you like to generate? "))
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    username_length = input("Set a custom length for the usernames (press Enter to skip): ")
    username_length = int(username_length) if username_length.isdigit() else None

    # Generate usernames
    usernames = [generate_username(include_numbers, include_special_chars, username_length) for _ in range(num_usernames)]
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)

    # Save to file option
    save_to_file = input("\nDo you want to save these usernames to a file? (yes/no): ").strip().lower() == "yes"
    if save_to_file:
        save_usernames_to_file(usernames)

if __name__ == "__main__":
    main()
