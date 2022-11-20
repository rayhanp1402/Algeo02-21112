import cv2
import os
import numpy

# 1. Extract dataset training images
folder = input("Masukkan nama folder dataset: ")
images = []
count = 0 

for filename in os.listdir(r"..\Algeo02-21112\{}".format(folder)):
    img = cv2.imread(os.path.join(r"..\Algeo02-21112\{}".format(folder), filename), cv2.IMREAD_GRAYSCALE)
    if img is not None:
        img = cv2.resize(img, (256, 256))
        img = img.flatten() 
        images.append(img) 
        count += 1

# 2. Mencari nilai rata-rata dataset
sum = [0 for j in range(65536)] # 256 x 256
for i in range(count):
    sum = numpy.add(sum, images[i]) 
mean = numpy.divide(sum, count)

# 3. mencari selisih training images terhadap rata-rata
for i in range(count):
    images[i] = numpy.subtract(images[i], mean)