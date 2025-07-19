from typing import Optional, List
import os
from utils import validate_email, validate_egyptian_phone, get_user_input

# Constants
USERS_FILE = "users.txt"


def email_exists(email: str) -> bool:
    """
    Check if the email already exists in the users file.
    
    Args:
        email (str): The email address to check
        
    Returns:
        bool: True if email exists, False otherwise
    """
    if not os.path.exists(USERS_FILE):
        return False
    
    with open(USERS_FILE, "r", encoding="utf-8") as file:
        for line in file:
            user_data = line.strip().split(",")
            if len(user_data) >= 5 and user_data[2] == email:
                return True
    return False


def get_user_by_email(email: str) -> Optional[List[str]]:
    """
    Retrieve user data by email address.
    
    Args:
        email (str): The email address to search for
        
    Returns:
        Optional[List[str]]: User data as list [first_name, last_name, email, password, phone] 
                           or None if not found
    """
    if not os.path.exists(USERS_FILE):
        return None
    
    with open(USERS_FILE, "r", encoding="utf-8") as file:
        for line in file:
            user_data = line.strip().split(",")
            if len(user_data) >= 5 and user_data[2] == email:
                return user_data
    return None


def validate_password_strength(password: str) -> bool:
    """
    Validate password strength (minimum 6 characters).
    
    Args:
        password (str): The password to validate
        
    Returns:
        bool: True if password meets requirements, False otherwise
    """
    return len(password) >= 6


def register_user() -> None:
    """
    Register a new user with comprehensive validation and store data in users.txt.
    Collects: first name, last name, email, password, confirm password, mobile phone.
    """
    print("\n" + "="*50)
    print("           USER REGISTRATION")
    print("="*50)
    
    # Get first name
    first_name = get_user_input(
        "First Name: ",
        str,
        lambda x: len(x.strip()) > 0
    ).strip()
    
    # Get last name
    last_name = get_user_input(
        "Last Name: ",
        str,
        lambda x: len(x.strip()) > 0
    ).strip()
    
    # Get and validate email
    while True:
        email = input("Email: ").strip().lower()
        if not validate_email(email):
            print("❌ Invalid email format. Please try again.")
            continue
        elif email_exists(email):
            print("❌ Email already registered. Please use a different email.")
            continue
        else:
            break
    
    # Get and validate password
    while True:
        password = input("Password (minimum 6 characters): ")
        if not validate_password_strength(password):
            print("❌ Password must be at least 6 characters long.")
            continue
        
        confirm_password = input("Confirm Password: ")
        if password != confirm_password:
            print("❌ Passwords do not match. Please try again.")
            continue
        else:
            break
    
    # Get and validate Egyptian phone number
    while True:
        phone = input("Mobile Phone (Egyptian number): ")
        if not validate_egyptian_phone(phone):
            print("❌ Invalid Egyptian phone number. Format: 01XXXXXXXXX")
            print("   Valid prefixes: 010, 011, 012, 015")
            continue
        else:
            break
    
    # Save user data to file
    try:
        with open(USERS_FILE, "a", encoding="utf-8") as file:
            file.write(f"{first_name},{last_name},{email},{password},{phone}\n")
        
        print("\n" + "="*50)
        print("✅ Registration successful!")
        print(f"   Welcome {first_name} {last_name}!")
        print("   You can now login with your email and password.")
        print("="*50)
        
    except IOError as e:
        print(f"❌ Error saving user data: {e}")


def login_user() -> Optional[str]:
    """
    Authenticate user login and return their email if successful.
    
    Returns:
        Optional[str]: User email if login successful, None otherwise
    """
    print("\n" + "="*50)
    print("              USER LOGIN")
    print("="*50)
    
    if not os.path.exists(USERS_FILE):
        print("❌ No registered users found. Please register first.")
        return None
    
    # Get login credentials
    email = input("Email: ").strip().lower()
    password = input("Password: ")
    
    # Authenticate user
    user_data = get_user_by_email(email)
    if user_data and len(user_data) >= 5 and user_data[3] == password:
        print("\n" + "="*50)
        print(f"✅ Welcome back {user_data[0]} {user_data[1]}!")
        print("   Login successful!")
        print("="*50)
        return email
    else:
        print("\n❌ Incorrect email or password.")
        print("   Please check your credentials and try again.")
        return None


def display_user_profile(email: str) -> None:
    """
    Display user profile information.
    
    Args:
        email (str): The email of the user whose profile to display
    """
    user_data = get_user_by_email(email)
    if user_data:
        print("\n" + "="*50)
        print("              USER PROFILE")
        print("="*50)
        print(f"Name: {user_data[0]} {user_data[1]}")
        print(f"Email: {user_data[2]}")
        print(f"Phone: {user_data[4]}")
        print("="*50)
    else:
        print("❌ User profile not found.")
