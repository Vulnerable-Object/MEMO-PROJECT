#!/usr/bin/env python3
"""
User Authentication Module for Crowdfunding Platform

This module handles all user-related operations including:
- User registration with validation
- User login and authentication
- Email uniqueness checking
- Data persistence to text files

The user data is stored in a simple text file format:
firstname,lastname,email,password,phone

Author: Your Team
Version: 1.0
"""

from utils import validate_email, validate_egyptian_phone
import os

# Configuration: Where we store user account information
USERS_FILE = "users.txt"


def email_exists(email: str) -> bool:
    """
    Check if an email address is already registered in our system.
    
    Args:
        email (str): The email address to check
        
    Returns:
        bool: True if email exists, False otherwise
        
    This prevents users from creating multiple accounts with the same email.
    """
    # If no users file exists yet, then no emails exist
    if not os.path.exists(USERS_FILE):
        return False
        
    # Read through all registered users to check for email duplicates
    with open(USERS_FILE, "r") as file:
        for line in file:
            user_data = line.strip().split(",")
            if len(user_data) >= 3 and user_data[2] == email:
                return True
    return False


def register_user() -> None:
    """
    Register a new user in our crowdfunding platform.
    
    This function guides the user through the registration process:
    1. Collects personal information (name, email, phone)
    2. Validates all input data
    3. Ensures email uniqueness
    4. Securely stores user data
    
    The registration process includes validation for:
    - Email format correctness
    - Email uniqueness (no duplicates)
    - Password confirmation matching
    - Egyptian phone number format
    """
    print("\n🎯 USER REGISTRATION")
    print("=" * 40)
    print("Let's create your account! We need some basic information.")
    print()
    
    # Collect user's personal information
    first_name = input("👤 First Name: ").strip()
    while not first_name:
        print("❌ First name cannot be empty!")
        first_name = input("👤 First Name: ").strip()
        
    last_name = input("👤 Last Name: ").strip()
    while not last_name:
        print("❌ Last name cannot be empty!")
        last_name = input("👤 Last Name: ").strip()

    # Email validation loop - keep asking until we get a valid, unique email
    while True:
        email = input("📧 Email Address: ").strip().lower()
        
        if not email:
            print("❌ Email cannot be empty!")
            continue
            
        if not validate_email(email):
            print("❌ Invalid email format! Please use format like: user@example.com")
            continue
            
        if email_exists(email):
            print("❌ This email is already registered! Please use a different email.")
            continue
            
        # If we reach here, email is valid and unique
        print("✅ Email looks good!")
        break

    # Password setup with confirmation
    while True:
        password = input("🔒 Create Password: ").strip()
        if len(password) < 6:
            print("❌ Password must be at least 6 characters long!")
            continue
            
        confirm_password = input("🔒 Confirm Password: ").strip()
        
        if password != confirm_password:
            print("❌ Passwords don't match! Please try again.")
            continue
            
        # Password is valid and confirmed
        print("✅ Password confirmed!")
        break

    # Egyptian phone number validation
    while True:
        phone = input("📱 Egyptian Phone Number (01XXXXXXXXX): ").strip()
        
        if not phone:
            print("❌ Phone number cannot be empty!")
            continue
            
        if not validate_egyptian_phone(phone):
            print("❌ Invalid Egyptian phone number!")
            print("💡 Format should be: 01XXXXXXXXX (11 digits starting with 01)")
            continue
            
        # Phone number is valid
        print("✅ Phone number is valid!")
        break

    # Save the new user to our database file
    try:
        with open(USERS_FILE, "a", encoding="utf-8") as file:
            file.write(f"{first_name},{last_name},{email},{password},{phone}\n")
        
        print("\n🎉 REGISTRATION SUCCESSFUL!")
        print("=" * 40)
        print(f"Welcome to our platform, {first_name}!")
        print("You can now login and start creating amazing projects!")
        
    except Exception as e:
        print(f"❌ Error saving user data: {e}")
        print("Please try registering again.")


def login_user() -> str | None:
    """
    Authenticate a user and return their email if successful.
    
    Returns:
        str | None: User's email if login successful, None if failed
        
    This function:
    1. Prompts for email and password
    2. Searches through registered users
    3. Validates credentials
    4. Returns email for successful login or None for failure
    """
    print("\n🔐 USER LOGIN")
    print("=" * 30)
    print("Please enter your credentials to access your account.")
    print()
    
    email = input("📧 Email Address: ").strip().lower()
    password = input("🔒 Password: ").strip()
    
    # Check if we have any registered users
    if not os.path.exists(USERS_FILE):
        print("❌ No registered users found!")
        print("💡 Please register first to create an account.")
        return None

    # Search through all registered users
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                user_data = line.strip().split(",")
                
                # Make sure we have complete user data
                if len(user_data) < 4:
                    continue
                    
                stored_email = user_data[2]
                stored_password = user_data[3]
                
                # Check if credentials match
                if email == stored_email and password == stored_password:
                    user_first_name = user_data[0]
                    user_last_name = user_data[1]
                    
                    print(f"\n✅ LOGIN SUCCESSFUL!")
                    print(f"🎉 Welcome back, {user_first_name} {user_last_name}!")
                    print("Let's make some amazing projects happen!")
                    
                    return email
                    
    except Exception as e:
        print(f"❌ Error reading user data: {e}")
        return None
    
    # If we reach here, credentials didn't match
    print("\n❌ LOGIN FAILED!")
    print("The email or password you entered is incorrect.")
    print("💡 Please double-check your credentials and try again.")
    print("💡 If you don't have an account, please register first.")
    
    return None
