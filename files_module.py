import os

# incomplete task file utility

def save_incomplete_tasks(incomplete_tasks):
    sub_dir = "saved_data"
    file_name = "incomplete_task.txt"
    file_path = os.path.join(sub_dir,file_name)
    check_create_task_file(file_path)
    with open(file_path, "w") as f:
        for task in incomplete_tasks:
            f.write(task,"\n")

def load_incomplete_tasks(incomplete_tasks):
    sub_dir = "saved_data"
    file_name = "incomplete_tasks.txt"
    file_path = os.path.join(sub_dir,file_name)
    check_create_task_file(file_path)
    with open(file_name,"r") as f:
        for line in f:
            incomplete_tasks.append(line.strip())

# completed task files utility

def save_complete_tasks(completed_tasks):
    sub_dir = "saved_data"
    file_name = "completed_task.txt"
    file_path = os.path.join(sub_dir,file_name)
    check_create_task_file(file_path)
    with open(file_path,"w") as f:
        for i in completed_tasks:
            f.write(i,"\n")

def load_complete_tasks(completed_tasks):
    sub_dir = "saved_data"
    file_name = "completed_task.txt"
    file_path = os.path.join(sub_dir,file_name)
    check_create_task_file(file_path)
    with open(file_path,"r"):
        for line in f:
            completed_tasks.append(line.strip())

# general file creation
    
def check_create_task_file(file_path):
    if not(os.path.exists(file_path)):
        with open(file_path,"x") as f:
            pass #do nothing