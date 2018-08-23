from tkinter import *
import requests
wn=Tk()
wn.title("Canvas")
wn.geometry('300x300')

def Enter(event):
    entry.focus_get()
    click()
def click():
    canvas.delete(ALL)
    canvas.create_text(150, 20, text="Погода на сегодня:", fill='white', font="Arial 12")
    link="http://api.openweathermap.org/data/2.5/weather?q="+city.get()+"&units=metric&APPID=6bab4d6713adbf3a428b1f2a7454395d"
    r=requests.get(link)
    temp=r.json()['main']['temp']
    canvas.create_text(150, 100, text=city.get(), fill='white', font="Arial 20")
    canvas.create_text(150, 150, text=str(temp)+"C", fill='red', font="Arial 20")
#frames
topFrame=Frame(wn)
topFrame.grid()
bottomFrame=Frame(wn)
bottomFrame.grid()
#labels
label=Label(topFrame, text="Введите город:", font="Arial 12")
label.grid(row=0,column=0)
#entry
city=StringVar()
entry=Entry(topFrame,width=20,textvariable=city)
entry.bind("<Return>", Enter)
entry.grid(row=0,column=1)
#button
button=Button(topFrame, text='Show', font="Arial 12", command=click)
button.grid(row=0,column=2)

canvas = Canvas(bottomFrame, height=295, width=295, bg='black')
#arc=canvas2.create_arc(coord,start=30,extent=330,fill='red')
#canvas2.create_text(150,150,text='Hello',font='Calibri 20')
canvas.grid()
wn.mainloop()

"""
canvas1 = Canvas(window,height=300,width=300,bg='white')
canvas1.create_line(0,0,300,300)
canvas1.create_oval(50,50,200,200)
canvas1.create_rectangle(100,150,200,250)
canvas1.delete(ALL)
canvas1.pack()
"""
