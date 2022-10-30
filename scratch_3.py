from tkinter import *


#definitions
root = Tk()
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
label_2.grid(columnspan=6, row=1, column=0, sticky=E)
entry_1.grid(row=0, column=6)
button_1.grid(columnspan=2, row=7, column=5)
listbox_2.grid(rowspan=6, columnspan=6, row=2, column=0)
scrollbar_1.grid(rowspan=6, row=2, column=4, sticky=N+S)
optionmenu_1.grid(columnspan=3, row=0, column=1)
label_3.grid(row=0, column=0)


root.mainloop()

