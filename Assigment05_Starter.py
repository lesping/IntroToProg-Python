# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Lespinoza,08.04.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

print ("""
--------------------------
THIS IS A DAILY TO DO LIST
--------------------------
""")
input ("Please press 'Enter' key to start!")

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
task_str = "" # Add a new task
priority_str = "" # Add the priority of task

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
try:
    objFile = open(objFile, "r") # read the data we keep in the text file
    for row in objFile: # to loop through the rows of data
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        print (dicRow["Task"] + "|" + dicRow["Priority"])
        lstTable.append(dicRow) # managing the data in the memory
        print (lstTable)
    objFile.close()
except:
    print("File not found")
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("Your current data is: ")
        print("--------------------------")
        for row in lstTable: # go through the list table
            print(row["Task"] + "|" + row["Priority"])  # the user can see the current data collected
            print(row) # another simple way to show the current data
            print("--------------------------")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        print ("Type in a Task and Priority for your table list")
        task_str = input("Enter an Task: ") # add new tasks
        priority_str = input("Enter a Priority: ") # add its priorities
        dicRow = {"Task":task_str, "Priority":priority_str} # row of data
        lstTable.append (dicRow) # each dicRow is part of a table data
        print (lstTable) # to see the progress of the table list
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strData = input("Task to remove:")
        for row in lstTable: # go through the list table
            if row["Task"].lower() == strData.lower():
                lstTable.remove(row) # delete the row from the table
                print (strData, "was removed")
            else:
                print (strData, "not found")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        while (True):
            strChoice = input("Save? ('y/n'): ")
            if (strChoice.lower() == "y"):
                objFile = open("ToDoList.txt", "w")  # writing into the .txt file
                for row in lstTable:
                    objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n") # save the new data
                objFile.close()
                print ("Got it!")
                break
            elif (strChoice.lower() == "n"):
                print ("Your data was not saved")
                break
            else:
                print ("please choose only 'y' or 'n'")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("please choose only 'y' or 'n'")
        strChoice = input("Exit? ('y/n'): ") # make a choice
        if (strChoice.lower() == "y"):
            break  # and Exit the program
        elif (strChoice.lower() == "n"):
            continue # continue in the program
    else:
        print ("please choose only '1 to 5' ")