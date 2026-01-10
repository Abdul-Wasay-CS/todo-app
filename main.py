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
        
        # To seperate the command keyword and the task name
        space_index = command_string.find(" ")
        command_name = command_string[space_index].lower()
        task_name = command_string[space_index:]
        
        if command_name == "add":
            add_task(incomplete_tasks,task_name)
        elif command_name == "finish":
            task_index = find_task_index(incomplete_tasks, task_name)
            
            
if __name__ == "__main__":
    main()