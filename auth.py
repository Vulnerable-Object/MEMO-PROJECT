from utils import validate_email, validate_egyptian_phone
import os

USERS_FILE = "users.txt"

def email_exists(email: str) -> bool:
    """Check if the email already exists in the users file."""
    if not os.path.exists(USERS_FILE):
        return False
    with open(USERS_FILE, "r") as file:
        for line in file:
            if line.strip().split(",")[2] == email:
                return True
    return False


def register_user() -> None:
    """Register a new user and store data in users.txt."""
    print("\n--- Register ---")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    while True:
        email = input("Email: ")
        if not validate_email(email):
            print("Invalid email format.")
        elif email_exists(email):
            print("Email already registered.")
        else:
            break

    while True:
        password = input("Password: ")
        confirm = input("Confirm Password: ")
        if password != confirm:
            print("Passwords do not match.")
        else:
            break

    while True:
        phone = input("Phone Number: ")
        if not validate_egyptian_phone(phone):
            print("Invalid Egyptian phone number.")
        else:
            break

    with open(USERS_FILE, "a") as file:
        file.write(f"{first_name},{last_name},{email},{password},{phone}\n")

    print("Registration successful.")


def login_user() -> str | None:
    """Login user and return their email if successful."""
    print("\n--- Login ---")
    email = input("Email: ")
    password = input("Password: ")

    if not os.path.exists(USERS_FILE):
        print("No registered users found.")
        return None

    with open(USERS_FILE, "r") as file:
        for line in file:
            user_data = line.strip().split(",")
            if email == user_data[2] and password == user_data[3]:
                print(f"Welcome {user_data[0]} {user_data[1]}!")
                return email
    print("❌ Incorrect email or password.")
    return None
