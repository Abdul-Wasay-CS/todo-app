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

### Utility Functions
- **Input Validation** - Ensures correct data types for all inputs:
  - `get_integer()` - Forces integer input
  - `get_string()` - Handles string input
  - `get_float()` - Forces float input
  - `get_boolean()` - Forces boolean input
- **Task Search** - Find tasks in lists by content
- **Task Indexing** - Locate task positions in lists
- **List Display** - Formatted task listing with headings

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
- Incomplete tasks are stored in `incomplete_tasks.json`
- Completed tasks are stored in `completed_tasks.json`
- Files are created automatically on first run
- All changes are saved automatically when you exit

## 📁 Project Structure

```
task_manager.py          # Main application file
incomplete_tasks.json    # Storage for pending tasks
completed_tasks.json     # Storage for finished tasks
README.md               # This documentation file
```

## 🔧 Technical Details

### Core Data Structures
- **Incomplete Tasks List** - Stores all pending tasks
- **Completed Tasks List** - Stores all finished tasks

### Function Groups
1. **Require Functions** - Core task operations (add, complete, delete, view)
2. **Input Functions** - Validated user input handlers
3. **File Functions** - Persistent storage operations
4. **Utility Functions** - Helper functions for task management

## 📝 Notes

- The application automatically loads your previous tasks on startup
- All changes are saved automatically
- Task lists are displayed in a clean, formatted manner
- Input validation prevents errors from incorrect data entry

## 🛠 Requirements

- Python 3.x
- No external libraries required (uses only Python standard library)

---

*This Task Manager helps you stay organized by keeping track of your pending and completed tasks in a simple, command-line interface.*
