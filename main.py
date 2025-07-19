from auth import register_user, login_user
from project import project_menu

def main_menu() -> None:
    """Display the main application menu."""
    while True:
        print("\n===== Crowdfunding App =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user_email = login_user()
            if user_email:
                project_menu(user_email)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
