import cv2

# ekstraksi foto
images = []
filename = input("Masukkan nama file : ")
path = r'..\Algeo02-21112\Dataset\{}.jpg'
img = cv2.imread(path.format(filename), 0)
if img is not None:
    img = cv2.resize(img, (256, 256))
    images.append(img)
    # menghasilkan foto hasil ekstraksi
    cv2.imwrite(r"..\Algeo02-21112\test\{}_extracted.jpg".format(filename), img)
else:
    print("input tidak sesuai")