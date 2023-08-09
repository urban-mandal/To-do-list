import sys, viewtasks, Taskstorage, time
#time.sleep is used to make everything not so rushed
def complete_a_task():
    print("""Hi!!!
please write the task you want to mark as completed
if you want to view the tasks write 1 than press enter reversing is not yet an option""")

    ct = sys.stdin.readline()
    ct = ct.strip()
    cremove = ct#in the remove func \n is added to the item but because
    ct = ct + "\n"#we want to append \n here we need to copy ct and the put the cremove var in to remove func

    if ct == "1":
        viewtasks.viewtasks()
    else:
        #check if the task exists
        cfile = open("storage", "r")
        clines = cfile.readlines()
        cfile.close()

        if ct in clines:
            Taskstorage.removetask(cremove)
            ctfile = open("completedtasks", "a")
            ctfile.writelines(ct)
            ctfile.close()
            time.sleep()
        else:
            print("""the task doesnt exist, make sure that you have written it correctly
if you still want to mark it as complete please write it again if not type 5""")
            anwser = sys.stdin.readline()

            if anwser == "5":
                print("youll be rideirected to the menu")
                time.sleep(1)
            else:
                complete_a_task()
                time.sleep(1)

            
