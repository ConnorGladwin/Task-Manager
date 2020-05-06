# imports the os module. this is purely used so that it will run on my system  
# import os

# imports the date module
import datetime
from datetime import date
import functions

#opens the two files that will be used in the program
usersFile = open('user.txt', 'r+')
tasksFile = open('tasks.txt', 'r+')

# defines the arrays that the program will use when splitting the contents of the file
users = []
passwords = []

tUser = []
tTitle = []
tasks = []
dateA = []
dateD = []
tComp = []

# defines variables that will be used in the program
login = False
taskCount = 0
userCount = 0
log = False
admin = False
taskAdd = 0
userRegister = 0
today = date.today().strftime('%b %d %Y')

# splits the information in the files and appends them to the arrays
for line in usersFile:
    field = line.split(",")

    userName = field[0]
    password = field[1]

    users.append(userName)
    passwords.append(password)

for line in tasksFile:
    field = line.split(",")
    count = 1

    user = field[0]
    taskT = field[1]
    task = field[2]
    dateAssgin = field[3]
    dueDate = field[4]
    taskComp = field[5]

    tUser.append(user)
    tTitle.append(taskT)
    tasks.append(task)
    dateA.append(dateAssgin)
    dateD.append(dueDate)
    tComp.append(taskComp)

# begins the login sequence of the program
while(login == False):

    # allows the user to input their user name and password
    name = input("User name: ")
    passW = input("Password: ")

    # checks if the users name is in the list
    if name in users:

        # defines the position of the users name in the user name array
        index = users.index(name)

        # checks if the input password matches the password in the indexed position
        if(passW in passwords[index]):
            print("Login successful \n")        
            login = True

        else:
            print("Password incorrect!")

    else:
        print("Username incorrect!")

# begins the main body of the program
while(login == True):

    if(log == False):
        print(f"Welcome back {name}!")
        print(today)
    
    log = True

    # checks if the user is the admin
    if(name == "admin"):
        admin = True

    functions.Menu(name)
    option = input("Option: ")
    print("\n")

    # allows the user to register a new user 
    if(option == "r"):
        functions.Register(name, users)
        
    # allows the user to add a new task
    elif(option == "a"):
        functions.AddTask(taskAdd, today)

    # allows the user to check all tasks
    elif(option == "va"):

        functions.ViewAll(tUser, tTitle, tasks, dateA, dateD, tComp)

    # allows the user to check all tasks assigned to them
    elif(option == "vm"):

        functions.ViewMy(name, tUser, tTitle, tasks, dateA, dateD, tComp)

    # exits the program
    elif(option == "e"):
        functions.Exit(users)
    
    # allows the admin to check how many tasks and how many users there are
    elif(option == "ds"):
        functions.Stats(admin, tTitle, users)

    # allows the admin to generate and print a report
    elif option == "gr":

        functions.TaskReport(tUser, tTitle, tasks, dateA, dateD, tComp, today, taskAdd)
        functions.UserReport(users, tUser, tTitle, tasks, dateA, dateD, tComp, userRegister, taskAdd, today)

        option = input("Display reports? (y/n): ")

        if option == "y":
            functions.TaskReport(tUser, tTitle, tasks, dateA, dateD, tComp, today, taskAdd)
            functions.UserReport(users, tUser, tTitle, tasks, dateA, dateD, tComp, userRegister, taskAdd, today)
            functions.PrintReports()
        else:
            pass
        
    else:
        print(f"Option {option} does not exist. Please select from the list of available options.\n")

# closes the files used in the program
usersFile.close()
tasksFile.close()
