# Mini-Project-To-Do-List-Application

A fully functional, command-line To-Do List Application built with Python. This project demonstrates core Python programming concepts including functions, error handling, user input validation, and data management.

## Features

- **Add Tasks**: Create new tasks with a default "Incomplete" status
- **View Tasks**: Display all tasks with their titles and statuses in a formatted list
- **Mark Complete**: Mark tasks as "Complete" with full input validation
- **Delete Tasks**: Remove tasks from the list with validation
- **Input Validation**: Graceful handling of invalid user input
- **Error Handling**: Comprehensive try-except-finally blocks for robust error management
- **User-Friendly Interface**: Clean CLI with formatted menus and status indicators

## How to Run

1. Navigate to the project directory:
   ```bash
   cd Mini-Project-To-Do-List-Application
   ```

2. Run the application:
   ```bash
   python To-Do-List-App.py
   ```

3. Follow the on-screen menu to manage your tasks

## Menu Options

1. **Add a task** - Enter a task title to add it to your list
2. **View tasks** - Display all tasks with their current status
3. **Mark a task as complete** - Select a task number to mark it as complete
4. **Delete a task** - Remove a task from the list by selecting its number
5. **Quit** - Exit the application

## Technical Implementation

### Code Organization
- Modular design with separate functions for each feature
- Clear function names with comprehensive docstrings
- Organized error handling with try-except-finally blocks

### Data Structure
- Tasks stored as dictionaries with "title" and "status" fields
- Global list maintains all tasks during the session

### Error Handling
- Empty input validation
- Index range checking
- Type validation for numeric input
- Exception handling for unexpected errors
- Keyboard interrupt handling (Ctrl+C)

### Key Functions
- `display_menu()` - Shows the menu interface
- `add_task()` - Adds new tasks to the list
- `view_tasks()` - Displays all tasks with formatting
- `mark_task_complete()` - Updates task status
- `delete_task()` - Removes tasks from the list
- `get_user_choice()` - Validates user menu selection
- `main()` - Main application loop

## 💡 Usage Examples

### Adding a Task
- Type `add_task()`
- Enter the task title: Buy groceries
- Task 'Buy groceries' added successfully!


### Viewing Tasks
- Type `view_tasks()`
Your Tasks:
1. [○] Buy groceries - Incomplete
2. [✓] Complete project - Complete
3. [○] Call mom - Incomplete


### Marking a Task Complete
- Type `mark_task_complete()`
Enter the task number to mark as complete: 1
✓ Task 'Buy groceries' marked as complete!


## Technologies Used
- Python 3.x
- Built-in modules: `collections` (implicitly through list operations)
- Standard I/O with `input()` and `print()`

## Learning Outcomes

This project demonstrates:
-  Functions and modularity
-  Error handling (try-except-finally)
-  Input validation and user interaction
-  Data structures (lists and dictionaries)
-  Control flow (loops and conditionals)
-  String formatting
-  Code documentation with docstrings

## Edge Cases Handled
- Empty task lists
- Invalid menu selections
- Non-numeric task number input
- Out-of-range task indices
- Empty task titles
- Keyboard interrupts (Ctrl+C)

## Notes
- Tasks are stored in memory and will be lost when the application closes
- For persistent storage, consider adding file I/O or database integration as a future enhancement

## Version
- Version 1.0 - Initial release with core functionality

---
**GitHub:** [Mini-Project-To-Do-List-Application](https://github.com/walmartjobluke-ops/Mini-Project-To-Do-List-Application/blob/main/To-Do-List-App.py)

**Created:** February 12th, 2026
