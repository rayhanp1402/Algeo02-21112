import cv2
import numpy as np
import os


def trnsflat(list):
    trans = np.zeros(shape=(len(list),1))
    for i in range(len(list)):
        trans[i][0] = list[i]
    return trans

def extractor_data(file_path):
    images = []
    pathallimage = []
    path = file_path
    for filename in os.listdir(path):
        pathofimage = os.path.join(path, filename)#display
        
        pathallimage.append(pathofimage)#display


        img_gray = cv2.imread(os.path.join(path, filename),cv2.IMREAD_GRAYSCALE)#hitung
        img_gray = cv2.resize(img_gray, (100, 100))#hitung
        img_gray = img_gray.flatten()
        trnsp = trnsflat(img_gray)

        images.append(trnsp) 
    return images,pathallimage

def nama_path(path):
    nama_file = os.path.basename(path)
    file = os.path.splitext(nama_file)
    return file[0]
# k,l = extractor_data('D:\\python\\Tubes Algeo 2\\Algeo02-21112\\test\\dataset')
# hasil = nama_path(l[0])
# print(hasil)




