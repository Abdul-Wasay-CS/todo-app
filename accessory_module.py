def incomplete_task_exists(list, task):
    task_found = False
    for curr_task in list:
        # .lower() to make the search case-insensitive
        if curr_task.lower() == task.lower():
            task_found = True
            break
    return task_found

def find_incomplete_task_index(list,task):
    if incomplete_task_exists(list,task):
        return list.index(task)
    else:
        return -1

def print_list(list):
    print("""
          |---------------------------------------|""")
    for i in list:
        print(f"""
          |%-39s|""" %i)
    print("""
          |---------------------------------------|""")

def print_list(list, heading):
    print(f"""
          |------------%15s------------|"""%heading)
    for i in list:
        print(f"""
            |%-39s|""" %i)
        print("""
            |---------------------------------------|""")