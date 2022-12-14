import numpy as np
import math
from eigen2 import *
from kofarian import *

def swapColumn(Matrix, Column1, Column2):
    temp = np.zeros(Matrix.shape[1])
    for i in range(Matrix.shape[1]):
        temp[i] = Matrix[i, Column1]

    for i in range(Matrix.shape[1]):
        Matrix[i, Column1] = Matrix[i, Column2]
        Matrix[i, Column2] = temp[i]

    return Matrix

def sortEigen(eigenValue, eigenVecMatrix):
    for i in range(eigenVecMatrix.shape[1]):
        for j in range(eigenVecMatrix.shape[1]):
            if(i != j and eigenValue[i] >= eigenValue[j]):
                swapColumn(eigenVecMatrix, i, j)
                temp = eigenValue[i]
                eigenValue[i] = eigenValue[j]
                eigenValue[j] = temp

    return (eigenValue, eigenVecMatrix)
                

def potongmatrix(Matrix):
    row = len(Matrix)
    col = len(Matrix[0])
    
    if(col<=100):
        kosong = np.zeros(shape=(row,col-1))
        for i in range(row):
            for j in range(col-1):
                kosong[i][j] = Matrix[i][j]
        return kosong
    elif(col>100):
        kosong2 = np.zeros(shape=(row,100))
        for i in range(row):
            for j in range(100):
                kosong2[i][j] += Matrix[i][j]
        return kosong2




def rate(list_photo):
    n1 = list_photo[0]
    row = len(n1)
    col = len(n1[0])
    d = np.zeros(shape=(row,col))
    for i in range(0,len(list_photo)):
        d = np.add(d,list_photo[i])
    rate = d/len(list_photo)
    return rate

def kurangdgnrata2 (list_photo):
    n1 = list_photo[0]
    row = len(n1)
    col = len(n1[0])
    rata2 = rate(list_photo)
    for i in range(0,len(list_photo)):
        list_photo[i] = np.subtract(list_photo[i],rata2)
    gabung = list_photo[0]
    for i in range(1,len(list_photo)):
        gabung = np.concatenate((gabung,list_photo[i]),axis=1)
    return gabung
def eigenface(list_photo):
    kov = kofarian(list_photo)
    eigvalue = eigenValue(kov)[0]
    eigvec = eigenVector(kov)
    disort = sortEigen(eigvalue,eigvec)[1]
    dipotong = potongmatrix(disort)
    matrixkrg = kurangdgnrata2(list_photo)
    hasil = np.dot(matrixkrg,dipotong)
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






def berat_eigface(list_photo,eigen_face):
    krgmatrix = kurangdgnrata2(list_photo)
    splitkrgmatrix = splitmatrix(krgmatrix)
    eigface = eigen_face
    hasil_akhir=[]
    hasil_split = splitmatrix(eigface)
    col = len(hasil_split)
    berat = np.zeros(shape=(col,1))
    for j in range(col):
        for k in range(col):
            d = dotkali(splitkrgmatrix[j],hasil_split[k])/dotkali(hasil_split[k],hasil_split[k])
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
    
def cek_img(new_img,list_photo,eigen_face,weight_training):
    rata2 = rate(list_photo)
    kurang_img =  np.subtract(new_img,rata2)
    eigface = eigen_face
    ngesplit = splitmatrix(eigface)
    berat_training=weight_training
    berat_img = np.zeros(shape=(len(ngesplit),1))
    for i in range (len(ngesplit)):
        berat_img[i] += dotkali(kurang_img,ngesplit[i])/dotkali(ngesplit[i],ngesplit[i])
    for i in range(len(ngesplit)):
        berat_training[i] = np.subtract(berat_img,berat_training[i])
    for i in range(len(ngesplit)):
        berat_training[i] = panjangmatrix(berat_training[i])
    return berat_training
    
    

        




# print(eigenValue(a)[0])
# print(eigenVector(a))
# print(sortEigen(eigenValue(a)[0], eigenVector(a))[0])
# print(sortEigen(eigenValue(a)[0], eigenVector(a))[1])