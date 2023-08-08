import Taskstorage, sys
def addtasks():
    #we tell the user to enter the task he wants to add and we store the input
    print("""Please write the the task you want to add.
In case you dont want to add anything press 5 and than enter""")
          

    b = sys.stdin.readline()
    b = b.strip()

    if b == "5":
        print("we will redirect you to the menu")
    else:
        Taskstorage.taskstorage(b)
        print("the tasks has been stored to remove or view the task youll have to do that in the menu")