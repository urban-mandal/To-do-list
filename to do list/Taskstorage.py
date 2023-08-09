#code that stores all tasks inputed in to a file

def taskstorage(a):
    storage = open("storage", "a")
    a = a + "\n" #we add \n to tell the program that thats the end of the line
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