import datetime
#code that stores all tasks inputed in to a file

def taskstorage(a):
    todays_date = str(datetime.date.today())
    #we get todays date so that the we can append it to the task
    #thats being add so the user knows when he added the task
    storage = open("storage", "a")
    a = a + ":\t" + todays_date + "\n" #we add \n to tell the program that thats the end of the line
    storage.write(a)
    storage.close()

def removetask(b):#we use b so that everything is more clear
    file = open("storage", "r")
    lines = file.readlines()
    file.close()
    b = b + "\n"
    if b in lines:
        lines.remove(b)
    print(lines, b)

    filefixed = open("storage", "w")#w since it overwrites anything that hase existed in the file
    filefixed.writelines(lines)
    filefixed.close()

def viewthetasks():
    vtasks = open("storage", "r")
    vlines = vtasks.readlines()
    vtasks.close()
    return vlines