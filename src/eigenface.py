import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import os

window = tk.Tk()
window.title("Face Recognition")

judul = tk.Label(window,text="Selamat datang di Face Recognition")
judul.grid(column=0,row=0)


logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logobel = tk.Label(image=logo)
logobel.image = logo
logobel.grid(column=0,row=1)

ingfolder = '' #buat folder training image 
copy = '' #copy folder training image
def cari():
    ingfolder = filedialog.askdirectory()
    global copy 
    copy = ingfolder
    if(ingfolder==''):
        hasilfolder.config(text='Belum milih folder nih')
    elif(ingfolder!=''):
        hasilfolder.config(text='Mantap')

foldertraining = tk.Label(window,text="Input training image")
foldertraining.grid(column=0,row=3) 
butttraining = tk.Button(window,text="Select",command=lambda:cari())
butttraining.grid(column=0,row=4)
hasilfolder = tk.Label(window,text='Pilih yuk pilih')
hasilfolder.grid(column=0,row=5)

image = tk.Label(window,text="Input test image")
image.grid(column=0,row=6)
imagename=''
copyimage=''

def openimage():
    if(copy==''):
        hasilimage.config(text="Belum ada folder training mazeh")
    elif(copy!=''):
        ftypes = [('Jpg','*.jpg'),('PNG','*.png')]
        imagename = filedialog.askopenfilename(filetypes=ftypes)
        global copyimage
        global displayimage
        copyimage = imagename
        if(imagename==''):
            hasilimage.config(text='Belum milih file nih')
        elif(imagename!=''):
            hasilimage.config(text='Mantap')
            img = Image.open(imagename)
            img2 = img.resize((256,256))
            displayimage = ImageTk.PhotoImage(img2)
            Labelimage.config(image=displayimage,width=256,height=256)
            Labelmirip.config(image=displayimage,width=256,height=256)
    
imagebut = tk.Button(window,text="Select",command=openimage)
imagebut.grid(column=0,row=7)
hasilimage = ttk.Label(window,text="Pilih yuk pilih")
hasilimage.grid(column=0,row=8)


imageframe = tk.LabelFrame(window,text="Test Image")
imageframe.grid(column=2,row=1,rowspan=7)
Labelimage = tk.Label(imageframe,width=36,height=16)
Labelimage.pack()

Imagemirip = tk.LabelFrame(window,text="Closest Image")
Imagemirip.grid(column=3,row=1,rowspan=7)
Labelmirip = tk.Label(Imagemirip,width=36,height=16)
Labelmirip.pack()
window.mainloop()