from tkinter import *
from tkinter import filedialog
def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

# ws = Tk()
# ws.title("PythonGuides")
# ws.geometry("400x450")
# ws['bg']='#fb0'
#
# txtarea = Text(ws, width=40, height=20)
# txtarea.pack(pady=20)
#
# pathh = Entry(ws)
# pathh.pack(side=LEFT, expand=True, fill=X, padx=20)



# Button(
#     ws,
#     text="Open File",
#     command=openFile
# ).pack(side=RIGHT, expand=True, fill=X, padx=20)
#
#
# ws.mainloop()

# creating tkinter window
root = Tk()
root.title('Menu Demonstration')
root.geometry("400x450")
root['bg']='#fb0'
txtarea = Text(root, width=40, height=20)
txtarea.pack(pady=20)

pathh = Entry(root)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = openFile)
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
mainloop()