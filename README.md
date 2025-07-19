# 🌟 Crowdfunding Platform

A simple yet powerful command-line crowdfunding application that allows users to create, manage, and discover fundraising projects. Built with Python, this platform enables people to bring their ideas to life and support causes they care about.

## 🎯 What This Project Does

This crowdfunding platform is like a simplified version of Kickstarter or GoFundMe, but runs in your terminal. Here's what it offers:

### 🔐 User Management
- **User Registration**: Create accounts with email validation and Egyptian phone number support
- **Secure Login**: Authenticate users to access their personal project dashboard
- **Data Persistence**: All user information is safely stored in text files

### 🚀 Project Management
- **Create Projects**: Launch fundraising campaigns with detailed descriptions and target amounts
- **Browse Projects**: Discover all available projects with status indicators (Active, Coming Soon, Ended)
- **Edit Projects**: Modify your own projects anytime before they end
- **Delete Projects**: Remove projects with confirmation to prevent accidents
- **Search by Date**: Find projects that were active on specific dates

### 🎨 User Experience Features
- **Colorful Interface**: Emoji-rich interface that's fun and easy to navigate
- **Input Validation**: Comprehensive validation for all user inputs
- **Error Handling**: Friendly error messages that guide users to correct issues
- **Currency Formatting**: Professional display of amounts in Egyptian Pounds (EGP)
- **Date Validation**: Smart date handling with logical constraints

## 🏗️ Project Structure

```
crowdfunding-platform/
├── main.py          # Application entry point and main menu
├── auth.py          # User registration and authentication
├── project.py       # Project management functionality
├── utils.py         # Helper functions and validation
├── users.txt        # User data storage (auto-created)
├── projects.txt     # Project data storage (auto-created)
└── README.md        # This documentation file
```

### 📁 File Descriptions

- **`main.py`**: The heart of the application - handles the main menu and user navigation
- **`auth.py`**: Manages user accounts, registration, and login functionality
- **`project.py`**: Core project management - create, view, edit, delete, and search projects
- **`utils.py`**: Utility functions for validation, formatting, and data cleaning
- **`users.txt`**: Simple database file storing user information (firstname,lastname,email,password,phone)
- **`projects.txt`**: Simple database file storing project data (email,title,details,target,start_date,end_date)

## 🚀 How to Run the Application

### Prerequisites
- Python 3.7 or higher installed on your system
- A terminal or command prompt
- Basic familiarity with command-line interfaces

### Quick Start

1. **Navigate to the project directory**:
   ```bash
   cd /path/to/crowdfunding-platform
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Follow the on-screen prompts**:
   - Choose option 1 to register as a new user
   - Choose option 2 to login with existing credentials
   - Choose option 3 to exit the application

### First Time Setup

When you run the application for the first time:

1. **Register a new account**:
   - Provide your first and last name
   - Enter a valid email address
   - Create a secure password (minimum 6 characters)
   - Enter your Egyptian phone number (format: 01XXXXXXXXX)

2. **Login to your account**:
   - Enter your registered email and password
   - Access the project management dashboard

3. **Create your first project**:
   - Provide a compelling project title
   - Write a detailed description (minimum 20 characters)
   - Set your fundraising target in Egyptian Pounds
   - Choose start and end dates for your campaign

## 🎮 User Guide

### 🏠 Main Menu Options

When you start the application, you'll see three main options:

1. **📝 Register as New User**: Create a new account
2. **🔐 Login to Your Account**: Access existing account
3. **👋 Exit Application**: Close the program

### 🏗️ Project Management Dashboard

After logging in, you'll have access to:

1. **🚀 Create New Project**: Launch a new fundraising campaign
2. **👀 View All Projects**: Browse all available projects on the platform
3. **✏️ Edit My Projects**: Modify your existing projects
4. **🗑️ Delete My Project**: Remove projects with confirmation
5. **🔍 Search Projects by Date**: Find projects active on specific dates
6. **🔙 Back to Main Menu**: Return to the main application menu

### 📝 Creating a Project

When creating a project, you'll need to provide:

- **Project Title**: A catchy name for your project (5-100 characters)
- **Description**: Detailed explanation of your project (20-500 characters)
- **Fundraising Target**: Amount you want to raise (100 - 10,000,000 EGP)
- **Start Date**: When your campaign begins (YYYY-MM-DD format)
- **End Date**: When your campaign ends (must be after start date, max 365 days duration)

### 🔍 Project Status Indicators

Projects display different status indicators:

- **⏳ Coming Soon**: Project hasn't started yet
- **🔥 Active (X days left)**: Currently running campaign
- **✅ Campaign Ended**: Project has finished

## 📊 Data Storage

The application uses simple text files for data storage:

### Users Data Format
```
firstname,lastname,email,password,phone
John,Doe,john.doe@example.com,secure123,01012345678
```

### Projects Data Format
```
email,title,details,target_amount,start_date,end_date
john.doe@example.com,Help Gaza,A fundraising campaign for Gaza,100000,2025-07-01,2025-08-01
```

## 🛡️ Security Features

- **Email Validation**: Ensures proper email format
- **Phone Validation**: Validates Egyptian mobile numbers (01XXXXXXXXX)
- **Input Sanitization**: Cleans and validates all user inputs
- **Data Integrity**: Comprehensive error handling and data validation
- **User Isolation**: Users can only edit/delete their own projects

## 🔧 Technical Requirements

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.7 or higher
- **Memory**: Minimal (< 50MB)
- **Storage**: Minimal (< 1MB for application + data files)

### Python Dependencies
The application uses only Python standard library modules:
- `os` - File system operations
- `re` - Regular expressions for validation
- `datetime` - Date handling and validation

No external packages need to be installed!

## 🚀 Deployment Guide

### Local Deployment

1. **Download the project files**:
   ```bash
   # If using git
   git clone <repository-url>
   
   # Or download and extract the files manually
   ```

2. **Ensure Python is installed**:
   ```bash
   python --version
   # Should show Python 3.7 or higher
   ```

3. **Run the application**:
   ```bash
   cd crowdfunding-platform
   python main.py
   ```

### Server Deployment

For running on a server or remote machine:

1. **Upload files to server**:
   ```bash
   scp -r crowdfunding-platform/ user@server:/path/to/destination/
   ```

2. **Connect to server**:
   ```bash
   ssh user@server
   cd /path/to/destination/crowdfunding-platform
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

### Creating a Launcher Script

Create a simple launcher script (`start.sh` on Linux/Mac or `start.bat` on Windows):

**Linux/Mac (start.sh)**:
```bash
#!/bin/bash
cd /path/to/crowdfunding-platform
python main.py
```

**Windows (start.bat)**:
```batch
@echo off
cd /d C:\path\to\crowdfunding-platform
python main.py
pause
```

Make it executable:
```bash
chmod +x start.sh  # Linux/Mac only
```

## 🐛 Troubleshooting

### Common Issues and Solutions

**Problem**: "Python is not recognized as an internal or external command"
- **Solution**: Install Python or add it to your system PATH

**Problem**: "No module named 'utils'"
- **Solution**: Make sure you're running the command from the project directory

**Problem**: "Permission denied" when creating files
- **Solution**: Ensure you have write permissions in the project directory

**Problem**: Application crashes when entering invalid data
- **Solution**: The application has comprehensive validation, but if you encounter crashes, please report the specific input that caused the issue

### Data Recovery

If data files get corrupted:

1. **Backup existing files** (if partially readable):
   ```bash
   cp users.txt users_backup.txt
   cp projects.txt projects_backup.txt
   ```

2. **Create new empty files**:
   ```bash
   touch users.txt
   touch projects.txt
   ```

3. **Manually restore data** from backups if needed

## 🤝 Contributing

This project is designed to be educational and easy to understand. If you want to contribute:

1. **Code Style**: Follow the existing pattern of clear documentation and human-readable code
2. **Testing**: Test all new features thoroughly
3. **Documentation**: Update this README if you add new features

## 📝 License

This project is created for educational purposes. Feel free to use, modify, and distribute as needed.

## 🆘 Support

If you need help with the application:

1. **Check this README** for common solutions
2. **Review the code comments** - they explain how everything works
3. **Test with simple inputs** first to ensure basic functionality works

## 🎉 Acknowledgments

This crowdfunding platform was created to demonstrate:
- Clean, readable Python code
- User-friendly command-line interfaces  
- Proper data validation and error handling
- File-based data persistence
- Modular code organization

---

**Happy Fundraising! 🌟**

*Remember: Every great project starts with a single step. Your ideas matter, and this platform is here to help bring them to life!*