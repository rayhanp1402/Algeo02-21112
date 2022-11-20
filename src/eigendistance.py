import numpy as np
import math
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

def trainingimg (list_photo):
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
    return list_photo

def eigenface(eigvector,list_photo):
    rata = trainingimg(list_photo)
    for i in range(0,len(list_photo)):
        list_photo[i] = np.dot(eigvector,rata[i])
    return list_photo

def distance(eigvector,new,list_photo):
    rata2 = rate(list_photo)
    hasilnew = np.subtract(new,rata2)
    for i in range(0,len(hasilnew)):
        for j in range(0,len(hasilnew[0])):
            if(hasilnew[i][j]<0):
                hasilnew[i][j] = hasilnew[i][j]*(-1)
    eigenfacenew = np.dot(eigvector,hasilnew)
    tr = eigenface(eigvector,list_photo)
    for i in range(0,len(tr)):
        tr[i] = np.subtract(eigenfacenew,tr[i])
    acuan = tr[0]
    row = len(acuan)
    col = len(acuan[0])
    for i in range(0,len(tr)):
        for j in range(0,row):
            for k in range(0,col):
                tr[i][j][k] = (tr[i][j][k])**(2)
    hasilakhir = [0 for i in range(len(tr))]
    for i in range(0,len(hasilakhir)):
        for j in range(0,row):
            for k in range(0,col):
                hasilakhir[i] += tr[i][j][k]
    for i in range(0,len(hasilakhir)):
        hasilakhir[i] = hasilakhir[i]**(1/2)
    return hasilakhir
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




