import random
import string

def generate_password(length=12):
    """Generate a random password with letters, digits, and symbols."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        if length < 4:
            print("Length must be at least 4. Using 4 instead.")
            length = 4
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12
    
    password = generate_password(length)
    print(f"\nYour password: {password}")

if __name__ == "__main__":
    main()