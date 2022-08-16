#!/usr/bin/env python
import os

print("Add or remove underscores from file names")
file_extension = input("What type of files do you want to replace? Enter file extension:")

n = 5
while n<6:

    print('Enter 1 to add underscores.\n')

    print('Enter 2 to remove underscores.\n')

    print('Enter 3 to stop program. \n')

    choice = int(input('Enter your choice:'))

    if (choice == 1):

        list_of_files = os.listdir()
        for i in list_of_files:
                if i.endswith(file_extension):
                    newname = i.replace(" ","_")
                    os.rename(i, newname)
        print(i)

    elif (choice == 2):

        list_of_files = os.listdir()
        for i in list_of_files:
                if i.endswith(file_extension):
                    newname = i.replace("_"," ")
                    os.rename(i, newname)
        print(i)

    elif (choice == 3):
        break

    else:
        print('Invalid choice')
