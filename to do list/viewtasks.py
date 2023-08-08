import Taskstorage

def viewtasks():
    vlines2 = Taskstorage.viewthetasks()
    alltasks = ""

    for i in vlines2:
        i = i.strip()
        alltasks = alltasks + ", " + i 
    print(f"here are all your tasks {alltasks}")
    