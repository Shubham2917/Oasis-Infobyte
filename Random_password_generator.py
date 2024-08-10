import random
import string

def generate_password(length):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    all_characters = lowercase + uppercase + digits + special

    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    password = generate_password(length)

    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
