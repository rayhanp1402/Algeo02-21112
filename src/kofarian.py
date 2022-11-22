import numpy as np
import math
from extracdata_func import *
# from eigen import *

def kofarian(list_photo):
  n1 = list_photo[0]
  row = len(n1)
  col = len(n1[0])
  d = np.zeros(shape=(row,col))
  for i in range(0,len(list_photo)):
    d = np.add(d,list_photo[i])
  rate = d/len(list_photo)
  for i in range(0,len(list_photo)):
    list_photo[i] = np.subtract(list_photo[i],rate)
  gabung = list_photo[0]
  for i in range(1,len(list_photo)):
    gabung = np.concatenate((gabung,list_photo[i]),axis=1)
  trnsps = np.transpose(gabung)
  L = np.dot(trnsps,gabung)
  return L

# k,l = extractor_data('..\Algeo02-21112\test\dataset')
# p = kofarian(k)
# print(len(p))
# print(len(p[0]))
# print(type(p[0][0]))
# a = EigenValue(p)
# print(a)
# # p = len(l)


