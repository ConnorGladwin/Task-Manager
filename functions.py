import datetime

# prints the menu
def Menu(name):
    print("\n--- Menue ---")
    print("Please select one of the following options: ")
    print("r - register new user")
    print("a - add task")
    print("va - view all tasks")
    print("vm - view all my tasks")

    #checks if the user is the admin, if so it prints the admin menu options
    if name == "admin":
        AdminMenu()
    
    print("e - exit\n")

# the admin menu
def AdminMenu():
    print("gr - generate reports")
    print("ds - display statistics")

# allows the user to add a new user to the system
def Register(name, users):
    newUserAdd = False

    # checks to see if the user is the admin
    if name == "admin":

        while newUserAdd == False:
            
            newUser = input("New user name: ")

            # checks that the user does not exist
            if newUser not in users:

                newPass = input("New user password: ")
                newPassCon = input("Confirm password: ")

                # confirms the user password
                if newPass == newPassCon:

                    usersFile = open('user.txt', 'a')   
                    usersFile.write(f"{newUser}, {newPass}")

                    print("New user successfully added!")
                    usersFile.close()
                    newUserAdd = True
                    userRegister += 1
                    break
                else:
                    print("User password does not match password confirmation.")

            else:
                print("User already registered")
                break

    else:
        print("You do not have permission to add new users.\n")

# allows the user to add a new task
def AddTask(taskAdd, today):

    name = input("User name: ")
    task = input("Task title: ")
    taskDesc = input("Task description: ")
    dateT = today
    dueDate = input("Due date: ")
    print("\n")

    task = open('tasks.txt', 'a')
    task.write(f"{name}, {task}, {taskDesc}, {dateT}, {dueDate}, No \n")

    print("New task successfully added.")
    taskAdd += 1
    task.close()

    # calls the 'another' function
    Another()

# checks if the user wants to add another task, if so calls the AddTask function
def Another():
    another = input("Would you like to add another task?")

    if another.lower() == "y":
        AddTask(taskAdd, today)
    else:
        pass

# allows the user to view all tasks assigned to all users
def ViewAll(tUser, tTitle, tasks, dateA, dateD, tComp):
    count = 0

    while True:

        print("----------")
        print(f"Task: {tTitle[count]}")
        print(f"Assigned to: {tUser[count]}")
        print(f"Task description: {tasks[count]}")
        print(f"Date assigned: {dateA[count]}")
        print(f"Due date: {dateD[count]}")
        print(f"Task complete? {tComp[count]}")
        count += 1

        if count >= len(tTitle):
            break

# allows the user to view all of the tasks assigned to them
def ViewMy(name, tUser, tTitle, tasks, dateA, dateD, tComp):
    x = []
    nameCount = tUser.count(name)
    count = 1

    if name in tUser:
            while nameCount >= count:

                taskNum = count - 1

                print(f"Task {count}: {tTitle[taskNum]}")
                print(f"Assigned to: {tUser[taskNum]}")
                print(f"Task description: {tasks[taskNum]}")
                print(f"Date assigned: {dateA[taskNum]}")
                print(f"Due date: {dateD[taskNum]}")
                print(f"Task complete? {tComp[taskNum]}")

                x.append([count, tTitle[taskNum], tUser[taskNum], tasks[taskNum], dateA[taskNum], dateD[taskNum], tComp[taskNum]])
                count += 1

            # calls the edit function
            Edit(x, name)

    else:
        print("You do not have any tasks assigned to you.")

# exits the program
def Exit(users):
    login = False
    print("Thank you for using the TMS. Goodbye.\n")
    exit()

# allows the admin to print statistics based on the number of users and number of tasks
def Stats(admin, tTitle, users):
    if(admin == True):

            taskCount = len(tTitle)
            userCount = len(users)
            
            print(f"Number of tasks: {taskCount}")
            print(f"Number of users: {userCount}")

# I have had a lot of trouble with this function
# I am hoping to get some direction with this function as I can't seem to come up with a way to edit the selected
# task and apply it to the task text file
def Edit(x):

    option = input("Would you like to edit your tasks?: ")

    if option.upper() == "Y":
        print("Whoop")
    else:
        pass

    print("Which task would you like to edit?: ")
    option = input("Option: ")

    for line in x:
        print("This function does not exist")

# generates a report on the tasks file by creating and writing the information to another file
def TaskReport(tUser, tTitle, tasks, dateA, dateD, tComp, today, taskAdd):

    n = 0
    y = 0
    overdue = 0

    taskOver = open("task_overview.txt", "w+")

    for i in range(len(tComp)):

        if tComp[i] == " No\n":
            n += 1
        else:
            y += 1

    for i in range(len(dateD)):
        if today > dateD[i]:
            if tComp[i] == " No\n":
                overdue += 1

    # calculates the percentage value for the incomplete and overdue tasks
    incomplete = (100 * float(n) / float(len(tTitle)))
    over = (100 * float(overdue) / float(len(tTitle)))

    taskOver.write(f"Task Overview for {today}: \n")
    taskOver.write(f"Number of tasks:   {taskAdd}\n")
    taskOver.write(f"Completed tasks:   {y}\n")
    taskOver.write(f"Incomplete tasks:  {n}\n")
    taskOver.write(f"Overdue tasks:     {overdue}\n")
    taskOver.write(f"Incomplete %:      {incomplete : .2f}\n")
    taskOver.write(f"Overdue %:         {over : .2f}\n")
    taskOver.close()

# generates a report on the user file by creating and writing the information to another file
def UserReport(users, tUser, tTitle, tasks, dateA, dateD, tComp, userRegister, taskAdd, today):

    userOver = open("user_overview.txt", "w+")

    # prints the date, the number of users and the number of tasks
    userOver.write(f"User overview for {today}: \n")
    userOver.write(f"Number of users registered:        {userRegister + len(tUser)}\n")
    userOver.write(f"Number of tasks added:             {taskAdd + len(tTitle)}\n\n")

    userCount = (len(users) - 1)
    taskCount = len(tTitle)
    i = 0
    y = 0
    n = 0
    x = []

    while i != userCount:

        y = 0
        n = 0
        x = []
        overdue = 0

        userName = users[i]
        index = users.index(userName)

        for name in tUser:
            if name == userName:
                x.append(f"{tUser}, {tTitle}, {tasks}, {dateA}, {dateD}, {tComp}")

        for line in x:

            if tComp[index] == "Yes":
                y += 1
            elif tComp[index] == "No":
                n += 1

        for j in range(len(dateD)):
            if today > dateD[index]:
                if tComp[index] == " No\n":
                    overdue += 1

        nameCount = tUser.count(userName)
        namePerc = (100 * float(nameCount) / float(taskCount))
        comp = (100 * float(y) / float(taskCount))
        incomp = (100 * float(n) / float(taskCount))
        overdue = (100 * float(overdue) / float(taskCount))

        userOver.write(f"User name:                 {userName}\n")
        userOver.write(f"Number of tasks:           {nameCount}\n")
        userOver.write(f"% of tasks:                {namePerc : .2f}\n")
        userOver.write(f"% of completed tasks:      {comp : .2f}\n")
        userOver.write(f"% of incomplete tasks:     {incomp : .2f}\n")
        userOver.write(f"% of overdue tasks:        {overdue : .2f}\n")
        userOver.write("\n")
        i += 1

    userOver.close()

# prints both reports to the console
def PrintReports():

    # opens both the task and user overview files 
    x = open('task_overview.txt', 'r')
    y = open('user_overview.txt', 'r')

    # runs through both files, printing the information
    for line in x:

        field = line.split("\n")
        print(field)
        print("\n")

    for line in y:

        field = line.split("\n")
        print(field)
        print("\n")
