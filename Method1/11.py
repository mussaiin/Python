import vk_requests as v
from tkinter import *

def Enter(event):
    identry.focus_get()
    vksearch()

def vksearch(text):
    api=v.create_api(app_id="5584212", login="87088150515", password="zadrbek123")
    a=api.users.get(user_ids="%s" % text, fields=["bdate ","city", "music"]) #86691410
    print(a)

def vkfriends(text):    
    api=v.create_api(app_id="5584212", login="87088150515", password="zadrbek123")
    a=api.friends.get(user_id="%s" % text, fields=["bdate ","city", "music"]) #86691410
    print(a)    

def vkmusic(text):    
    api=v.create_api(app_id="5584212", login="87088150515", password="zadrbek123")
    a=api.audio.getCount(owner_id="%s" % text) #
    print(a)    
    
"""
def getinfo():
    for k,v in a.items():
        if(k=="first_name"):
            name.config(text="Имя: "+v)
            return name
#wn
wn=Tk()
wn.title("VK APP")
wn.geometry("300x300")

#frames
frm1=Frame(wn)
frm1.grid()
frm2=Frame(wn)
frm2.grid()
frm3=Frame(wn)
frm3.grid()

#labels
#intopframe
idtext=Label(frm1, text="Введите ID:")
idtext.grid(row=0, column=0)

#inmidframe
name=Label(frm2, text="Имя:")
name.grid(row=0, column=0)
surname=Label(frm2, text="Фамилия:")
surname.grid(row=1, column=0)
bday=Label(frm2, text="Дата рождения:")
bday.grid(row=2, column=0)
country=Label(frm2, text="Страна:")
country.grid(row=3, column=0)
city=Label(frm2, text="Город:")
city.grid(row=4, column=0)
friends=Label(frm2, text="Друзей:")
friends.grid(row=5, column=0)
audios=Label(frm2, text="Песен:")
audios.grid(row=6, column=0)
videos=Label(frm2, text="Видео:")
videos.grid(row=7, column=0)

#entrys
usid=StringVar()
identry=Entry(frm1, width=30, textvariable=usid)
identry.bind("<Return>", Enter)
identry.grid(row=0, column=1)
#buttons
idbttn=Button(frm1, text="Show", command=vksearch)
idbttn.grid(row=0, column=2)

wn.mainloop()
"""
