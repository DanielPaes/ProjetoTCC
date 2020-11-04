from skimage.color import rgb2gray
import cv2
from skimage import io
from skimage.filters import gabor

img = io.imread('st1012.ppm')

img_ski = rgb2gray(img)
cv2.imshow('Gray_Skimage',img_ski)
cv2.waitKey(0)

img_open = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray_OpenCV',img_open)
cv2.waitKey(0)

filt_real, filt_imag = gabor(img_ski, theta=2*0.3927 , frequency= 0.9)
gabor_img_ski = filt_real
cv2.imshow('Gabor_Skimage',filt_real)
cv2.waitKey(0)

filt_real, filt_imag = gabor(img_open, theta=2*0.3927 , frequency= 0.9)
gabor_img_open = filt_real
cv2.imshow('Gabor_OpenCV',filt_real)
cv2.waitKey(0)


print(gabor_img_ski)
print(gabor_img_open)


