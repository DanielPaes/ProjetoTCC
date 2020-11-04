from skimage.filters import gabor
from skimage import io
import cv2
import numpy as np
import pandas as pd


matriz = []
df = pd.DataFrame(matriz)
lista_nomes = []

for i in range(1012, 1851):
    for l in range(0, 56):
        a = []
        b = []
        d = []
        try:
            caminho = '/home/daniel/PycharmProjects/TCC/Imagens_recortadas/st' + str(i) + '_' + str(l) + '.ppm'
            img = io.imread(caminho)
            image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            x = str(i) + '_' + str(l)
            print('Filtrando a Imagem st' + x)
            lista_nomes.append(x)

            for t in range(0,8):
                for f in range (2, 10):
                    filt_real, filt_imag = gabor(image, theta=0.3927*t, frequency=f/10)
                    a = np.array(filt_real)
                    b.append(a)
            d = np.array(b)
            matriz.append([d.mean(), d.var(), d.sum()*d.sum()])



        except:
            print('erro')

df = pd.DataFrame(matriz)

df2 = pd.DataFrame(lista_nomes)


df.to_csv(r'/home/daniel/Área de Trabalho/Filtro_Gabor_opencv.csv')

df2.to_csv(r'/home/daniel/Área de Trabalho/Lista_Imagens.csv')