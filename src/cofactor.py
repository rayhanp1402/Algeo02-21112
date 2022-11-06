import numpy as np
import math

def cofactor(list_photo):
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
  for i in range(0,len(list_photo)):
    list_photo[i] = np.subtract(list_photo[i],rate)
  for i in range(0,len(list_photo)):
    for baris in range(0,row):
      for kolom in range(0,col):
        if(list_photo[i][baris][kolom]<0):
          list_photo[i][baris][kolom] = list_photo[i][baris][kolom]*(-1)#kalau ada nilai negatif di pengurangan matrix
  for i in range(1,len(list_photo)):
    gabung = np.concatenate((list_photo[0],list_photo[i]),axis=1)
  trnsps = np.transpose(gabung)
  L = np.matmul(gabung,trnsps)
  return L


a = [[2,0,1],
     [1,2,0],
     [0,2,4]]
b = [[1,1,1],
     [0,1,0],
     [1,2,2]]
c = [a,b] #misalkan list matrik foto
d = cofactor(c)
print(d)