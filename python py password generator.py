import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    print("Generated Password:", generate_password(password_length))
