import numpy as np
import math
from eigen2 import *
from kofarian import *
def trnsflat(list):
    trans = np.zeros(shape=(len(list),1))
    for i in range(len(list)):
        trans[i][0] = list[i]
    return trans
#-------------------------------------------
def rate(list_photo):
    n1 = list_photo[0]
    row = len(n1)
    col = len(n1[0])
    d = np.zeros(shape=(row,col))
    for i in range(0,len(list_photo)):
        d = np.add(d,list_photo[i])
    rate = d/len(list_photo)
    for i in range(0,len(rate)):
        for j in range(0,len(rate[0])):
            rate[i][j] = math.floor(rate[i][j])
    return rate

def kurangdgnrata2 (list_photo):
    n1 = list_photo[0]
    row = len(n1)
    col = len(n1[0])
    rata2 = rate(list_photo)
    for i in range(0,len(list_photo)):
        list_photo[i] = np.subtract(list_photo[i],rata2)
    for i in range(0,len(list_photo)):
        for baris in range(0,row):
            for kolom in range(0,col):
                if(list_photo[i][baris][kolom]<0):
                    list_photo[i][baris][kolom] = list_photo[i][baris][kolom]*(-1)
    gabung = list_photo[0]
    for i in range(1,len(list_photo)):
        gabung = np.concatenate((gabung,list_photo[i]),axis=1)
    return gabung
def eigenface(list_photo):
    kov = kofarian(list_photo)
    eigvec = eigenVector(kov)
    matrixkrg = kurangdgnrata2(list_photo)
    hasil = np.matmul(matrixkrg,eigvec)
    return hasil






    

def dotkali(matrix1,matrix2):
    row = len(matrix1)
    col = len(matrix1[0])
    d = np.zeros(shape=(row,col))
    for i in range(row):
        d[i] = matrix1[i][0]*matrix2[i][0]
    hasil = 0
    for i in range(row):
        hasil+=d[i]
    return hasil
def splitmatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    hasil = []
    d = np.zeros(shape=(row,1))
    for i in range(col):
        for j in range(row):
            d[j] += matrix[j][i]
        hasil.append(d)
        d = np.zeros(shape=(row,1))
    return hasil

# a = np.array([[2,0,1],
#      [1,2,0],
#      [0,2,4]])

# b = np.array([[1,1,1],
#      [0,1,0],
#      [1,2,2]])
# a = a.flatten()
# a = trnsflat(a)

# b = b.flatten()
# b = trnsflat(b)
# d = [a,b]
# e = [a,b]
# test = eigenface(e)
# print(test)
# ngesplit = splitmatrix(a)
# print(ngesplit)




def berat_eigface(list_photo):
    eigface = eigenface(list_photo)
    hasil_akhir=[]
    hasil_split = splitmatrix(eigface)
    col = len(hasil_split)
    berat = np.zeros(shape=(col,1))
    for j in range(col):
        for k in range(col):
            d = dotkali(hasil_split[j],hasil_split[k])/dotkali(hasil_split[k],hasil_split[k])
            berat[k][0] += d
        hasil_akhir.append(berat)
        berat = np.zeros(shape=(col,1))

    return hasil_akhir

def panjangmatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    jml = 0
    for i in range(col):
        for j in range(row):
            matrix[j][i]=matrix[j][i]**2
    for i in range(col):
        for j in range(row):
            jml+=matrix[j][i]
    hasil = jml**(1/2)
    return hasil
    
def getMinIdx(list):
    min = list[0]
    for i in range(0,len(list)):
        if(min>list[i]):
            min = list[i]
    for i in range(0,len(list)):
        if(min==list[i]):
            idx = i
            break
    return idx

def cek_img(new_img,list_photo):
    rata2 = rate(list_photo)
    kurang_img =  np.subtract(new_img,rata2)
    for j in range(len(new_img[0])):
        for i in range(len(new_img)):
            if((kurang_img[i][j])<0):
                kurang_img[i][j] = kurang_img[i][j]*(-1)
    eigface = eigenface(list_photo)
    ngesplit = splitmatrix(eigface)
    berat_training=berat_eigface(list_photo)
    berat_img = np.zeros(shape=(len(ngesplit),1))
    for i in range (len(ngesplit)):
        berat_img[i] += dotkali(kurang_img,ngesplit[i])/dotkali(ngesplit[i],ngesplit[i])
    for i in range(len(ngesplit)):
        berat_training[i] = np.subtract(berat_img,berat_training[i])
    for i in range(len(ngesplit)):
        berat_training[i] = panjangmatrix(berat_training[i])
    return berat_training
    
    

        


# a = np.array([[2,0,1],
#      [1,2,0],
#      [0,2,4]])

# b = np.array([[1,1,1],
#      [0,1,0],
#      [1,2,2]])
# new = np.array([[2,1,2],
#      [0,3,4],
#      [1,1,4]])
# a = a.flatten()
# a = trnsflat(a)

# b = b.flatten()
# b = trnsflat(b)

# new = new.flatten()
# new = trnsflat(new)

# d = [a,b]

# hasil = cek_img(new,d)
# print(hasil)

# # test = eigenface(e)
# # print(test)
# # ngesplit = splitmatrix(a)
# # print(ngesplit)
# berat = berat_eigface(d)
# print(berat)

        








