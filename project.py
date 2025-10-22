#!/usr/bin/env python3
"""
Project Management Module for Crowdfunding Platform

This module handles all project-related operations including:
- Creating new fundraising projects
- Viewing and browsing all projects
- Editing user's own projects
- Deleting projects
- Searching projects by date range
- Project data persistence

Project data format in projects.txt:
email,title,details,target_amount,start_date,end_date

Author: Your Team
Version: 1.0
"""

import os
from datetime import datetime
from utils import (
    format_currency, 
    is_valid_date_format, 
    dates_are_logical, 
    clean_text_input,
    is_positive_number
)

# Configuration: Where we store project information
PROJECTS_FILE = "projects.txt"


def create_project(user_email: str) -> None:
    """
    Guide a user through creating a new fundraising project.
    
    Args:
        user_email (str): Email of the authenticated user creating the project
        
    This function collects and validates:
    - Project title and description
    - Fundraising target amount
    - Project start and end dates
    
    All data is validated before saving to ensure data integrity.
    """
    print("\n🚀 CREATE NEW PROJECT")
    print("=" * 50)
    print("Let's bring your amazing idea to life!")
    print("We'll need some details about your fundraising project.")
    print()
    
    # Get project title with validation
    while True:
        title = input("📝 Project Title: ").strip()
        if not title:
            print("❌ Project title cannot be empty!")
            continue
        if len(title) < 5:
            print("❌ Title should be at least 5 characters long!")
            continue
        if len(title) > 100:
            print("❌ Title is too long! Please keep it under 100 characters.")
            continue
        
        # Clean the title
        title = clean_text_input(title)
        print(f"✅ Great title: '{title}'")
        break
    
    # Get project description
    while True:
        details = input("📄 Project Description: ").strip()
        if not details:
            print("❌ Project description cannot be empty!")
            continue
        if len(details) < 20:
            print("❌ Please provide more details (at least 20 characters)!")
            print("💡 Tell people what your project is about and why it matters.")
            continue
        if len(details) > 500:
            print("❌ Description is too long! Please keep it under 500 characters.")
            continue
            
        # Clean the description
        details = clean_text_input(details)
        print("✅ Excellent description!")
        break
    
    # Get fundraising target
    while True:
        target_input = input("💰 Fundraising Target (EGP): ").strip()
        
        if not target_input:
            print("❌ Please enter a target amount!")
            continue
            
        if not is_positive_number(target_input):
            print("❌ Please enter a valid positive number!")
            print("💡 Example: 5000 or 10000.50")
            continue
            
        target_amount = float(target_input)
        
        if target_amount < 100:
            print("❌ Minimum fundraising target is 100 EGP!")
            continue
        if target_amount > 10000000:  # 10 million EGP
            print("❌ Maximum fundraising target is 10,000,000 EGP!")
            continue
            
        print(f"✅ Target set to {format_currency(target_amount)}")
        break
    
    # Get project dates
    print("\n📅 Project Timeline:")
    print("Please enter dates in YYYY-MM-DD format (e.g., 2025-07-15)")
    
    while True:
        start_date = input("🗓️  Start Date: ").strip()
        
        if not start_date:
            print("❌ Start date cannot be empty!")
            continue
            
        if not is_valid_date_format(start_date):
            print("❌ Invalid date format! Please use YYYY-MM-DD")
            print("💡 Example: 2025-07-15")
            continue
            
        # Check if start date is not in the past
        try:
            start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
            if start_datetime.date() < datetime.now().date():
                print("❌ Start date cannot be in the past!")
                continue
        except ValueError:
            print("❌ Invalid date!")
            continue
            
        print(f"✅ Start date: {start_date}")
        break
    
    while True:
        end_date = input("🗓️  End Date: ").strip()
        
        if not end_date:
            print("❌ End date cannot be empty!")
            continue
            
        if not is_valid_date_format(end_date):
            print("❌ Invalid date format! Please use YYYY-MM-DD")
            continue
            
        if not dates_are_logical(start_date, end_date):
            print("❌ End date must be after start date!")
            print(f"💡 Your start date is {start_date}")
            continue
            
        # Check if project duration is reasonable (at least 1 day, max 365 days)
        try:
            start_dt = datetime.strptime(start_date, "%Y-%m-%d")
            end_dt = datetime.strptime(end_date, "%Y-%m-%d")
            duration = (end_dt - start_dt).days
            
            if duration > 365:
                print("❌ Project duration cannot exceed 365 days!")
                continue
                
        except ValueError:
            print("❌ Invalid date!")
            continue
            
        print(f"✅ End date: {end_date}")
        break
    
    # Save the project
    try:
        with open(PROJECTS_FILE, "a", encoding="utf-8") as file:
            file.write(f"{user_email},{title},{details},{target_amount},{start_date},{end_date}\n")
        
        print("\n🎉 PROJECT CREATED SUCCESSFULLY!")
        print("=" * 50)
        print(f"🏷️  Title: {title}")
        print(f"💰 Target: {format_currency(target_amount)}")
        print(f"📅 Duration: {start_date} to {end_date}")
        print("🌟 Your project is now live and ready for supporters!")
        
    except Exception as e:
        print(f"❌ Error saving project: {e}")
        print("Please try creating your project again.")


def view_projects() -> None:
    """
    Display all available projects in a user-friendly format.
    
    Shows project details including owner, title, description,
    target amount, and duration for all projects in the system.
    """
    print("\n🌟 ALL FUNDRAISING PROJECTS")
    print("=" * 60)
    
    if not os.path.exists(PROJECTS_FILE):
        print("📭 No projects found yet!")
        print("💡 Be the first to create an amazing project!")
        return

    try:
        with open(PROJECTS_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
            
        if not lines:
            print("📭 No projects found yet!")
            return
            
        for idx, line in enumerate(lines, start=1):
            try:
                parts = line.strip().split(",", 5)
                if len(parts) < 6:
                    continue
                    
                email, title, details, target, start_date, end_date = parts
                target_amount = float(target)
                
                print(f"\n🏆 PROJECT #{idx}")
                print("-" * 40)
                print(f"👤 Project Owner: {email}")
                print(f"🏷️  Title: {title}")
                print(f"📝 Description: {details}")
                print(f"💰 Fundraising Target: {format_currency(target_amount)}")
                print(f"📅 Campaign Period: {start_date} to {end_date}")
                
                # Calculate project status
                try:
                    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
                    end_dt = datetime.strptime(end_date, "%Y-%m-%d")
                    now = datetime.now()
                    
                    if now.date() < start_dt.date():
                        print("⏳ Status: Coming Soon")
                    elif now.date() > end_dt.date():
                        print("✅ Status: Campaign Ended")
                    else:
                        days_left = (end_dt - now).days
                        print(f"🔥 Status: Active ({days_left} days left)")
                        
                except ValueError:
                    print("📊 Status: Unknown")
                    
            except (ValueError, IndexError) as e:
                print(f"⚠️  Error displaying project #{idx}: Invalid data format")
                continue
                
    except Exception as e:
        print(f"❌ Error reading projects: {e}")


def get_user_projects(user_email: str) -> list:
    """
    Get all projects belonging to a specific user.
    
    Args:
        user_email (str): Email of the user
        
    Returns:
        list: List of tuples (line_index, project_data)
    """
    if not os.path.exists(PROJECTS_FILE):
        return []
        
    try:
        with open(PROJECTS_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
            
        user_projects = []
        for i, line in enumerate(lines):
            if line.strip().startswith(user_email + ","):
                user_projects.append((i, line.strip()))
                
        return user_projects
        
    except Exception as e:
        print(f"❌ Error reading projects: {e}")
        return []


def display_user_projects(user_projects: list) -> None:
    """Display user's projects in a numbered list."""
    print("\n📋 YOUR PROJECTS")
    print("-" * 30)
    
    for idx, (_, project_data) in enumerate(user_projects, start=1):
        try:
            parts = project_data.split(",", 5)
            if len(parts) >= 6:
                _, title, _, target, start_date, end_date = parts
                target_amount = float(target)
                print(f"{idx}. {title}")
                print(f"   💰 Target: {format_currency(target_amount)}")
                print(f"   📅 {start_date} to {end_date}")
        except (ValueError, IndexError):
            print(f"{idx}. [Invalid project data]")


def edit_project(user_email: str) -> None:
    """
    Allow a user to edit their own projects.
    
    Args:
        user_email (str): Email of the authenticated user
        
    Users can modify:
    - Project title and description
    - Fundraising target
    - Project dates
    
    Only the project owner can edit their projects.
    """
    print("\n✏️  EDIT YOUR PROJECT")
    print("=" * 40)
    
    user_projects = get_user_projects(user_email)
    
    if not user_projects:
        print("📭 You don't have any projects to edit yet!")
        print("💡 Create your first project to get started!")
        return
    
    display_user_projects(user_projects)
    
    # Get user selection
    while True:
        try:
            choice = input(f"\nSelect project to edit (1-{len(user_projects)}): ").strip()
            project_index = int(choice) - 1
            
            if 0 <= project_index < len(user_projects):
                break
            else:
                print(f"❌ Please enter a number between 1 and {len(user_projects)}")
                
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Get the selected project
    original_line_index, project_data = user_projects[project_index]
    parts = project_data.split(",", 5)
    
    if len(parts) < 6:
        print("❌ Error: Invalid project data!")
        return
        
    _, old_title, old_details, old_target, old_start, old_end = parts
    
    print(f"\n🔧 Editing: {old_title}")
    print("=" * 40)
    print("💡 Press Enter to keep the current value, or type new value to change it.")
    print()
    
    # Edit title
    while True:
        new_title = input(f"📝 Title [{old_title}]: ").strip()
        if not new_title:
            new_title = old_title
            break
        if len(new_title) < 5:
            print("❌ Title should be at least 5 characters long!")
            continue
        if len(new_title) > 100:
            print("❌ Title is too long!")
            continue
        new_title = clean_text_input(new_title)
        break
    
    # Edit details
    while True:
        new_details = input(f"📄 Description [{old_details}]: ").strip()
        if not new_details:
            new_details = old_details
            break
        if len(new_details) < 20:
            print("❌ Please provide more details (at least 20 characters)!")
            continue
        if len(new_details) > 500:
            print("❌ Description is too long!")
            continue
        new_details = clean_text_input(new_details)
        break
    
    # Edit target
    while True:
        target_input = input(f"💰 Target [{old_target}]: ").strip()
        if not target_input:
            new_target = old_target
            break
        if not is_positive_number(target_input):
            print("❌ Please enter a valid positive number!")
            continue
        new_target_amount = float(target_input)
        if new_target_amount < 100:
            print("❌ Minimum target is 100 EGP!")
            continue
        if new_target_amount > 10000000:
            print("❌ Maximum target is 10,000,000 EGP!")
            continue
        new_target = str(new_target_amount)
        break
    
    # Edit dates
    while True:
        new_start = input(f"🗓️  Start Date [{old_start}]: ").strip()
        if not new_start:
            new_start = old_start
            break
        if not is_valid_date_format(new_start):
            print("❌ Invalid date format! Use YYYY-MM-DD")
            continue
        break
    
    while True:
        new_end = input(f"🗓️  End Date [{old_end}]: ").strip()
        if not new_end:
            new_end = old_end
            break
        if not is_valid_date_format(new_end):
            print("❌ Invalid date format! Use YYYY-MM-DD")
            continue
        if not dates_are_logical(new_start, new_end):
            print("❌ End date must be after start date!")
            continue
        break
    
    # Save changes
    try:
        with open(PROJECTS_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        # Update the specific line
        lines[original_line_index] = f"{user_email},{new_title},{new_details},{new_target},{new_start},{new_end}\n"
        
        with open(PROJECTS_FILE, "w", encoding="utf-8") as file:
            file.writelines(lines)
        
        print("\n✅ PROJECT UPDATED SUCCESSFULLY!")
        print("=" * 40)
        print(f"🏷️  Title: {new_title}")
        print(f"💰 Target: {format_currency(float(new_target))}")
        print(f"📅 Duration: {new_start} to {new_end}")
        
    except Exception as e:
        print(f"❌ Error updating project: {e}")


def delete_project(user_email: str) -> None:
    """
    Allow a user to delete their own projects.
    
    Args:
        user_email (str): Email of the authenticated user
        
    Only the project owner can delete their projects.
    Includes confirmation to prevent accidental deletions.
    """
    print("\n🗑️  DELETE PROJECT")
    print("=" * 30)
    
    user_projects = get_user_projects(user_email)
    
    if not user_projects:
        print("📭 You don't have any projects to delete!")
        return
    
    display_user_projects(user_projects)
    
    # Get user selection
    while True:
        try:
            choice = input(f"\nSelect project to delete (1-{len(user_projects)}): ").strip()
            project_index = int(choice) - 1
            
            if 0 <= project_index < len(user_projects):
                break
            else:
                print(f"❌ Please enter a number between 1 and {len(user_projects)}")
                
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Get project details for confirmation
    original_line_index, project_data = user_projects[project_index]
    parts = project_data.split(",", 5)
    
    if len(parts) >= 2:
        project_title = parts[1]
    else:
        project_title = "Unknown Project"
    
    # Confirmation
    print(f"\n⚠️  CONFIRM DELETION")
    print("=" * 30)
    print(f"You are about to delete: {project_title}")
    print("⚠️  This action cannot be undone!")
    
    while True:
        confirm = input("\nType 'DELETE' to confirm, or 'CANCEL' to abort: ").strip().upper()
        
        if confirm == "DELETE":
            break
        elif confirm == "CANCEL":
            print("✅ Deletion cancelled. Your project is safe!")
            return
        else:
            print("❌ Please type 'DELETE' or 'CANCEL'")
    
    # Delete the project
    try:
        with open(PROJECTS_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        # Remove the specific line
        lines.pop(original_line_index)
        
        with open(PROJECTS_FILE, "w", encoding="utf-8") as file:
            file.writelines(lines)
        
        print(f"\n✅ PROJECT DELETED!")
        print(f"🗑️  '{project_title}' has been removed from the platform.")
        
    except Exception as e:
        print(f"❌ Error deleting project: {e}")


def search_projects_by_date() -> None:
    """
    Search and display projects that are active on a specific date.
    
    Shows all projects where the given date falls between
    the project's start and end dates.
    """
    print("\n🔍 SEARCH PROJECTS BY DATE")
    print("=" * 40)
    
    while True:
        date_input = input("📅 Enter date to search (YYYY-MM-DD): ").strip()
        
        if not date_input:
            print("❌ Date cannot be empty!")
            continue
            
        if not is_valid_date_format(date_input):
            print("❌ Invalid date format! Please use YYYY-MM-DD")
            print("💡 Example: 2025-07-15")
            continue
            
        break
    
    try:
        search_date = datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date!")
        return
    
    print(f"\n🔍 Projects active on {date_input}:")
    print("=" * 50)
    
    if not os.path.exists(PROJECTS_FILE):
        print("📭 No projects found!")
        return
    
    found_projects = 0
    
    try:
        with open(PROJECTS_FILE, "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, 1):
                try:
                    parts = line.strip().split(",", 5)
                    if len(parts) < 6:
                        continue
                        
                    email, title, details, target, start_date, end_date = parts
                    
                    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
                    end_dt = datetime.strptime(end_date, "%Y-%m-%d")
                    
                    # Check if search date falls within project duration
                    if start_dt <= search_date <= end_dt:
                        found_projects += 1
                        target_amount = float(target)
                        
                        print(f"\n🏆 PROJECT #{found_projects}")
                        print("-" * 30)
                        print(f"🏷️  Title: {title}")
                        print(f"👤 Owner: {email}")
                        print(f"📝 Description: {details}")
                        print(f"💰 Target: {format_currency(target_amount)}")
                        print(f"📅 Duration: {start_date} to {end_date}")
                        
                except (ValueError, IndexError):
                    continue
                    
    except Exception as e:
        print(f"❌ Error searching projects: {e}")
        return
    
    if found_projects == 0:
        print("📭 No projects found for this date.")
        print("💡 Try searching for a different date!")
    else:
        print(f"\n✅ Found {found_projects} project(s) active on {date_input}")


def project_menu(user_email: str) -> None:
    """
    Display the project management menu and handle user choices.
    
    Args:
        user_email (str): Email of the authenticated user
        
    This menu provides access to all project-related functionality:
    - Creating new projects
    - Viewing all projects
    - Managing user's own projects
    - Searching projects by date
    """
    while True:
        print(f"\n🏗️  PROJECT MANAGEMENT")
        print("=" * 40)
        print(f"👤 Logged in as: {user_email}")
        print("-" * 40)
        print("1. 🚀 Create New Project")
        print("2. 👀 View All Projects")
        print("3. ✏️  Edit My Projects")
        print("4. 🗑️  Delete My Project")
        print("5. 🔍 Search Projects by Date")
        print("6. 🔙 Back to Main Menu")
        print("-" * 40)
        
        choice = input("Please choose an option (1-6): ").strip()

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
            print("🔙 Returning to main menu...")
            break
            
        else:
            print("❌ Invalid choice! Please select 1-6.")
            
        # Pause before showing menu again
        input("\nPress Enter to continue...")
