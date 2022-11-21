import numpy as np
import cv2

# def trnsflat(list):
#     trans = np.zeros(shape=(len(list),1))
#     for i in range(len(list)):
#         trans[i][0] = list[i]
#     return trans
def extraxtor_img(file_path):
    img = cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    
    return img
#k = extraxtor_img('D:\python\Tubes Algeo 2\Algeo02-21112\dataset\Adriana1.jpg')
#print(k[65535][0])