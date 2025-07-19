"""
Crowdfunding Console Application

A comprehensive console-based crowdfunding platform that allows users to:
- Register and login with Egyptian phone validation
- Create fundraising campaigns with target amounts and duration
- View, edit, and delete their own projects
- Search projects by date
- Browse all available projects

Author: Crowdfunding Team
Version: 1.0
"""

from typing import Optional
from auth import register_user, login_user
from project import project_menu


def display_welcome_banner() -> None:
    """Display the application welcome banner."""
    print("\n" + "="*70)
    print("                 🌟 CROWDFUNDING PLATFORM 🌟")
    print("="*70)
    print("        Turn your dreams into reality with community support!")
    print("           Create campaigns • Fund projects • Make impact")
    print("="*70)


def display_main_menu() -> None:
    """Display the main application menu options."""
    print("\n" + "="*50)
    print("                  MAIN MENU")
    print("="*50)
    print("1. 📝 Register New Account")
    print("2. 🔐 Login to Your Account")
    print("3. ℹ️  About Crowdfunding")
    print("4. 🚪 Exit Application")
    print("="*50)


def display_about_info() -> None:
    """Display information about crowdfunding."""
    print("\n" + "="*70)
    print("                    ABOUT CROWDFUNDING")
    print("="*70)
    print("📖 What is Crowdfunding?")
    print("   Crowdfunding is the practice of funding a project or venture")
    print("   by raising small amounts of money from a large number of people,")
    print("   typically via the Internet.")
    print()
    print("💡 How it Works:")
    print("   • Create a compelling project with clear goals")
    print("   • Set a realistic funding target")
    print("   • Share your campaign with potential supporters")
    print("   • Reach your goal with community support!")
    print()
    print("🎯 Popular Campaign Types:")
    print("   • Creative projects (art, music, film)")
    print("   • Technology innovations")
    print("   • Community initiatives")
    print("   • Charitable causes")
    print("   • Educational programs")
    print()
    print("📊 Fun Fact:")
    print("   In 2015, over US$34 billion was raised worldwide through")
    print("   crowdfunding platforms!")
    print("="*70)


def get_user_choice() -> str:
    """
    Get and validate user menu choice.
    
    Returns:
        str: User's menu selection
    """
    while True:
        choice = input("Choose an option (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("❌ Invalid option. Please choose 1, 2, 3, or 4.")


def handle_registration() -> None:
    """Handle user registration process."""
    print("\n🎉 Welcome to our crowdfunding community!")
    print("   Let's create your account to get started.")
    register_user()


def handle_login() -> Optional[str]:
    """
    Handle user login process.
    
    Returns:
        Optional[str]: User email if login successful, None otherwise
    """
    print("\n👋 Welcome back!")
    print("   Please enter your credentials to continue.")
    return login_user()


def main_menu() -> None:
    """
    Main application loop that handles user navigation and menu operations.
    """
    display_welcome_banner()
    
    while True:
        display_main_menu()
        choice = get_user_choice()
        
        if choice == "1":
            handle_registration()
            
        elif choice == "2":
            user_email = handle_login()
            if user_email:
                # User successfully logged in, enter project management
                project_menu(user_email)
                
        elif choice == "3":
            display_about_info()
            input("\nPress Enter to return to main menu...")
            
        elif choice == "4":
            print("\n" + "="*50)
            print("         Thank you for using our platform!")
            print("              💫 Dream • Create • Fund 💫")
            print("                    Goodbye! 👋")
            print("="*50)
            break


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n🛑 Application interrupted by user.")
        print("   Thank you for using our crowdfunding platform!")
        print("   Goodbye! 👋")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("   Please try running the application again.")
        print("   If the problem persists, contact support.")
