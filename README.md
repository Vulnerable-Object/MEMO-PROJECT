# 🌟 Crowdfunding Console Application

A comprehensive console-based crowdfunding platform built in Python that allows users to create, manage, and browse fundraising campaigns.

## 📋 Features

### 🔐 Authentication System
- **User Registration**: Complete registration with validation
  - First Name & Last Name
  - Email validation with format checking
  - Password strength validation (minimum 6 characters)
  - Password confirmation
  - Egyptian mobile phone validation (01XXXXXXXXX format)
  - Duplicate email prevention

- **User Login**: Secure authentication system
  - Email and password verification
  - User session management
  - Profile viewing capabilities

### 📊 Project Management
- **Create Projects**: Launch fundraising campaigns
  - Project title and detailed description
  - Target amount in Egyptian Pounds (EGP)
  - Campaign duration with start/end dates
  - Date validation (start date cannot be in the past)
  - Automatic date range validation

- **View All Projects**: Browse all available campaigns
  - Real-time status indicators (Active/Ended)
  - Formatted currency display
  - Project owner information
  - Campaign duration details

- **Edit Projects**: Modify your own campaigns
  - Update title, description, and target amount
  - Modify campaign dates
  - Input validation with current value preservation
  - Only project owners can edit their campaigns

- **Delete Projects**: Remove campaigns with confirmation
  - Secure deletion with "DELETE" confirmation
  - Only project owners can delete their campaigns
  - Warning messages for irreversible actions

- **Search by Date**: Find active projects on specific dates
  - Date-based project filtering
  - Shows only campaigns active on the specified date
  - Comprehensive search results display

## 🏗️ Architecture

### Modular Design
The application follows a clean modular architecture:

```
crowdfunding-app/
├── main.py          # Main application entry point
├── auth.py          # Authentication and user management
├── project.py       # Project management functionality
├── utils.py         # Utility functions and validation
├── users.txt        # User data storage
├── projects.txt     # Project data storage
└── README.md        # Documentation
```

### Key Components

#### 📁 `main.py`
- Application entry point and main menu
- User navigation and error handling
- Welcome banner and about information
- Keyboard interrupt handling

#### 🔐 `auth.py`
- User registration and login functionality
- Email and phone validation
- Password strength checking
- User profile management
- File-based user storage

#### 📊 `project.py`
- Project class definition with full CRUD operations
- Campaign creation, editing, and deletion
- Project search and filtering
- Date validation and status checking
- Enhanced user interface with emojis and formatting

#### 🛠️ `utils.py`
- Email format validation
- Egyptian phone number validation
- Date format validation and parsing
- Currency formatting utilities
- Generic input validation functions

## 📋 Requirements

- Python 3.7+
- No external dependencies required (uses only standard library)

## 🚀 Installation & Usage

1. **Clone or download the application files**
2. **Ensure all files are in the same directory**
3. **Run the application**:
   ```bash
   python main.py
   ```

## 📱 Egyptian Phone Number Validation

The application validates Egyptian mobile numbers with the following format:
- Must start with `01`
- Second digit must be `0`, `1`, `2`, or `5`
- Followed by exactly 8 digits
- Examples: `01012345678`, `01198765432`, `01555517867`

## 📅 Date Format

All dates must be entered in `YYYY-MM-DD` format:
- Example: `2025-12-31`
- Start date must be before end date
- Start date cannot be in the past

## 💾 Data Storage

The application uses simple text files for data persistence:

### `users.txt` Format:
```
FirstName,LastName,email@example.com,password,01234567890
```

### `projects.txt` Format:
```
owner@email.com,Project Title,Project Details,50000.0,2025-01-01,2025-12-31
```

## 🎨 User Interface Features

- **Colorful Emojis**: Enhanced visual experience with relevant emojis
- **Formatted Output**: Clean, professional-looking console output
- **Progress Indicators**: Clear status indicators for projects
- **Error Messages**: Descriptive error messages with helpful guidance
- **Confirmation Dialogs**: Safety confirmations for destructive actions
- **Currency Formatting**: Professional currency display (e.g., "50,000.00 EGP")

## 🔧 Type Hints & Documentation

The application follows Python best practices:
- **Type Hints**: Full type annotation for all functions
- **Docstrings**: Comprehensive documentation for all modules and functions
- **Error Handling**: Robust error handling with user-friendly messages
- **Input Validation**: Comprehensive input validation and sanitization

## 🛡️ Security Features

- **Input Sanitization**: All user inputs are validated and sanitized
- **Email Uniqueness**: Prevents duplicate email registrations
- **Password Validation**: Minimum password length requirements
- **Data Integrity**: Robust file handling with error recovery
- **User Isolation**: Users can only modify their own projects

## 🎯 Usage Examples

### Registration Example:
```
First Name: Ahmed
Last Name: Mohamed
Email: ahmed.mohamed@gmail.com
Password: mypassword123
Confirm Password: mypassword123
Mobile Phone: 01012345678
```

### Project Creation Example:
```
Project Title: Help Local School
Project Details: Fundraising to buy computers for our local school
Target Amount (EGP): 25000
Start Date (YYYY-MM-DD): 2025-01-15
End Date (YYYY-MM-DD): 2025-06-15
```

## 🐛 Error Handling

The application includes comprehensive error handling:
- File I/O errors with graceful recovery
- Invalid input format detection
- Network interruption handling (Ctrl+C)
- Data corruption protection
- User-friendly error messages

## 🤝 Contributing

This project follows academic requirements and demonstrates:
- Modular programming principles
- Clean code practices
- Comprehensive documentation
- Type safety with hints
- Robust error handling
- User experience design

## 📄 License

This is an educational project created for academic purposes.

---

**Made with ❤️ for the crowdfunding community**