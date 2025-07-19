#!/usr/bin/env python3
"""
Crowdfunding Application - Main Entry Point

This is a simple command-line crowdfunding platform that allows users to:
- Register and authenticate
- Create fundraising projects
- Browse and search existing projects
- Manage their own projects (edit/delete)

Author: Your Team
Version: 1.0
Date: 2025
"""

from auth import register_user, login_user
from project import project_menu


def display_welcome_banner():
    """Display a friendly welcome banner to greet users."""
    print("=" * 50)
    print("🌟 WELCOME TO THE CROWDFUNDING PLATFORM 🌟")
    print("=" * 50)
    print("Help bring amazing projects to life!")
    print("Support causes you care about.")
    print("Make a difference in your community.")
    print("=" * 50)


def main_menu() -> None:
    """
    Display the main application menu and handle user navigation.
    
    This is the heart of our application - it provides users with
    three main options: register as a new user, login to their account,
    or exit the application gracefully.
    """
    # Show a friendly welcome message when the app starts
    display_welcome_banner()
    
    while True:
        print("\n🏠 MAIN MENU")
        print("-" * 30)
        print("1. 📝 Register as New User")
        print("2. 🔐 Login to Your Account") 
        print("3. 👋 Exit Application")
        print("-" * 30)
        
        choice = input("Please choose an option (1-3): ").strip()

        if choice == "1":
            print("\n🎯 Starting registration process...")
            register_user()
            
        elif choice == "2":
            print("\n🔍 Attempting to log you in...")
            user_email = login_user()
            
            # If login is successful, take user to the project management area
            if user_email:
                print(f"✨ Login successful! Welcome back!")
                project_menu(user_email)
            else:
                print("❌ Login failed. Please try again.")
                
        elif choice == "3":
            print("\n👋 Thank you for using our Crowdfunding Platform!")
            print("💝 Remember: Every small contribution makes a big difference!")
            print("🌟 See you next time!")
            break
            
        else:
            print("❌ Oops! That's not a valid option.")
            print("💡 Please choose 1, 2, or 3.")


if __name__ == "__main__":
    # This is where our application starts running
    print("🚀 Starting Crowdfunding Application...")
    main_menu()
