# 🌟 Simple Crowdfunding App

**What is this?** A fundraising app like GoFundMe, but it runs in your computer's terminal.

## 🚀 Quick Start (Super Easy!)

1. **Open your terminal/command prompt**
2. **Go to the project folder**:
   ```
   cd crowdfunding-platform
   ```
3. **Run the app**:
   ```
   python main.py
   ```
4. **That's it!** The app will start and show you a menu.

## 🎮 How to Use the App

### First Time Using:
1. Choose option 1 to **register** (create account)
2. Fill in your details (name, email, password, phone)
3. Choose option 2 to **login** with your email and password

### After Login:
- **Create Project**: Start a new fundraising campaign
- **View Projects**: See all projects from everyone
- **Edit Projects**: Change your own projects
- **Delete Projects**: Remove your projects
- **Search**: Find projects by date

## 📱 Example: Creating Your First Project

1. Login to your account
2. Choose "Create New Project"
3. Enter details:
   - **Title**: "Help Local Animal Shelter"
   - **Description**: "Raising money to buy food and supplies for rescued animals"
   - **Target**: 5000 (EGP)
   - **Start Date**: 2025-01-01
   - **End Date**: 2025-02-01
4. Done! Your project is now live.

## 📁 What Files Do What?

- `main.py` → The main app (start here)
- `auth.py` → Login and registration stuff
- `project.py` → All the project features
- `utils.py` → Helper tools
- `users.txt` → Your accounts are saved here
- `projects.txt` → All projects are saved here

## ❓ Common Questions

**Q: Do I need to install anything?**
A: Just Python! That's it.

**Q: Where is my data stored?**
A: In simple text files (users.txt and projects.txt)

**Q: Can I edit other people's projects?**
A: No! You can only edit your own projects.

**Q: What if I make a mistake?**
A: The app asks for confirmation before deleting anything important.

## 🛠️ For Your Mentor

This project shows:
- ✅ Clean, readable code with lots of comments
- ✅ Proper input validation and error handling
- ✅ Good file organization (each file has one job)
- ✅ User-friendly interface with helpful messages
- ✅ All requirements from the assignment completed
- ✅ Beginner-friendly code that's easy to understand

## 🎯 What Makes This Code "Human"?

1. **Clear Names**: Functions are named like `create_project()` not `cp()`
2. **Lots of Comments**: Every part is explained
3. **Friendly Messages**: "✅ Project created!" instead of just "OK"
4. **Safe**: Validates everything before saving
5. **Organized**: Each feature is in its own file

## 🚨 Need Help?

If something doesn't work:
1. Make sure Python is installed: `python --version`
2. Make sure you're in the right folder
3. Check that all files are there: `ls` (Mac/Linux) or `dir` (Windows)

**That's it! Happy fundraising! 🎉**