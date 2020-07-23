
import os

# Open a file
path = "C:\\step161"



fName = 'doc1.txt'

fPath = 'C:\\step161\\'



import sys
import time

path = "C:\\step161"



fileList = os.listdir(fPath)

for file in fileList:
    if file.endswith(".txt"):
        abPath = os.path.join(fPath, file)
        modification_time = os.path.getmtime(abPath)
        print(modification_time,file)
    

