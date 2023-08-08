import addtasks, sys, removetask, viewtasks, Taskstorage
#in each file we use a diffrent letter for input so it make every thing more clear

#func that displays the menu basically ui
def displaymenu():
    print("Hi! Welcome to your to do list")
    
    #the menu will repeat it self untile the user quits
    while True:
        print("""1: add a task    2: remove a task, 3: view tasks
4:check completed tasks 5: quit to do list
please enter the number of a thing you want to do than press enter""")
        #gets the input and based on the input performs the task
        while True:
            try:
                a = int(sys.stdin.readline()) #int
                break
            except ValueError:
                print("buddy you have to enter a number!!")
        if a == 1:# add tasks func is called
            addtasks.addtasks()
        elif a == 2:# remove tasks func is called
            removetask.removingtasks()
        elif a == 3:# view tasks is called
            viewtasks.viewtasks()
        elif a == 4:# check completed tasks from file completed tasks
            pass
        elif a == 5:# quits the to do list
            print("You have quit the to do list")
            break
        
        
if __name__ == "__main__":
    displaymenu()