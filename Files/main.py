#Importing -------
import tkinter
from customtkinter import *
import os
from tkinter import messagebox as msg
# -----------------

#SetStyling--------
set_appearance_mode("dark")  
set_default_color_theme("blue")  
#------------------

#Config------------
app = CTk() 
app.title("ArduCMD")
app.resizable(False, False)
app.geometry("300x200")
Logo = tkinter.PhotoImage(file="./Images/logo.png")
app.iconphoto(False,Logo)
#-------------------

#Deifne/SetVars-----
Path = StringVar()
PJname = StringVar()
with open("./Logging/path.txt","r") as file:
  FR = file.read()
  if FR == "": Path.set(os.getcwd())
  else: Path.set(FR)  
PJname.set("MyProject")
#--------------------

#Functions-----------
def ECFF():
   f = open("./Snippets/Functions.txt","r")
   ff = f.read()
   Editor = tkinter.Toplevel(app)
   Editor.geometry("200x200")
   Editor.title("Editor")
   def SaveFile():
     file = open("./Snippets/Functions.txt","w")
     file.write(f"{Edit.get(1.0, tkinter.END)}")
     print(Edit.get(1.0, tkinter.END))
     Editor.destroy()
    Edit = tkinter.Text(Editor)
   Editor.configure(bg="#212325")
################  
def EMIF():
   f = open("./Snippets/ArduSnippet.txt","r")
   ff = f.read()
   Editor = tkinter.Toplevel(app)
   Editor.geometry("200x200")
   Editor.title("Editor")
   def SaveFile():
     file = open("./Snippets/ArduSnippet.txt","w")
     file.write(f"{Edit.get(1.0, tkinter.END)}")
     print(Edit.get(1.0, tkinter.END))
     Editor.destroy()
   Edit = tkinter.Text(Editor)
   Edit.insert("1.0",f"{ff}")
   Btn = tkinter.Button(Editor,text="Save",command=SaveFile)
   Edit.pack()
   Btn.place(x=25, y=10, anchor=tkinter.CENTER) 
   Editor.configure(bg="#212325")  
################
def CRT():
  path_ = Path.get()
  project_ = PJname.get()
  pj = project_.replace(" ","")
  if os.path.isdir(f"{path_}/{pj}") == False:
    os.makedirs(f"{path_}/{pj}/")
    os.mknod(f"{path_}/{pj}/{pj}.ino")
    os.mknod(f"{path_}/{pj}/Functions.h")
    with open(f"./Snippets/Functions.txt") as f:
        with open(f"{path_}/{pj}/Functions.h","w")  as file:
          file.write(f"{f.read()}")
    with open(f"./Snippets/ArduSnippet.txt") as f:
        with open(f"{path_}/{pj}/{pj}.ino","w") as file:
          file.write(f"{f.read()}")
    msg.showinfo("Project Created",f"Project Created as '{pj}'")
    with open("./Logging/path.txt","w") as file:￼…￼
  else: msg.showerror("Can't create the project","dictionary already exists. Please choose another name")
################
#--------------------

#CreatingWidgets-----
bl = CTkLabel(master=app, text=" ")
PJlb = CTkLabel(master=app, text="Project Name:")
PJen = CTkEntry(master=app,textvariable=PJname)
EMbtn = CTkButton(master=app,text="Edit MyFile.ino", command = EMIF)
ECFbtn = CTkButton(master=app, text="Edit Functions.h",command=ECFF)
pathlb = CTkLabel(master=app,text="Save path:")
path = CTkEntry(master=app,textvariable=Path)
CRbtn=CTkButton(master=app,text="Create",width=200,command=CRT)
#--------------------

#GriddingWidgts------
bl.grid (row= 1,column=1)
PJlb.grid(row=3,column=1)
PJen.grid(row=3,column=2)
EMbtn.grid(row=4,column=1)
ECFbtn.grid(row=4,column=2)
path.grid(row=5,column=2)
pathlb.grid(row=5,column=1)
CRbtn.place(x=50,y=150)
#--------------------

app.mainloop()
