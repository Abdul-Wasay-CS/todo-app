# Task Manager CLI Application

## 📋 Features

This Task Manager CLI application provides the following core functionalities:

### Task Management Functions
- **Add Task** - Add new tasks to the incomplete tasks list
- **Complete Task** - Move tasks from incomplete to completed status
- **Delete Task** - Remove tasks from the incomplete tasks list
- **View Incomplete Tasks** - Display all pending tasks
- **View Completed Tasks** - Display all finished tasks

### Data Persistence
- **File Handling** - Automatically saves and loads tasks from files
- **Incomplete Tasks Storage** - Persistent storage for pending tasks
- **Completed Tasks Storage** - Persistent storage for finished tasks
- **File Integrity Checks** - Validates task files on startup
- 
## 🚀 How to Use

### Running the Application
1. Ensure you have Python installed on your system
2. Run the application from your terminal/command prompt:
   ```bash
   python task_manager.py
   ```

### Available Commands
The application operates using a command-line interface with the following commands:

- **Add a new task**: Follow the prompts to enter your task description
- **Complete a task**: Select a task from the incomplete list to mark as complete
- **Delete a task**: Remove a task from the incomplete list
- **View tasks**: Choose to view either incomplete or completed tasks
- **Exit**: Close the application (tasks are automatically saved)

### Data Storage
- Completed and incomplete tasks are stored in Separte files
- File handling is independant of the type of Operating System being used.

## 🛠 Requirements

- Python 3.x
- No external libraries required (uses only Python standard library)

---
