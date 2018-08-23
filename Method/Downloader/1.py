import requests,bs4,os
import webbrowser as web
from tkinter import *

os.makedirs("Images Folder", exist_ok=True)

def stat(links, images):
    img1.config(text="Images:"+images)
    urls1.config(text="Links:"+links)
    wn.update()
    
def download(event=None):
    try:
        url=entry.get()
        if not (url.startswith("http://")):
            url="http://"+url
            print(url)
        index = requests.get(url)
        soup=bs4.BeautifulSoup(index.text, "html.parser")
        links=soup.select("a")
        images=soup.select("img")
        stat(str(len(links)), str(len(images)))
        for i in images:
            image_url=i.get("src")
            print(image_url)
            if(image_url!="" or image_url!=None):
                pos=image_url.rfind("/")+1
                filename=image_url[pos:]
                image_src=image_url
                img1.config(text="Downloading "+filename+"...", fg="green")
                wn.update()
                r=requests.get(image_src)
                file=open("Images Folder", filename, 'wb')
                file.write(r.content)
                file.close()
        img1.config(text="Done!", fg='blue')
        wn.update()
    except:
        img1.config(text="Connection or link error!", fg="red")
        wn.update()

wn=Tk()
wn.title("IMG Downloader")
wn.geometry("400x300")
wn.config="#969696"
frame1=Frame(wn, bg="#DCDCDC")
frame1.pack()

label=Label(frame1, text="Type Link:", font="Calibre",bg="#DCDCDC")
label.grid(row= 0 , column = 0)

entry=Entry(frame1,width='30')
entry.grid(row= 0 , column = 1)
#entry.bind("<Return>)

button=Button(frame1, text="Download", font = 'Calibre', command = download)
button.grid(row= 0 , column = 2)

frame2=Frame(wn,bg="#DCDCDC")
frame2.pack()
a=0
img1=Label(frame2, text="Images Downloaded:"+str(a), font="Calibre",bg="#DCDCDC")
img1.pack()

urls1=Label(frame2, text="Links Found:"+str(a), font="Calibre",bg="#DCDCDC")
urls1.pack()

wn.mainloop()
