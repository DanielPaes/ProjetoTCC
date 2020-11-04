import cv2
import numpy as np



img = cv2.imread('st1012.ppm')
x = img.shape[0]
y = img.shape[1]

im = np.zeros((x, y))
print(im)

for m in range(0, img.shape[0]):
    for n in range(0, img.shape[1]):
        (a, b, c) = img[m, n]
        a = float(a)
        b = float(b)
        c = float(c)
        d = ((a + b + c)/3)
        print(type(d))
        im[m, n] = d / 255


print(im)

cv2.imshow('Media - RGB',im)
cv2.waitKey(0)
