from tkinter import *
import requests

def from_kzt():
    money=float(KZT.get())
    usd.set(round(money/rates['KZT'],2))
def from_usd():
    money=float(US.get())
    kz.set(round(money*rates['KZT'],2))    
window=Tk()
window.minsize(250,200)
window.title("Converter")

r=requests.get("https://openexchangerates.org/api/latest.json?app_id=60da2bd9b3064714b2c5f2e8b00fbd40")
rates=r.json()['rates']

USD=Label(window,text="$:", fg='blue', font=("Times New Roman", 24))
TG=Label(window,text="₸:", fg='blue', font=("Times New Roman", 24))

USD.grid(row=0,column=0)
TG.grid(row=1, column=0)

usd=StringVar()
US=Entry(window,  width=20, textvariable=usd)
kz=StringVar()
KZT=Entry(window, width=20, textvariable=kz)

US.grid(row=0,column=1)
KZT.grid(row=1,column=1)

bt=Button(window,text='Convert',fg='blue', command=from_usd)
bt.grid(row=0,column=2)
bt1=Button(window,text='Convert',fg='blue', command=from_kzt)
bt1.grid(row=1,column=2)

"""
def click():
    login=entry1.get()
    pas=entry2.get()
    if(login=='1'):
        if(pas=="1"):
            window1.destroy()
            window2=Tk()
            txt=Label(window2,text="Welcome!",fg='green')
            txt.pack()
            window2.mainloop()
    else:
            wrng=Label(window1,text="smth is incorrect", fg='red')
            wrng.grid(columnspan=2)
login=Label(window1,text="Login:")
pas=Label(window1,text="Password:")

entry1=Entry(window1)
entry2=Entry(window1)

login.grid(row=0)
pas.grid(row=1)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

c=Checkbutton(window1,text="Keep me logged in")
c.grid(columnspan=2)

button1=Button(window1,text='Click Me!',fg='red', command=click)
button1.grid(columnspan=2)
"""
'''
def lc(event):
    print("Left")
def rc(event):
    print("Right")
def mid(event):
    print("Middle")

frame=Frame(window,width=300, height=250)
frame.bind("<Button-1>",lc)
frame.bind("<Button-2>",mid)
frame.bind("<Button-3>",rc)
frame.pack()
'''
'''
def pn():
    print("Hello World!")
button1=Button(window,text='Click Me!', command=pn)
button1.grid()
""
""
label1=Label(window,text="Name:")
label2=Label(window,text="Surname:")
label3=Label(window,text="E-Mail:")
label4=Label(window,text="Password:")

entry1=Entry(window)
entry2=Entry(window)
entry3=Entry(window)
entry4=Entry(window)

label1.grid(row=0)
label2.grid(row=1)
label3.grid(row=2)
label4.grid(row=3)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)
entry4.grid(row=3,column=1)

c=Checkbutton(window,text="Keep me logged in")
c.grid(columnspan=2)

button1=Button(window,text='Click Me!',fg='red')
button1.grid(columnspan=2)
'''
'''
topFrame=Frame(window)
topFrame.pack()
bottomFrame=Frame(window)
bottomFrame.pack(side=BOTTOM)

theLabel=Label(topFrame,text="name:",bg='blue',fg='white')
theLabel.pack(side=LEFT) #pack - to show

entry=Entry(topFrame)
entry.pack(side=LEFT)

button1=Button(bottomFrame,text='Click Me!',fg='red')
button1.pack(side=BOTTOM)
'''
'''
theLabel=Label(window,text="Hello World!")
theLabel.pack() #pack - to show

topFrame=Frame(window)
topFrame.pack()

bottomFrame=Frame(window)
bottomFrame.pack(side=BOTTOM)

button1=Button(topFrame,text='Button1',fg='red')
button1.pack(side=LEFT)
button2=Button(topFrame,text='Button1',fg='green')
button2.pack(side=LEFT)
button3=Button(topFrame,text='Button1',fg='blue')
button3.pack(side=LEFT)
button1=Button(bottomFrame,text='Button1',fg='purple')
button1.pack(side=BOTTOM)
'''
'''
one=Label(window,text="One",bg='red',fg='white')
one.pack()
two=Label(window,text="Two",bg='green',fg='black')
two.pack(fill=X)
three=Label(window,text="Three",bg='blue',fg='white')
three.pack(side=LEFT, fill=Y)
'''

window.mainloop()

