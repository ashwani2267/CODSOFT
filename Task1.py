def task():
    tasks = [] #empty list
    print("----To Do List----")

    total_task = int(input("how many task want to bs added=")) #5
    for i in range(1,total_task+1): #6
        task_name = input(f"enter task{i}=") #enter task 1=
        tasks.append(task_name)

    print(f"today's task are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))
        if operation == 1:
            add = input("Enter task you want to add=")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task that you want to update=")
            if updated_val in tasks:
                upd = input("enter new task=")
                ind = tasks.index(updated_val)
                tasks[ind] = upd
                print(f"Updated task {upd}....")

        elif operation == 3:
            del_val = input("Enter task that you want to delete=")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted....")
        elif operation == 4:
            print(f"Total tasks = {tasks}")
        elif operation == 5:
            print("Closing the program.....")
            break
        else:
            print("Invalid Input")
task()