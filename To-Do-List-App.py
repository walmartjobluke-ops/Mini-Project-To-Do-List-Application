"""
To-Do List Application
A command-line interface for managing tasks with features to add, view, 
mark complete, and delete tasks. Includes comprehensive error handling 
and input validation.
"""

# Global list to store tasks
tasks = []

def display_menu():
    
#Display the main menu options to the user.
    
    print("\n" + "=" * 40)
    print("Welcome to the To-Do List App!")
    print("=" * 40)
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")
    print("=" * 40)

def add_task():
    
#Add a new task to the to-do list, default status is 'Incomplete', and includes error handling for empty input.
    
    try:
        task_title = input("\nEnter the task title: ").strip()
        
        if not task_title:
            print("Error: Task title cannot be empty!")
            return False
        
        task = {
            "title": task_title,
            "status": "Incomplete"
        }
        tasks.append(task)
        print(f"✓ Task '{task_title}' added successfully!")
        return True
    
    except Exception as e:
        print(f"Error adding task: {e}")
        return False
    finally:
        pass


def view_tasks():
    
#Display all tasks with their titles and statuses and shows a message if the list is empty.

    try:
        if not tasks:
            print("\nNo tasks in the list. Add one to get started!")
            return True
        
        print("\n" + "-" * 50)
        print("Your Tasks:")
        print("-" * 50)
        
        for index, task in enumerate(tasks, 1):
            status_indicator = "✓" if task["status"] == "Complete" else "○"
            print(f"{index}. [{status_indicator}] {task['title']} - {task['status']}")
        
        print("-" * 50)
        return True
    
    except Exception as e:
        print(f"Error viewing tasks: {e}")
        return False
    finally:
        pass


def mark_task_complete():

#Mark a task as complete by its index.
#Includes input validation for task selection.

    try:
        if not tasks:
            print("\nNo tasks to mark as complete!")
            return False
        
        view_tasks()
        
        task_index_str = input("\nEnter the task number to mark as complete: ").strip()
        
        try:
            task_index = int(task_index_str) - 1
        except ValueError:
            print("Error: Please enter a valid number!")
            return False
        
        if task_index < 0 or task_index >= len(tasks):
            print("Error: Invalid task number!")
            return False
        
        tasks[task_index]["status"] = "Complete"
        print(f"✓ Task '{tasks[task_index]['title']}' marked as complete!")
        return True
    
    except Exception as e:
        print(f"Error marking task complete: {e}")
        return False
    finally:
        pass


def delete_task():
    
#Delete a task from the list by its index.
#Includes input validation for task selection.
    
    try:
        if not tasks:
            print("\nNo tasks to delete!")
            return False
        
        view_tasks()
        
        task_index_str = input("\nEnter the task number to delete: ").strip()
        
        try:
            task_index = int(task_index_str) - 1
        except ValueError:
            print("Error: Please enter a valid number!")
            return False
        
        if task_index < 0 or task_index >= len(tasks):
            print("Error: Invalid task number!")
            return False
        
        deleted_task = tasks.pop(task_index)
        print(f"✓ Task '{deleted_task['title']}' deleted successfully!")
        return True
    
    except Exception as e:
        print(f"Error deleting task: {e}")
        return False
    finally:
        pass


def get_user_choice():
    """
    Get and validate the user's menu choice.
    
    Returns:
        str: The user's menu choice (1-5) or None if invalid.
    """
    try:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice not in ['1', '2', '3', '4', '5']:
            print("Error: Please enter a number between 1 and 5!")
            return None
        
        return choice
    
    except Exception as e:
        print(f"Error getting user choice: {e}")
        return None
    finally:
        pass


def main():
    """
    Main function to run the To-Do List Application.
    Implements the main loop and routes user input to appropriate functions.
    """
    try:
        print("\n" + "=" * 40)
        print("To-Do List Application Started!")
        print("=" * 40)
        
        while True:
            try:
                display_menu()
                choice = get_user_choice()
                
                if choice is None:
                    continue
                
                if choice == '1':
                    add_task()
                elif choice == '2':
                    view_tasks()
                elif choice == '3':
                    mark_task_complete()
                elif choice == '4':
                    delete_task()
                elif choice == '5':
                    print("\nThank you for using To-Do List App! Goodbye!")
                    break
            
            except KeyboardInterrupt:
                print("\n\nApplication interrupted by user.")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                print("Please try again.")
    
    finally:
        print("Application closed.")


if __name__ == "__main__":
    main()
