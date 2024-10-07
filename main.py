import os, time

title = "\033[34mTODO LIST MANAGEMENT SYSTEM\033[0m"

print(f"{title: ^60}")
print()
toDoList = []



def prettyprint():
  print()
  print("Here is your todo list")
  for row in toDoList:
    for item in row:
      print(f"{item: ^10}", end=" | ")
    print()
  print()

def printPriority(userPriority):
  print()
  priorityList = []
  
  for row in toDoList:
    if userPriority in row:
      priorityList.append(row)
      
  for list in priorityList:
    for item in list:
      print(f"{item: ^10}", end=" | ")
    print()
  print()




while True:
  print("""  1: ADD
  2: VIEW
  3: EDIT
  4: REMOVE""")
  menu = input("> ")
  if menu.lower() == "add" or menu == "1":
    time.sleep(1)
    os.system("clear")
    print("ADD")
    print()
    print()
    name = input("What to add?: ")
    dueDate = input("When is it due?: ")
    priority = input("Priority(High/Medium/Low)?: ")

    newList = [name, dueDate, priority.lower()]
    toDoList.append(newList)
    
    print()
    print()
    print("Added Sucessfully")
  elif menu.lower() == "remove" or menu == "4":
    name = input("Wwhat do you want to remove from the to do list?: ")
    
    for row in toDoList:
      if name in row:
        confirm = input(f"Are you sure you want to remove {name} from the list?y/n: ")
        if confirm == "y":
          toDoList.remove(row)
          print(f"{name} removed from the list.")
        else:
          print(f"{name} not removed.")
      else:
        print(f"{name} was not in the list")
  elif menu.lower() == "view" or menu == "2":
    print("VIEW")
    print()
    print()
    print("""1: View All
          2: View Priority""")
    view = input("> ")
    if view == "2":
      askPriority = input("Which priority?(High/Medium/Low): ")
      if askPriority.lower() == "high":
        print("High Priority List")
        printPriority("high")
      elif askPriority.lower() == "medium":
        print("medium Priority List")
        printPriority("medium")
      elif askPriority.lower() == "low":
        print("Low Priority List")
        printPriority("low")
      else:
        print("Invalid Response")  
      
    else:
      prettyprint()
      
    #time.sleep(5)
    #os.system("clear")
    
  elif menu.lower() == "edit" or menu == "3":
    editItem = input("Which item do you want to edit? ")
    for row in toDoList:
      if editItem in row:
        newItem = input("What is the new name?")
        newDate = input("New Due Date?: ")
        newPriority = input("What is the new priority? ")
        toDoList.remove(row)
        newRow = [newItem, newDate, newPriority]
        
        toDoList.append(newRow)
      
  else:
    print("Invalid input, try again.")

  time.sleep(3)
  os.system("clear")
  print(f"{title: ^60}")
  