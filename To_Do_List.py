to_Do_List = []
run = False
def show_Help():
    print("What task's do you need to do today?")
    print("""Enter 'Exit' when your finished adding tasks.
Enter 'Help' to show these instructions.
Enter 'Tasks' to see list.""")

def add_To_List(new_Task):
    to_Do_List.append(new_Task)
    print("{} has been added to the to-do list. Your list now has {} items".format(new_Task,len(to_Do_List)))

def show_List():
    print("There's no tasks in this list") if len(to_Do_List) == 0 else print("Here's your list")
    for task in to_Do_List:
     print("- " + task)

show_Help()

while run == False:
    new_Task = input("- ").lower()
    if new_Task == "exit":
        run = True
        continue
    elif new_Task == "help":
        show_Help()
        continue
    elif new_Task == "tasks":
        show_List()
        continue
    add_To_List(new_Task)

show_List()
