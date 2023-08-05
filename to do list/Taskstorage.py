#code that stores all tasks inputed in to a file

def taskstorage(a):
    storage = open("storage.txt", "a")
    a = a + "\n"
    storage.write(a)
    storage.close()