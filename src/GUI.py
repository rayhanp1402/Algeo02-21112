import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image as Img
from extracdata_func import *
from kofarian import *
from eigen2 import *
from extractor_func import *
from eigendistance import *
import time


window = tk.Tk()
window.title("Face Recognition")

judul = tk.Label(window,text="Selamat datang di Face Recognition")
judul.grid(column=0,row=0)


logo = Img.open('D:python\\Tubes Algeo 2\\Algeo02-21112\\src\\logo.png')
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
        global displayclosest
        copyimage = imagename
        if(imagename==''):
            hasilimage.config(text='Belum milih file nih')
        elif(imagename!=''):
            hasilimage.config(text='Mantap')
            start = time.time()
            img = Img.open(imagename)
            img2 = img.resize((256,256))
            displayimage = ImageTk.PhotoImage(img2)
            Labelimage.config(image=displayimage,width=256,height=256)
            #----------------------------------------------------
            #------------------Hitung Hitung---------------------
            #-----------------------------------------------------
            list_foto,direktori = extractor_data(copy)
            copy_list_foto,buang = extractor_data(copy)
            copy_list_foto2,buang2 = extractor_data(copy)
            eig_face_list_foto = eigenface(list_foto)
            weight_training_foto = berat_eigface(copy_list_foto2,eig_face_list_foto)
            ekstrak = extraxtor_img(imagename)
            berat_image = cek_img(ekstrak,copy_list_foto,eig_face_list_foto,weight_training_foto)
            getminimum = getMinIdx(berat_image)
            if(berat_image[getminimum]<0.30):
                imageclosest = Img.open(direktori[getminimum])
                imageclosest2 = imageclosest.resize((256,256))
                displayclosest = ImageTk.PhotoImage(imageclosest2)
                Labelmirip.config(image=displayclosest,width=256,height=256)
                HasilResult.config(text=nama_path(direktori[getminimum]))
                end = time.time()
                waktu = end-start
                hasil_waktu = f'{waktu:.2f}'
                TimeDis.config(text=hasil_waktu)
                print(berat_image[getminimum])
            elif(berat_image[getminimum]>0.30 and berat_image[getminimum]<0.40):
                HasilResult.config(text="Tidak ada yang mirip")
                imageclosest = Img.open('D:python\\Tubes Algeo 2\\Algeo02-21112\\src\\default.png')
                imageclosest2 = imageclosest.resize((256,256))
                displayclosest = ImageTk.PhotoImage(imageclosest2)
                Labelmirip.config(image=displayclosest,width=256,height=256)
                end = time.time()
                waktu = end-start
                hasil_waktu = f'{waktu:.2f}'
                TimeDis.config(text=hasil_waktu)
                berat_image = []
            else:
                HasilResult.config(text="Image tidak diterima")
                imageclosest = Img.open('D:python\\Tubes Algeo 2\\Algeo02-21112\\src\\default.png')
                imageclosest2 = imageclosest.resize((256,256))
                displayclosest = ImageTk.PhotoImage(imageclosest2)
                Labelmirip.config(image=displayclosest,width=256,height=256)
                end = time.time()
                waktu = end-start
                hasil_waktu = f'{waktu:.2f}'
                TimeDis.config(text=hasil_waktu)
                print(berat_image[getminimum])
                berat_image = []

    
imagebut = tk.Button(window,text="Select",command=openimage)
imagebut.grid(column=0,row=7)
hasilimage = ttk.Label(window,text="Pilih yuk pilih")
hasilimage.grid(column=0,row=8)


dasar = Img.open('D:python\\Tubes Algeo 2\\Algeo02-21112\\src\\default.png')
dasar = ImageTk.PhotoImage(dasar)


imageframe = tk.LabelFrame(window,text="Test Image")
imageframe.grid(column=2,row=1,rowspan=7)
Labelimage = tk.Label(imageframe,width=256,height=256,image=dasar)
Labelimage.pack()

Imagemirip = tk.LabelFrame(window,text="Closest Image")
Imagemirip.grid(column=3,row=1,rowspan=7)
Labelmirip = tk.Label(Imagemirip,width=256,height=256,image=dasar)
Labelmirip.pack()

Result = tk.Label(window,text="Result:")
Result.grid(column=2,row=8)
HasilResult = tk.Label(window,text="")
HasilResult.grid(column=2,row=9)

TimeEx = tk.Label(window,text="Time Execution:")
TimeEx.grid(column=3,row=8)
TimeDis = tk.Label(window,text="")
TimeDis.grid(column=3,row=9)
window.mainloop()