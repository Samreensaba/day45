import os,time

os.system("clear")

title = "\033[34mTODO List Management System\033[0m"
toDoList = []



def add():
  time.sleep(2)
  os.system("clear")
  print("\033[36mADD\033[0m")
  print()
  print()
  name = input("WHat do you want to add? ")
  dueDate = input("What is the due date? ")
  priority = input("What is the priority(high/medium/low)? ")
  newList = [name.capitalize(), dueDate, priority.capitalize()]
  toDoList.append(newList)

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

def view():
  print("\033[38mVIEW\033[0m")
  print()
  print()
  viewOption = input("1: View All\n2: View Priority\n> ")
  if viewOption == "1":
    print()
    print("Here is your TODO List")
    print()
    for row in toDoList:
      for item in row:
        print(f"{item: ^10}", end=" | ")
      print()
    print()
  elif viewOption == "2":
    userPriority = input("1: High\n2: Medium\n3: Low\n> ")
    if userPriority == "1":
      userPriority = "High"
      print("High priority List:")
      print()
      printPriority(userPriority)
    elif userPriority == "2":
      userPriority = "Medium"
      print("Mediun priority List:")
      print()
      printPriority(userPriority)
    elif userPriority == "3":
      userPriority = "Low"
      print("Low priority List:")
      print()
      printPriority(userPriority)
    else:
      print("Invali response")
  else:
    print("Invalid response")

def edit():
  print("\033[37mEDIT\033[0m")
  print()
  print()
  findList = input("Which item do you want to edit? ")
  isavailable = False
  for row in toDoList:
      if findList.capitalize() in row:
        isavailable = True
  if isavailable:
        newItem = input("What is the new name?: ")
        newDate = input("New Due Date?: ")
        newPriority = input("What is the new priority?: ")
        toDoList.remove(row)
        newRow = [newItem.capitalize(), newDate, newPriority.capitalize()]
        
        toDoList.append(newRow)
        print()
        print("Changed Sucessfully")
    
  else:
    print(f"\033[32m{findList}\033[0m not found in TODO List")

def remove():
  name = input("What do you want to delete? ")
  isAvailable = False
  for row in toDoList:
    if name in row:
      isAvailable = True
  if isAvailable:
    confirmation = input(f"Are you sure you want to delete {name}?y/n ")
    if confirmation == "y":
      toDoList.remove(row)
      print(f"{name} deleted")
    elif confirmation == "n":
      print(f"{name} not deleted")
    else:
      print("Invalid response")
  else:
    print(f"{name} not found in list")





print(f"{title: ^50}")

while True:
  menu = input("1: ADD\n2: VIEW\n3: EDIT\n4: REMOVE\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  elif menu == "4":
    remove()
  else:
    print("Invalid Option")
  print()
  time.sleep(3)
  os.system("clear")
  print(f"{title: ^50}")