from tkinter import *
import os
wn=Tk()
wn.geometry('500x500')
wn.title("Notepad")


def about():
    messagebox.showinfo("about","Python Lesson!")
def undo():
    textPad.event_generate("<<Undo>>")
def copy():
    textPad.event_generate("<<Copy>>")
def paste():
    textPad.event_generate("<<Paste>>")
def cut():
    textPad.event_generate("<<Cut>>")
def redo():
    textPad.event_generate("<<Redo>>")
   
def select_all():
    textPad.tag_add("sel",1.0,END)

def new_file():
    global filename
    wn.title("Untitled.txt")
    filename=None
    textPad.delete(1.0,END)
def open_file():
    global filename
    filename=filedialog.askopenfilename()
    wn.title(os.path.basename(filename))
    file=open(filename,"r",encoding="utf-8")
    textPad.delete(1.0,END)
    textPad.insert(1.0,file.read())
    file.close()

def save():
    try:
        global filename
        file=open(filename,"w",encoding="utf-8")
        content=textPad.get(1.0,END)
        file.write(content)
        file.close()
    except:
        save_as()
def save_as():
    f=filedialog.asksaveasfilename()
    file=open(f,"w",encoding="utf-8")
    content=textPad.get(1.0,END)
    file.write(content)
    file.close()
def exit_nt():
    if messagebox.askokcancel("Exit","Do you really want to exit?"):
        wn.destroy()
        exit()


def search_for(n,textPad,t2,e):
    textPad.tag_remove('match','1.0',END)
    count=0
    if n:
        pos=1.0
        while True:
            pos=textPad.search(n,pos,stopindex=END)
            if not pos:
                break
            lastpos='%s +%dc' % (pos,len(n))
            textPad.tag_add('match',pos,lastpos)
            count+=1
            pos=lastpos
        textPad.tag_config('match',foreground="red",background="yellow")
    e.focus_set()
    t2.title('% matches found')

def on_find():
    t2=Toplevel(wn)
    t2.title("Find")
    t2.geometry("265x65+200+250")
    label=Label(t2,text="Find All")
    label.grid(row=0,column=0)
    v=StringVar()
    e=Entry(t2,width=25,textvariable=v)
    e.grid(row=0,column=1)
   # e.focus_set()
    b=Button(t2,text="Find All",command=lambda:search_for(v.get,textPad,t2,e))
    b.grid(row=0,column=2)
    def close_search():
        textPad.tag_remove('match','1.0',END)
        t2.destroy()
    t2.protocol('WN_DELETE_WINDOW',close_search)


        

        
    
    
    
    


    

menubar=Menu(wn)
#images
newicon = PhotoImage(file='icons/new_file.gif')
openicon = PhotoImage(file='icons/open_file.gif')
saveicon = PhotoImage(file='icons/Save.gif')
cuticon = PhotoImage(file='icons/Cut.gif')
copyicon = PhotoImage(file='icons/Copy.gif')
pasteicon = PhotoImage(file='icons/Paste.gif')
undoicon = PhotoImage(file='icons/Undo.gif')
redoicon = PhotoImage(file='icons/Redo.gif')




#file
filemenu = Menu(menubar, tearoff=0 ) 
filemenu.add_command(label="New", accelerator='Ctrl+N', compound=LEFT, image=newicon, underline=0,command=new_file  )
filemenu.add_command(label="Open", accelerator='Ctrl+O', compound=LEFT, image=openicon, underline=0,command=open_file)
filemenu.add_command(label="Save", accelerator='Ctrl+S',compound=LEFT, image=saveicon,underline=0,command=save)
filemenu.add_command(label="Save as",accelerator='Shift+Ctrl+S',command=save_as)
filemenu.add_separator()        
filemenu.add_command(label="Exit", accelerator='Alt+F4',command=exit_nt) 
menubar.add_cascade(label="File", menu=filemenu) 

#Edit
editmenu = Menu(menubar)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label="Undo", accelerator = "Ctrl+Z", compound=LEFT,image=undoicon,command=undo)
editmenu.add_command(label="Redo", accelerator = "Ctrl+Y", compound=LEFT,image=redoicon,command=redo)
editmenu.add_command(label="Copy", accelerator = "Ctrl+C", compound=LEFT,image=copyicon,command=copy)
editmenu.add_command(label="Cut", accelerator = "Ctrl+X", compound=LEFT,image=cuticon,command=cut)
editmenu.add_command(label="Paste", accelerator = "Ctrl+V", compound=LEFT,image=pasteicon,command=paste)
editmenu.add_command(label="Select All", accelerator = "Ctrl+A",command=select_all)
editmenu.add_command(label="Find", accelerator = "Ctrl+F",command=on_find)

#View
viewmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu)
showIn=IntVar()
showIn.set(1)
viewmenu.add_checkbutton(label="Show Info",variable=showIn)

showIn2=IntVar()
showIn2.set(1)
viewmenu.add_checkbutton(label="Show Line",variable=showIn2)

showIn3=IntVar()
showIn3.set(0)
viewmenu.add_checkbutton(label="Highlight",variable=showIn3)

thememenu=Menu(menubar,tearoff=0)
viewmenu.add_cascade(label="Themes",menu=thememenu)

dictionary={
    '1 color':'white',
    '2 color':'blue',
    '3 color':'green',
    '4 color':'red'
    }

themechoice=StringVar()
themechoice.set('1 Default white')

for k in sorted(dictionary):
    thememenu.add_radiobutton(label=k,variable=themechoice)
#About
aboutmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="About",menu=aboutmenu)
aboutmenu.add_command(label="About Us",command=about)

#blue frame with buttons
frame=Frame(wn,height=25,bg="light sea green")
frame.pack(fill=X)

#textpad
textPad=Text(wn,undo=True)
textPad.pack(expand=YES,fill=BOTH)

#scroll
scroll=Scrollbar(textPad)
textPad.configure(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT,fill=Y)

buttonOpen=Button(frame,image=newicon,command=new_file)
buttonOpen.grid(row=0,column=0)
b2=Button(frame, compound=LEFT, image=saveicon, command=save)
b2.grid(row=0,column=1)
b3=Button(frame, compound=LEFT, image=cuticon, command=Cut)
b3.grid(row=0,column=2)
b4=Button(frame, compound=LEFT, image=copyicon, command=Copy)
b4.grid(row=0,column=3)
b5=Button(frame, compound=LEFT, image=pasteicon, command=Paste)
b5.grid(row=0,column=4)
b6=Button(frame, compound=LEFT, image=undoicon, command=Undo)
b6.grid(row=0,column=5)
b7=Button(frame, compound=LEFT, image=redoicon, command=Redo)
b7.grid(row=0,column=6)

wn.config(menu=menubar)
wn.mainloop()
