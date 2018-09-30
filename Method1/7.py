from tkinter import *

def ADD():
    name=nEntry.get()
    tel=tEntry.get()
    if (name==""):
        if(tel==""):
            label1=Label(TopFrame,text="Name is empty!", fg='red', font="Calibre 10")
            label1.grid(row=2,column=1)
            label2=Label(TopFrame,text="Telephone is empty!", fg='red', font="Calibre 10")
            label2.grid(row=4,column=1)
    else:
        listbox.insert(END, name+": "+tel)
        
def DEL():
    select=listbox.curselection()
    index=select[0]
    listbox.delete(index)
def export():

    f1=listbox.get(1,END)
    f2=open("Contacts.txt", "w")
    f2.write(str(f1))
    f2.close()
    
def EDIT():
    name=nEntry.get()
    tel=tEntry.get()
    select=listbox.curselection()
    index=select[0]
    listbox.delete(index)  
    listbox.insert(index, name+": "+tel)
    
wn=Tk()
wn.title("Phonebook")
wn.geometry("300x400")
TopFrame=Frame(wn)
TopFrame.grid()
BottomFrame=Frame(wn)
BottomFrame.grid()
ButtonFrame=Frame(wn)
ButtonFrame.grid()
label=Label(TopFrame,text="List of Students:", font="Calibre 16")
label.grid(columnspan=2)

names=Label(TopFrame,text="Name:", font="Calibre 16")
names.grid(row=1,column=0)
nEntry=Entry(TopFrame,width=20)
nEntry.grid(row=1,column=1)

phones=Label(TopFrame,text="Telephone:", font="Calibre 16")
phones.grid(row=3,column=0)
tEntry=Entry(TopFrame,width=20)
tEntry.grid(row=3,column=1)

listbox=Listbox(BottomFrame, selectmode=SINGLE)
listbox.grid()

addButton=Button(ButtonFrame, text='Add',command=ADD)
addButton.grid(row=0,column=0)
deleteButton=Button(ButtonFrame, text='Delete',command=DEL)
deleteButton.grid(row=0,column=1)
editButton=Button(ButtonFrame, text='Edit',command=EDIT)
editButton.grid(row=0,column=3)
expButton=Button(ButtonFrame, text='Export Contacts',command=export)
expButton.grid(columnspan=2)

wn.mainloop()
