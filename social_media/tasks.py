print("- - - - To-do List - - - - -")
print()
print("* * * * * * * * * * * * * * * *")
print()

print("1. Add task")
print("2. View task")
print("3. Mark done")
print("4. Delete task")
print("5. View updated tasks")
print("6. Exit.")
print()
print()

tot_num_task = 0
tot_tasks = []

while True:
    choice = int(input("Enter your choice(1/2/3/4/5/6): "))

    if choice == 1:
        num_task = int(input("How many tasks: "))
        for num_task in range(1, num_task + 1):
            print()
            t = input(f"Task {num_task}: ")
            tot_tasks.append(t)
        print("Tasks successfully added.")
        tot_num_task = len(tot_tasks)

    elif choice == 2:
        if len(tot_tasks) == 0:
            print("No tasks today")
        else:
            for index, task in enumerate(tot_tasks, start=1):
                print(index, task)

    elif choice == 3:
        if len(tot_tasks) == 0:
            print("No tasks today")
        else:
            done_task = int(input("Enter task no. that you completed: "))
            if done_task >= 1 and done_task <= len(tot_tasks):
                comp_task = tot_tasks[done_task - 1]
                print("DONE -", tot_tasks[done_task - 1])
                tot_tasks.remove(tot_tasks[done_task - 1])
                tot_tasks.insert(done_task - 1, f"DONE - {comp_task}")

    elif choice == 4:
        delete_task = int(input("Enter task no. to be deleted: "))
        dtask = tot_tasks[delete_task - 1]
        tot_tasks.remove(dtask)
        print("Task successfully deleted.")

    elif choice == 5:
        usr_resp = input("Would you like to view updated task list? (y/n): ")
        if usr_resp.lower() == "y":
            print(tot_tasks)

    elif choice == 6:
        print("Thank you for using this program :)")
        break
