import cv2
import numpy as np
import os
#from PIL import Image as Img,ImageTk
#from tkinter import *
def trnsflat(list):
    trans = np.zeros(shape=(len(list),1))
    for i in range(len(list)):
        trans[i][0] = list[i]
    return trans

def extractor_data(file_path):
    images = []
    images_kotak = []
    path = file_path
    for filename in os.listdir(path):
        img = cv2.imread(os.path.join(path, filename))#display
        img = cv2.resize(img, (256, 256))#display
        
        images_kotak.append(img)#display


        img_gray = cv2.imread(os.path.join(path, filename),cv2.IMREAD_GRAYSCALE)#hitung
        img_gray = cv2.resize(img_gray, (256, 256))#hitung

        img_gray = img_gray.flatten()#di flat buat hitung
        transflat = trnsflat(img_gray)
        images.append(transflat) 
    return images,images_kotak
#k,l = extractor('D:\python\Tubes Algeo 2\Algeo02-21112\dataset')


#win = Tk()
#win.geometry("700x550")
#p = l[2]
#blue,green,red = cv2.split(p)
#img = cv2.merge((red,green,blue))
#im = Img.fromarray(img)
#imgtk = ImageTk.PhotoImage(image=im)
#Label(win, image= imgtk).pack()
#win.mainloop()