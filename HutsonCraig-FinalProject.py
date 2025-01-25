"""
Title: Encryption Device
Author: Craig Hutson
Last Updated: 6 December, 2024
Purpose: To encrpyt/decrypt passwords
"""
from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Encryption Device")
root.geometry("400x400")
bg=PhotoImage(file="encrypt.png")
global ebutlabel
global dbutlabel
global rbutlabel

def encrypt2():
    global ebutlabel
    word=ebox.get()
    data=list(word)
    data.reverse()
    data.insert(0,"!")
    data.insert(-3,"%")
    data.insert(-1,"#")
    x="".join(data)
    ebutlabel=Label(frame1, text=x)
    ebutlabel.pack()

def decrypt():
    global dbutlabel
    word=dbox.get()
    data=list(word)
    data.reverse()
    for i in data:
        if i in ("!","%","#"):
            data.remove(i)
    x="".join(data)
    dbutlabel=Label(frame2, text=x)
    dbutlabel.pack(side="bottom")

def reset():
    ebutlabel.destroy()
    dbutlabel.destroy()
    rbutlabel=Label(root, text="Reset")
    rbutlabel.pack()

piclabel=Label(root, image=bg)
piclabel.place(x=0, y=0, relwidth=1, relheight=1)

frame1=LabelFrame(root, text="Encryption:", bg="deepskyblue3", padx=10, pady=10)
frame1.pack()
frame2=LabelFrame(root, text="Decryption:", bg="deepskyblue3", padx=10, pady=10)
frame2.pack()

ebox=Entry(frame1, width=20,)
ebox.pack(padx=5, pady=15)
dbox=Entry(frame2, width=20,)
dbox.pack(padx=5, pady=15)

ebutton=Button(root, text="Encrypt", width=15, bg="gray63", command=encrypt)
ebutton.pack(padx=5, pady=10)
dbutton=Button(root, text="Decrypt", width=15, bg="gray63", command=decrypt)
dbutton.pack(padx=5, pady=10)
rbutton=Button(root, text="Reset", width=15, bg="gray50", command=reset)
rbutton.pack(side="bottom", padx=5, pady=15)

img=ImageTk.PhotoImage(Image.open("padlock1.png"))
picLabel=Label(root, image=img)
picLabel.pack()




root.mainloop()
