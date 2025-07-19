import os
from datetime import datetime

PROJECTS_FILE = "projects.txt"


def create_project(user_email: str) -> None:
    """Create a new fundraising project."""
    print("\n--- Create New Project ---")
    title = input("Title: ")
    details = input("Details: ")

    while True:
        try:
            target = float(input("Total Target (EGP): "))
            if target <= 0:
                print("Target must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        start_date = input("Start Date (YYYY-MM-DD): ")
        end_date = input("End Date (YYYY-MM-DD): ")
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            if start >= end:
                print("Start date must be before end date.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    with open(PROJECTS_FILE, "a") as file:
        file.write(f"{user_email},{title},{details},{target},{start_date},{end_date}\n")

    print("✅ Project created successfully!")


def view_projects() -> None:
    """Display all projects."""
    print("\n--- All Projects ---")
    if not os.path.exists(PROJECTS_FILE):
        print("No projects found.")
        return

    with open(PROJECTS_FILE, "r") as file:
        for idx, line in enumerate(file, start=1):
            email, title, details, target, start, end = line.strip().split(",", 5)
            print(f"\nProject #{idx}")
            print(f"Owner: {email}")
            print(f"Title: {title}")
            print(f"Details: {details}")
            print(f"Target: {target} EGP")
            print(f"Duration: {start} to {end}")


def edit_project(user_email: str) -> None:
    """Edit a user's own project."""
    if not os.path.exists(PROJECTS_FILE):
        print("No projects found.")
        return

    with open(PROJECTS_FILE, "r") as file:
        lines = file.readlines()

    my_projects = [(i, line.strip()) for i, line in enumerate(lines) if line.startswith(user_email + ",")]

    if not my_projects:
        print("You have no projects to edit.")
        return

    print("\n--- Your Projects ---")
    for idx, (i, proj) in enumerate(my_projects, start=1):
        _, title, *_ = proj.split(",", 5)
        print(f"{idx}. {title}")

    try:
        choice = int(input("Enter project number to edit: "))
        original_index = my_projects[choice - 1][0]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    print("Leave field blank to keep current value.")

    old_data = lines[original_index].strip().split(",", 6)
    _, old_title, old_details, old_target, old_start, old_end = old_data

    title = input(f"Title [{old_title}]: ") or old_title
    details = input(f"Details [{old_details}]: ") or old_details

    while True:
        target = input(f"Target [{old_target}]: ")
        if not target:
            target = old_target
            break
        try:
            if float(target) <= 0:
                print("Target must be positive.")
            else:
                break
        except ValueError:
            print("Enter a valid number.")

    while True:
        start = input(f"Start Date [{old_start}]: ") or old_start
        end = input(f"End Date [{old_end}]: ") or old_end
        try:
            start_date = datetime.strptime(start, "%Y-%m-%d")
            end_date = datetime.strptime(end, "%Y-%m-%d")
            if start_date >= end_date:
                print("Start must be before end.")
            else:
                break
        except ValueError:
            print("Invalid date format.")

    lines[original_index] = f"{user_email},{title},{details},{target},{start},{end}\n"
    with open(PROJECTS_FILE, "w") as file:
        file.writelines(lines)

    print("✅ Project updated.")


def delete_project(user_email: str) -> None:
    """Delete a user's own project."""
    if not os.path.exists(PROJECTS_FILE):
        print("No projects found.")
        return

    with open(PROJECTS_FILE, "r") as file:
        lines = file.readlines()

    my_projects = [(i, line.strip()) for i, line in enumerate(lines) if line.startswith(user_email + ",")]

    if not my_projects:
        print("You have no projects to delete.")
        return

    print("\n--- Your Projects ---")
    for idx, (i, proj) in enumerate(my_projects, start=1):
        _, title, *_ = proj.split(",", 5)
        print(f"{idx}. {title}")

    try:
        choice = int(input("Enter project number to delete: "))
        original_index = my_projects[choice - 1][0]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    lines.pop(original_index)

    with open(PROJECTS_FILE, "w") as file:
        file.writelines(lines)

    print("✅ Project deleted.")


def search_projects_by_date() -> None:
    """Search and display projects by a given date."""
    date_input = input("Enter a date (YYYY-MM-DD): ")
    try:
        search_date = datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    found = False
    with open(PROJECTS_FILE, "r") as file:
        for line in file:
            fields = line.strip().split(",", 6)
            if len(fields) < 6:
                continue
            _, title, details, target, start, end = fields
            try:
                start_date = datetime.strptime(start, "%Y-%m-%d")
                end_date = datetime.strptime(end, "%Y-%m-%d")
                if start_date <= search_date <= end_date:
                    found = True
                    print(f"\nTitle: {title}")
                    print(f"Details: {details}")
                    print(f"Target: {target}")
                    print(f"From: {start} To: {end}")
            except ValueError:
                continue

    if not found:
        print("No projects found on that date.")


def project_menu(user_email: str) -> None:
    """Menu for project-related operations."""
    while True:
        print("\n--- Project Menu ---")
        print("1. Create Project")
        print("2. View All Projects")
        print("3. Edit My Projects")
        print("4. Delete My Project")
        print("5. Search by Date")
        print("6. Back to Main Menu")
        choice = input("Select: ")

        if choice == "1":
            create_project(user_email)
        elif choice == "2":
            view_projects()
        elif choice == "3":
            edit_project(user_email)
        elif choice == "4":
            delete_project(user_email)
        elif choice == "5":
            search_projects_by_date()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
