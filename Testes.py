from skimage.filters import gabor
from skimage import io
import cv2
import numpy as np
import pandas as pd

arr_mean = []
arr_var = []
arr_energy = []

caminho = '/home/daniel/PycharmProjects/TCC/Imagens_recortadas/st1012_0.ppm'
img = io.imread(caminho)

im = np.zeros((img.shape[0], img.shape[1]))
for m in range(0, img.shape[0]):
    for n in range(0, img.shape[1]):
        (a, b, c) = img[m, n]
        a = float(a)
        b = float(b)
        c = float(c)
        d = ((a + b + c) / 3)
        im[m, n] = d / 255

filt_real, filt_imag = gabor(im, theta=0.3927 * 0, frequency=5 / 10)

a = np.array(filt_real)

arr_mean.append(a.mean())
arr_var.append(a.var())
arr_energy.append(a.sum() * a.sum())

print(arr_mean)
print(arr_var)
print(arr_energy)