from tkinter import *

def About():
    messagebox.showinfo(title="About", message="This is an About category")
    return

def Exit():
    mExit=messagebox.askyesno(title="Quit", message="Are you sure?")
    if mExit>0:
        wn.destroy()
        return

def delete():
    select=listbox.curselection()
    index=select[0]
    listbox.delete(index)

def show(event):
    select=listbox.curselection()
    index=select[0]
    name2=listbox.get(index)
    name.set(name2)

def deleteAll():
    listbox.delete(0,END)

wn=Tk()
menubar=Menu(wn)
filemenu=Menu(menubar, tearoff=0) # 1st -- -- -- line
filemenu.add_command(label="About", command=About)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
wn.config(menu=menubar)

frame=Frame(wn)
frame.pack()

scrollbar=Scrollbar(frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

listbox=Listbox(frame,selectmode=SINGLE,yscrollcommand=scrollbar.set) #SINGLE, EXTENDED(with CTRL), MULTIPLE
listbox.pack(side=LEFT)

scrollbar.config(command=listbox)

listbox.insert(END,"It's a list")
for  i in ['one','two','three','four','five','six','seven','eight','nine','ten']:
    listbox.insert(END,i)

deletebutton=Button(wn,text='Delete', command=delete)
deletebutton.pack()

deleteall=Button(wn,text='Delete All', command=deleteAll)
deleteall.pack()

name=StringVar()
label=Label(wn, textvariable=name)
label.pack()

listbox.bind("<<ListboxSelect>>", show)

temp_list=list(listbox.get(0,END))
print(temp_list)
print(listbox.size())

wn.mainloop()
