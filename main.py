from functions import add_task
from functions import find_task_index
def main():
    incomplete_tasks=[]
    completed_tasks=[]
    print("""
          |---------------------------------------------------|
          |             Welcome to the todo App               |
          |---------------------------------------------------|""")
    while True:
        print("""
                            Command menu
                            
            add [task_name]
            finish [task_name]
            delete [task_name]
            view
            """)
        command_string = input().strip()
        
        parts = command_string.split(" ", 1)
        command_name = parts[0].lower()
        task_name = parts[1] if len(parts) > 1 else ""


        
        if command_name == "add":
            add_task(incomplete_tasks,task_name)
        elif command_name == "finish":
            task_index = find_task_index(incomplete_tasks, task_name)
            
            
if __name__ == "__main__":
    main()
