tasks = []

sample_task ={
    "id" : 0,
    "title" : "",
    "completed" : False
}


def add_task():
    description = input(" TO DO : ")
    what_time = input(" what time do you specify for this task: ")
    print(" self study")
    print(" school work")
    print(" exercise")
    print(" entertainment")
    print(" outing")
    print(" Friends meetup")


    category= input(" Select from above: ")
    task_id = len(tasks) + 1



    task = { "id": task_id,
             "description": description,
             "what_time": what_time,
             "category": category,
             "completed": False
            }


    tasks.append(task)
    print(f"{description} is added to task with ID {task_id}!\n")
    


def view_task():
    if len(tasks) == 0:
        print(" No tasks recorded yet")
        return
    else:
        for task in tasks:
            if task['completed'] == True:
              print(f"{task['id']} | {task['description']} | {task['what_time']} | {task['category']}  done")

            else:
                 print(f"{task['id']} | {task['description']} | {task['what_time']} | {task['category']}   not done")


def task_mark():
    if len(tasks) == 0:
        print(" No tasks recorded yet")
        return
        
    view_task()

    target_id = int(input("Enter task ID to be marked as completed: "))
    
    found = False
    for task in tasks:
        if task["id"] == target_id :
            task["completed"] = True
            print(" TASK COMPLETED")
            found = True
            break      
    if not found:
            print("Task ID not found")

def delete_task():
    if len(tasks) == 0:
        print("No task recorded yet!!!")
        return
    
    view_task()
    target_ide = input(" Task id to delete the task: ")

    for task in tasks:
        if task["id"] == target_ide:
            task["completed"] = True
            print(" TASK COMPLETED!!!")
            found = True
            break

    if not found:
            print(" TASK ID NOT FOUND!!!")





while True:
    print("===== Task Tracker =====")

    print("----- MENU ----")
    print(" 01. Add task")
    print(" 02. View task")
    print(" 03. Mark task as completed")
    print(" 04. Delete task")
    print(" 05. Exit")

    choice = input(" Select from the above menu and type only number (i.e: 1, 2, etc): ").strip()
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        task_mark()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print(" EXIT")
        break
    else:
        print(" INVALID OPTION")
 
