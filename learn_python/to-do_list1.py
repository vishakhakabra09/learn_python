tasks = []

while True:
    print("\n1 Add Task")
    print("2 Show Tasks")
    print("3 Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        t = input("Enter task: ")
        tasks.append(t)

    elif ch == "2":
        for i in tasks:
            print(i)

    elif ch == "3":
        break

    else:
        print("Wrong choice")