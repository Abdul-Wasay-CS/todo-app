import accessory_module as ac
import safe_inputs_module as inp
import files_module as files

def main():
    incomplete_tasks=[]
    completed_tasks=[]
    
    files.load_incomplete_tasks(incomplete_tasks)
    files.load_complete_tasks(completed_tasks)
    
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
            view_tasks
            exit
            """)
        command_string = input("Enter your Command:").strip()
        
        # To seperate the command keyword and the task name
        space_index = command_string.find(" ")
        command_name = command_string[0:space_index].lower()
        task_name = command_string[space_index+1:]
        
        if command_name == "add":
            add_task(incomplete_tasks,task_name)
        elif command_name == "finish":
            task_index = ac.find_task_index(incomplete_tasks, completed_tasks, task_name)
            if task_index < 0:
                print("Task Not Found, Completion falied")
                continue
            else:
                finish_task(incomplete_tasks, completed_tasks, task_index)
        elif command_name == "view_tasks":
            view_completed_task(completed_tasks)
            view_pending_task(incomplete_tasks)
        elif command_name == "exit":
            break
        else:
            print("Invalid Command")
        
def add_task(list,task_name):
    list.append(task_name)
def finish_task(incomplete_tasks, finished_tasks, task_index):
    # This function must be only called if the task in question is found in the list
    incomplete_tasks.remove(task_index)
    finished_tasks.append(task_index)
def view_pending_task(incomplete_tasks):
    ac.print_list(incomplete_tasks,"Pending Tasks")
def view_completed_task(completed_tasks):
    ac.print_list(completed_tasks,"Completed Tasks")

main()