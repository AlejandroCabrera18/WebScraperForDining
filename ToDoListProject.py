"""
To do list Project
By: Alejandro Cabrera
Purpose: To create a simple to do list application, to warm up my python skills
"""
def displayList(List):
    i = 0
    for i in range(len(List)):
        print(str(i+1)+": "+List[i])

def __main__():
    '''main function'''
    try:
        toDoList = open("todolist.txt","r")
    except:
        toDoList = open("todolist.txt","x")
    List = toDoList.readlines()
    displayList(List)
    toDoList.close()
    num = 1
    response = ""
    while(response != "done"):
        response = input("If you would like to add a task to the To-Do List, type in the task. However, if you would like to remove a task, type the corresponding number of the task to remove it. Or if you are done, type 'done'   ")
        try:
            response = int(response)
            if response > -1:
                List.pop(response-1)
                displayList(List)
        except:
            if (response != "done"):
                List.append(response)
                displayList(List)
    toDoList = open("todolist.txt","w")
    i = 0
    for i in range(len(List)):
        toDoList.write(List[i])
        toDoList.write("\n")
    
__main__()
