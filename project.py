from typing import List, Optional, Tuple
import os
from datetime import datetime
from utils import (
    validate_date_format, 
    validate_date_range, 
    format_currency,
    get_user_input
)

# Constants
PROJECTS_FILE = "projects.txt"


class Project:
    """
    Represents a crowdfunding project.
    """
    def __init__(self, owner_email: str, title: str, details: str, 
                 target: float, start_date: str, end_date: str):
        """
        Initialize a Project instance.
        
        Args:
            owner_email (str): Email of the project owner
            title (str): Project title
            details (str): Project description
            target (float): Target amount in EGP
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
        """
        self.owner_email = owner_email
        self.title = title
        self.details = details
        self.target = target
        self.start_date = start_date
        self.end_date = end_date
    
    def to_string(self) -> str:
        """
        Convert project to string format for file storage.
        
        Returns:
            str: Comma-separated project data
        """
        return f"{self.owner_email},{self.title},{self.details},{self.target},{self.start_date},{self.end_date}"
    
    @classmethod
    def from_string(cls, data: str) -> Optional['Project']:
        """
        Create Project instance from string data.
        
        Args:
            data (str): Comma-separated project data
            
        Returns:
            Optional[Project]: Project instance or None if invalid data
        """
        try:
            parts = data.strip().split(",", 5)
            if len(parts) != 6:
                return None
            
            owner_email, title, details, target, start_date, end_date = parts
            return cls(owner_email, title, details, float(target), start_date, end_date)
        except (ValueError, IndexError):
            return None
    
    def is_active(self, check_date: Optional[datetime] = None) -> bool:
        """
        Check if project is currently active.
        
        Args:
            check_date (Optional[datetime]): Date to check against, defaults to today
            
        Returns:
            bool: True if project is active, False otherwise
        """
        if check_date is None:
            check_date = datetime.now()
        
        start = validate_date_format(self.start_date)
        end = validate_date_format(self.end_date)
        
        if start is None or end is None:
            return False
        
        return start <= check_date <= end


def load_projects() -> List[Project]:
    """
    Load all projects from the projects file.
    
    Returns:
        List[Project]: List of all projects
    """
    projects = []
    if not os.path.exists(PROJECTS_FILE):
        return projects
    
    try:
        with open(PROJECTS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                project = Project.from_string(line)
                if project:
                    projects.append(project)
    except IOError as e:
        print(f"❌ Error reading projects file: {e}")
    
    return projects


def save_projects(projects: List[Project]) -> bool:
    """
    Save all projects to the projects file.
    
    Args:
        projects (List[Project]): List of projects to save
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(PROJECTS_FILE, "w", encoding="utf-8") as file:
            for project in projects:
                file.write(project.to_string() + "\n")
        return True
    except IOError as e:
        print(f"❌ Error saving projects: {e}")
        return False


def get_user_projects(user_email: str) -> List[Tuple[int, Project]]:
    """
    Get all projects owned by a specific user.
    
    Args:
        user_email (str): Email of the project owner
        
    Returns:
        List[Tuple[int, Project]]: List of tuples (index, project)
    """
    projects = load_projects()
    user_projects = []
    
    for i, project in enumerate(projects):
        if project.owner_email == user_email:
            user_projects.append((i, project))
    
    return user_projects


def create_project(user_email: str) -> None:
    """
    Create a new fundraising project with comprehensive validation.
    
    Args:
        user_email (str): Email of the project creator
    """
    print("\n" + "="*60)
    print("           CREATE NEW CROWDFUNDING PROJECT")
    print("="*60)
    
    # Get project title
    title = get_user_input(
        "Project Title: ",
        str,
        lambda x: len(x.strip()) > 0
    ).strip()
    
    # Get project details
    details = get_user_input(
        "Project Details: ",
        str,
        lambda x: len(x.strip()) > 0
    ).strip()
    
    # Get target amount
    target = get_user_input(
        "Target Amount (EGP): ",
        float,
        lambda x: x > 0
    )
    
    # Get and validate date range
    while True:
        start_date = input("Start Date (YYYY-MM-DD): ")
        end_date = input("End Date (YYYY-MM-DD): ")
        
        if validate_date_range(start_date, end_date):
            # Check if start date is not in the past
            start_datetime = validate_date_format(start_date)
            if start_datetime and start_datetime.date() < datetime.now().date():
                print("❌ Start date cannot be in the past.")
                continue
            break
        else:
            print("❌ Invalid date range. Start date must be before end date.")
            print("   Please use YYYY-MM-DD format.")
    
    # Create and save project
    new_project = Project(user_email, title, details, target, start_date, end_date)
    projects = load_projects()
    projects.append(new_project)
    
    if save_projects(projects):
        print("\n" + "="*60)
        print("✅ Project created successfully!")
        print(f"   Title: {title}")
        print(f"   Target: {format_currency(target)}")
        print(f"   Duration: {start_date} to {end_date}")
        print("="*60)
    else:
        print("❌ Failed to save project. Please try again.")


def view_projects() -> None:
    """
    Display all projects with enhanced formatting.
    """
    print("\n" + "="*80)
    print("                    ALL CROWDFUNDING PROJECTS")
    print("="*80)
    
    projects = load_projects()
    if not projects:
        print("📭 No projects found.")
        print("   Be the first to create a crowdfunding campaign!")
        print("="*80)
        return
    
    current_date = datetime.now()
    
    for idx, project in enumerate(projects, start=1):
        status = "🟢 ACTIVE" if project.is_active(current_date) else "🔴 ENDED"
        
        print(f"\n📋 Project #{idx} {status}")
        print(f"   Owner: {project.owner_email}")
        print(f"   Title: {project.title}")
        print(f"   Details: {project.details}")
        print(f"   Target: {format_currency(project.target)}")
        print(f"   Duration: {project.start_date} to {project.end_date}")
        print("-" * 80)
    
    print("="*80)


def edit_project(user_email: str) -> None:
    """
    Edit a user's own project with improved interface.
    
    Args:
        user_email (str): Email of the project owner
    """
    user_projects = get_user_projects(user_email)
    
    if not user_projects:
        print("\n❌ You have no projects to edit.")
        print("   Create your first project to get started!")
        return
    
    print("\n" + "="*60)
    print("              EDIT YOUR PROJECTS")
    print("="*60)
    
    # Display user's projects
    for idx, (_, project) in enumerate(user_projects, start=1):
        status = "🟢 ACTIVE" if project.is_active() else "🔴 ENDED"
        print(f"{idx}. {project.title} {status}")
        print(f"   Target: {format_currency(project.target)}")
        print(f"   Duration: {project.start_date} to {project.end_date}")
        print("-" * 60)
    
    # Get user selection
    try:
        choice = get_user_input(
            "Enter project number to edit: ",
            int,
            lambda x: 1 <= x <= len(user_projects)
        )
        original_index, selected_project = user_projects[choice - 1]
    except (ValueError, IndexError):
        print("❌ Invalid selection.")
        return
    
    print(f"\nEditing: {selected_project.title}")
    print("Leave field blank to keep current value.\n")
    
    # Get updated values
    title = input(f"Title [{selected_project.title}]: ").strip()
    if not title:
        title = selected_project.title
    
    details = input(f"Details [{selected_project.details}]: ").strip()
    if not details:
        details = selected_project.details
    
    # Get target amount
    target_input = input(f"Target [{format_currency(selected_project.target)}]: ").strip()
    if target_input:
        try:
            target = float(target_input)
            if target <= 0:
                print("❌ Target must be positive. Keeping original value.")
                target = selected_project.target
        except ValueError:
            print("❌ Invalid target amount. Keeping original value.")
            target = selected_project.target
    else:
        target = selected_project.target
    
    # Get date range
    while True:
        start_input = input(f"Start Date [{selected_project.start_date}]: ").strip()
        end_input = input(f"End Date [{selected_project.end_date}]: ").strip()
        
        start_date = start_input if start_input else selected_project.start_date
        end_date = end_input if end_input else selected_project.end_date
        
        if validate_date_range(start_date, end_date):
            break
        else:
            print("❌ Invalid date range. Please try again.")
    
    # Update project
    projects = load_projects()
    projects[original_index] = Project(user_email, title, details, target, start_date, end_date)
    
    if save_projects(projects):
        print("\n✅ Project updated successfully!")
    else:
        print("❌ Failed to update project.")


def delete_project(user_email: str) -> None:
    """
    Delete a user's own project with confirmation.
    
    Args:
        user_email (str): Email of the project owner
    """
    user_projects = get_user_projects(user_email)
    
    if not user_projects:
        print("\n❌ You have no projects to delete.")
        return
    
    print("\n" + "="*60)
    print("              DELETE YOUR PROJECTS")
    print("="*60)
    print("⚠️  WARNING: This action cannot be undone!")
    print("="*60)
    
    # Display user's projects
    for idx, (_, project) in enumerate(user_projects, start=1):
        status = "🟢 ACTIVE" if project.is_active() else "🔴 ENDED"
        print(f"{idx}. {project.title} {status}")
        print(f"   Target: {format_currency(project.target)}")
        print("-" * 60)
    
    # Get user selection
    try:
        choice = get_user_input(
            "Enter project number to delete: ",
            int,
            lambda x: 1 <= x <= len(user_projects)
        )
        original_index, selected_project = user_projects[choice - 1]
    except (ValueError, IndexError):
        print("❌ Invalid selection.")
        return
    
    # Confirm deletion
    print(f"\n⚠️  You are about to delete: {selected_project.title}")
    confirmation = input("Type 'DELETE' to confirm: ").strip()
    
    if confirmation != "DELETE":
        print("❌ Deletion cancelled.")
        return
    
    # Delete project
    projects = load_projects()
    projects.pop(original_index)
    
    if save_projects(projects):
        print("\n✅ Project deleted successfully!")
    else:
        print("❌ Failed to delete project.")


def search_projects_by_date() -> None:
    """
    Search and display projects active on a specific date.
    """
    print("\n" + "="*60)
    print("           SEARCH PROJECTS BY DATE")
    print("="*60)
    
    date_input = input("Enter a date (YYYY-MM-DD): ").strip()
    search_date = validate_date_format(date_input)
    
    if not search_date:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")
        return
    
    projects = load_projects()
    found_projects = []
    
    for project in projects:
        if project.is_active(search_date):
            found_projects.append(project)
    
    if not found_projects:
        print(f"\n📭 No active projects found on {date_input}")
        print("="*60)
        return
    
    print(f"\n🔍 Projects active on {date_input}:")
    print("="*60)
    
    for idx, project in enumerate(found_projects, start=1):
        print(f"\n📋 Project #{idx}")
        print(f"   Owner: {project.owner_email}")
        print(f"   Title: {project.title}")
        print(f"   Details: {project.details}")
        print(f"   Target: {format_currency(project.target)}")
        print(f"   Duration: {project.start_date} to {project.end_date}")
        print("-" * 60)
    
    print("="*60)


def project_menu(user_email: str) -> None:
    """
    Display and handle the project management menu.
    
    Args:
        user_email (str): Email of the logged-in user
    """
    while True:
        print("\n" + "="*60)
        print("              PROJECT MANAGEMENT MENU")
        print("="*60)
        print("1. 🆕 Create New Project")
        print("2. 👀 View All Projects") 
        print("3. ✏️  Edit My Projects")
        print("4. 🗑️  Delete My Project")
        print("5. 🔍 Search Projects by Date")
        print("6. 👤 View My Profile")
        print("7. 🚪 Back to Main Menu")
        print("="*60)
        
        choice = input("Select an option (1-7): ").strip()
        
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
            from auth import display_user_profile
            display_user_profile(user_email)
        elif choice == "7":
            print("\n👋 Returning to main menu...")
            break
        else:
            print("❌ Invalid choice. Please select 1-7.")
            
        # Wait for user to continue
        input("\nPress Enter to continue...")
