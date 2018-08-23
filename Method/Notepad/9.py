from tkinter import *
wn=Tk()
wn.geometry("350x350")
wn.title("Notepad")

def newfile():
    global filename
    wn.title("Untitled")
    filename=None
    textPad.delete(1.0,END)
    
def save():
    f1=filedialog.asksaveasfile()
    file=open(f1, "w")
    content=textPad.get(1.0, END)
    file.write(content)
    file.close()
    
def saveas():
    f2=filedialog.asksaveasfilename()
    file=open(f2, "w")
    content=textPad.get(1.0, END)
    file.write(content)
    file.close()    

def about():
    messagebox.showinfo("info","message")

def Help():
    messagebox.showinfo("info","message")

def on_find():
    t2=Toplevel(wn)
    t2.title("Find")
    t2.geometry("265x65+200+250")
    Label(t2, text="Find All").grid(row=0, column=0)
    y=StringVar()
    e=Entry(t2, width=25, textvariable=y)
    e.grid(row=0, column=1)
    e.focus_set()
    Button(t2, text="Find", command=lambda:search_for(y.get(), textPad, t2, e)).grid(row=0, column=2)
    def close_search():
        textPad.tag_remove("match", "1.0", END)
        t2.destroy()
    t2.protocol("WN_DELETE_WINDOW", close_search)

def search_for(n, textPad, t2, e):
    textPad.tag_remove('match', '1.0', END)
    count=0
    if n:
        pos='1.0'
        while True:
            pos=textPad.search(n, pos, stopindex=END)
            if not pos:
                break
            lastpos="%s+%dc" %(pos, len(n))
            textPad.tag_add('match', pos, lastpos)
            count+=1
            pos = lastpos
        textPad.tag_config('match', foreground="red", background="yellow")
    e.focus_set()
    t2.title("%d matches found" %count)
    
def exitclose():
    if messagebox.askokcancel("Exit", "Do you really want to close?"):
        wn.destroy()
        exit()
        
def Undo():
    textPad.event_generate("<<Undo>>")
def Redo():
    textPad.event_generate("<<Redo>>")
def Cut():
    textPad.event_generate("<<Cut>>")
def Copy():
    textPad.event_generate("<<Copy>>")
def Paste():
    textPad.event_generate("<<Paste>>")

def openfile():
    filedialog.askopenfile()
def savefile():
    filedialog.asksaveasfile()
def saveasfile():
    filedialog.asksaveasfilename()
def exitfile():
    filedialog.exit()  
def selectall():
    textPad.tag_add('select','1.0','end')
    
menubar=Menu(wn)

#images
newicon=PhotoImage(file="icons/new_file.gif")
openicon=PhotoImage(file="icons/open_file.gif")
saveicon=PhotoImage(file="icons/save.gif")
undoicon=PhotoImage(file="icons/undo.gif")
redoicon=PhotoImage(file="icons/redo.gif")
cuticon=PhotoImage(file="icons/cut.gif")
copyicon=PhotoImage(file="icons/copy.gif")
pasteicon=PhotoImage(file="icons/paste.gif")

#commandsframe
frame=Frame(wn)
frame.pack(fill=X)
b1=Button(frame, compound=LEFT, image=newicon, command=newfile)
b1.grid(row=0,column=0)
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

#menu
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)

viewmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu)

aboutmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="About",menu=aboutmenu)

#filemenu
filemenu.add_command(label="New File", accelerator="Ctrl+N", command=newfile, compound=LEFT,image=newicon,underline=0)
filemenu.add_command(label="Open File", accelerator="Ctrl+O", command=openfile, compound=LEFT,image=openicon,underline=0)
filemenu.add_command(label="Save", accelerator="Ctrl+S", command=save,compound=LEFT,image=saveicon,underline=0)
filemenu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=saveas, compound=LEFT,underline=0)
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator="Alt+F4", command=exitclose, compound=LEFT, underline=0)

#editmenu
editmenu.add_command(label="Undo", accelerator="Ctrl+Z", command=Undo, compound=LEFT,image=undoicon,underline=0)
editmenu.add_command(label="Redo", accelerator="Ctrl+Y", command=Redo, compound=LEFT,image=redoicon,underline=0)
editmenu.add_separator()
editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=Cut, compound=LEFT,image=cuticon,underline=0)
editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=Copy, compound=LEFT,image=copyicon,underline=0)
editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=Paste, compound=LEFT,image=pasteicon,underline=0)
editmenu.add_separator()
editmenu.add_command(label="Find", accelerator="Ctrl+F", command=on_find, compound=LEFT,underline=0)
editmenu.add_command(label="Select All", accelerator="Ctrl+A", command=selectall, compound=LEFT,underline=0)

#viewmenu
showIn=IntVar()
showIn.set(True)
showIn1=IntVar()
showIn1.set(True)
showIn2=IntVar()
showIn2.set(False)

viewmenu.add_checkbutton(label="Show Line Number", variable=showIn)
viewmenu.add_checkbutton(label="Show Info Bar at Bottom", variable=showIn1)
viewmenu.add_checkbutton(label="Highlight Current Line", variable=showIn2)

#aboutmenu
aboutmenu.add_command(label="About", command=about, compound=LEFT,underline=0)
aboutmenu.add_command(label="Help", command=Help, compound=LEFT,underline=0)

#thememenu
thememenu=Menu(viewmenu,tearoff=0)
viewmenu.add_cascade(label="Themes", menu=thememenu)

themeArray={
    '1. Default White':'FFFFFF',
    '2. Greygarrious Grey':'D1D4D1',
    '3. Lovely Lavender':'E1E1FF',
    '4. Aquamarine':'D1E7E0',
    '5. Bold Beige':'FFF0E1',
    '6. Cobalt Blue':'333AA',
    '7. Olive Green':'5B8340'
    }
v=StringVar()
v.set('1. Default White')
for k in sorted(themeArray):
    thememenu.add_radiobutton(label=k,variable=v)



#textPad
textPad=Text(wn, undo=True)
textPad.pack(expand=YES,fill=BOTH)
scroll=Scrollbar(textPad)
textPad.configure(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT,fill=Y)

wn.config(menu=menubar)
wn.mainloop()
