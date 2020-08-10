#
#Python:3.8.3
#
#Author:  Star Erickson
#
#Purpose: To create a script that will use Python 3 and Tkinter module

#           The script will re-create an exact copy of a GUI from the
#           supplied image at the bottom of this page.


import os

import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import os, shutil
import os.path, time


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 250))
        self.master.title('Check files')
        self.master.config(bg='lightgray')

        self.varbox1 = StringVar()
        self.varbox2 = StringVar()


        self.txtbox1 = Entry(self.master,text=self.varbox1 , width=43, font=("Helvetica", 16), fg='black', bg='white')
        self.txtbox1 .grid(row=2, column=4,padx=(30,0), pady=(60,0))

        self.txtbox2 = Entry(self.master,text=self.varbox2, width=43, font=("Helvetica", 16), fg='black', bg='white')
        self.txtbox2.grid(row=3, column=4,padx=(30,0), pady=(20,0))

        self.btnBrowseone = Button(self.master, text="Browse...", width=15, height=1, command=self.browseone)
        self.btnBrowseone.grid(row=2, column=1,padx=(10,0), pady=(60,0), sticky=NW)

        self.btnBrowsetwo = Button(self.master, text="Browse...", width=15, height=1, command=self.browsetwo)
        self.btnBrowsetwo.grid(row=3, column=1,padx=(10,0), pady=(20,0), sticky=SW)

        
        self.btnFiles = Button(self.master, text="Check for files...", width=15, height=2, command=self.files)
        self.btnFiles.grid(row=4, column=1,padx=(10,0), pady=(20,0), sticky=SW)

        
        self.btnClose = Button(self.master, text="Close Program", width=15, height=2, command=self.close)
        self.btnClose.grid(row=4, column=4,padx=(0,0), pady=(20,0), sticky=SE)

    def browseone(self):
        path = filedialog.askdirectory()
        print(self.txtbox1.insert(INSERT,path))
        

    def browsetwo(self):
        path = filedialog.askdirectory()
        print(self.txtbox2.insert(INSERT,path))
       

    def files(self):
        source_dir = self.txtbox1.get()
        destination_dir = self.txtbox2.get()
       # absolute_path = [] Levi taught me about this for an upcoming expanded assignment
        for filename in os.listdir(source_dir):
            if filename.endswith('.txt'):
                Current_path = os.path.join(source_dir, filename)
               # absolute_path.append(Current_path) Continued from Levi 
                shutil.move(Current_path, destination_dir)

                
       

    def close(self):
        self.master.destroy()


#path = 'C:/Users/guesttta/Documents/GitHub/Python/File Transfer assignment/Source Folder/'
#copyto= 'C:/Users/guesttta/Documents/GitHub/Python/File Transfer assignment/Destination Folder/'



def Update(path, copyto):
    files = os.listdir(path)
    files.sort()
    for f in files:
        src = os.path.join(path, f) #path of source
        dst = os.path.join(copyto, f) #path of destination
        if os.path.exists(dst):
            if os.stat(src).st_mtime > os.stat(dst).st_mtime:
                shutil.copy(src,dst)
                print('Updated: ' + f)
        else:
            print('Copied: ' + f)
            shutil.copy(src,dst) #copying from source to destination
        

        


       





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
