import random
import string

def generate_password(length):
    # Define the character pools
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    # Combine the pools into one
    all_characters = letters + digits + symbols
    
    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    # Prompt user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                raise ValueError("Password length must be at least 1.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
