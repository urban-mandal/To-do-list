import Taskstorage, time
#time.sleep is used to make everything not so rushed
def viewtasks():
    vlines2 = Taskstorage.viewthetasks()#opens the file reads it returns whatever is in it
    alltasks = ""
    #string so that we dont print a list with for loop we append all vlines2 contents to the string
    for i in vlines2:
        i = i.strip()
        alltasks = alltasks + ", " + i 
    print(f"here are all your tasks {alltasks}")
    print("youll be now returned to the menu")
    time.sleep(1)

def view_completed_tasks():
    vcfile = open("completedtasks", "r")
    vclines = vcfile.readlines()
    vcfile.close()

    for i in vclines:
        i = i.strip()
        print(f"{i},")
    time.sleep(2)
    print("youll now see the menu")
    time.sleep(1)
    
