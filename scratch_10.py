import tkinter as tk
import os
from natsort import natsorted
from tkinter import *
from tkinter import filedialog
from tkinter import font
from markdown2 import Markdown
from tkhtmlview import HTMLLabel
def clickEvent(*args):
    #insert code that will execute here
    for i in listbox.curselection():
        listbox1.delete(0,tk.END)
        #folder=r"C:\\Users\\SifayathAhmedF\\"+listbox.get(i)
        folder=ROOT_PATH+listbox.get(i)
        print("Folder : " + folder)
        os.chdir(folder)
        files = natsorted(os.listdir(os.getcwd()))
        listbox1.delete(0,tk.END)
        print(files)
        a="333333"
        for file in files:
            listbox1.insert(files.index(file),file)
            #t=F6F6F6+files.index(file)
            a = hex(int(a, 16) + int('1FF', 16)+int('FF00', 16) + int('02',16))
            print(a.replace('0x','').upper().rjust(6,'0'))
            listbox1.itemconfig("end", bg = '#'+a.replace('0x','').upper().rjust(6,'0') if (files.index(file) < 500 and int(a,16)<int('FFFFFF',16)) else "green")
        listbox1.update()
        T.delete('1.0', tk.END)
        listbox1.bind('<<ListboxSelect>>', clickEvent1)

def clickEvent1(*args):
    #insert code that will execute here
    T.delete('1.0', tk.END)
    for i in listbox1.curselection():
        file = listbox1.get(i)
        if(file):
            print(file)
            with open(file,'r') as f:
                data=f.read()
                T.insert(tk.END, data)
    #T.edit_modified(0)
    md2html = Markdown()
    outputbox.set_html(md2html.convert(T.get("1.0" , END)))
    markdownText = T.get("1.0", END)
    html = md2html.convert(markdownText)
    outputbox.set_html(html)

def outputboxrefresh(*args):
    md2html = Markdown()
    #outputbox.set_html(md2html.convert(T.get("1.0" , END)))
    markdownText = T.get("1.0", END)
    html = md2html.convert(markdownText)
    outputbox.set_html(html)

def saveFile():
    tf = filedialog.asksaveasfile(
        mode='w',
        title ="Save file",
        defaultextension=".txt"
    )
    #tf.config(mode="w")
    #pathh.insert(END, tf)
    data = str(T.get(1.0, END))
    tf.write(data)
    tf.close()

root = tk.Tk()
ws= Frame(root)
# specify size of window
root.geometry("250x170")
# Create a listbox
#listbox = tk.Listbox(root, height=40, selectbackground='#00A619',background='#F6F6F6', activestyle='none', exportselection=False,font=('Calibri',20))##, selectmode='MULTIPLE')
#listbox1 = tk.Listbox(root, height=40, selectbackground='Pink', background='#F6F6F6', activestyle='none', exportselection=False, font=('Calibri',20))##, selectmode='MULTIPLE')

#listbox = tk.Listbox(root, height=40, selectbackground='#B1C9E8',background='#F6F6F6', activestyle='none', exportselection=False,
#                     font=font.Font(family='Serif',weight='bold',size=10))##, selectmode='MULTIPLE')
#listbox = tk.Listbox(root, height=40, selectbackground='#B1C9E8',background='#F6F6F6', activestyle='none', exportselection=False,
#                     font=font.Font(family='MS Sans Serif',weight='bold',size=10))##, selectmode='MULTIPLE')
login_btn = PhotoImage(file = r"C:\Users\SifayathAhmedF\Pictures\Composite Shot 1-00;00;05;14.png")
listbox = tk.Listbox(root, height=40, selectbackground='#B1C9E8',background='#F6F6F6', activestyle='none', exportselection=False,
                     font=font.Font(family='Calibri',weight='bold',size=18))##, selectmode='MULTIPLE')
listbox1 = tk.Listbox(root, height=40, selectbackground='#59CBE8', background='#F6F6F6', activestyle='none', exportselection=False, font=('Calibri',18))##, selectmode='MULTIPLE')
ROOT_PATH = r"C:\\Users\\SifayathAhmedF\\"
#os.chdir("C:\\Users\\SifayathAhmedF")
os.chdir(ROOT_PATH)
directories = natsorted(os.listdir(os.getcwd()),key=str.lower)
print(directories)

#[listbox.insert(0,x) for x in directories]
for x in directories:
    print(x)
    listbox.insert(directories.index(x),x)

listbox.bind('<<ListboxSelect>>', clickEvent)
# Create text widget and specify size.
T = tk.Text(root, height = 100, width = 70,background='#F6F6F6')
outputbox = HTMLLabel(
    root,height = 100, width="100",background="beige", html="<h1>Welcome</h1>")

# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None) #openFile)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

# display Menu
root.config(menu = menubar)

listbox.grid(row=2, column=0,sticky = tk.NW,rowspan=2,columnspan=1, pady = 2)
listbox1.grid(row=2,column=1,sticky = tk.NW, pady = 2)
T.grid(row=2,column=2)
outputbox.grid(row=2,column=3)
T.bind('<Key>',outputboxrefresh)
#outputbox.fit_height()
ws.grid(row=0,column=2)
var_1 = StringVar(root)
label_1 = Label(root, text="Search:")
label_2 = Label(root, text="Subject specific programs below")
label_3 = Label(root, text="Subject:")
entry_1 = Entry(root) #this should search through the strings listed under listbox_2 configs
button_1 = Button(root, text="Install")
scrollbar_1 = Scrollbar(root)
listbox_2 = Listbox(root, yscrollcommand=scrollbar_1.set)
optionmenu_1 = OptionMenu(root, var_1, "Computing", "Engineering", "Physics")
string_1 = StringVar(root, name="Google Chrome")
string_2 = StringVar(root, name="Thunderbird")
string_3 = StringVar(root, name="Adobe Reader X")
string_4 = StringVar(root, name="WinRAR")
string_5 = StringVar(root, name="OpenOffice")
string_6 = StringVar(root, name="Program 1")
string_7 = StringVar(root, name="Program 2")
string_8 = StringVar(root, name="Program 3")
string_9 = StringVar(root, name="Program 4")
string_10 = StringVar(root, name="Program 5")
string_11 = StringVar(root, name="Program 6")

#configuration
root.title("Network Installation")
listbox_2.insert(1, string_1)
listbox_2.insert(2, string_2)
listbox_2.insert(3, string_3)
listbox_2.insert(4, string_4)
listbox_2.insert(5, string_5)
listbox_2.insert(6, string_6)
listbox_2.insert(7, string_7)
listbox_2.insert(8, string_8)
listbox_2.insert(9, string_9)
listbox_2.insert(10, string_10)
listbox_2.insert(11, string_11)
optionmenu_1.config(width=15)
scrollbar_1.config(command=listbox_2.yview)
#grid additions
label_1.grid(row=0, column=5)
label_2.grid( row=1, column=0, columnspan=6, sticky=E)
label_3.grid(row=0, column=0)
entry_1.grid(row=0, column=6)
button_1.grid(row=7, column=5, columnspan=2,)
listbox_2.grid(row=2, column=0, rowspan=6, columnspan=6)
scrollbar_1.grid(row=2, column=4,rowspan=6,  sticky=N+S)
optionmenu_1.grid( row=0, column=1, columnspan=3)


Button(
    ws,
    text="Save File",
    command=saveFile
).pack(side=RIGHT, expand=True, fill=X, padx=20)

tk.mainloop()

