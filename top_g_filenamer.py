#!/usr/bin/env python
import os

list_of_files = os.listdir()
for i in list_of_files:
    if i.endswith('.pdf'):
        newname = i.replace(" ","_")
        os.rename(i, newname)
print(i)
