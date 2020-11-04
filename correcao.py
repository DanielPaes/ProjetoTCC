from skimage.filters import gabor
from skimage import io
import numpy as np
import pandas as pd

f_m = []
f_a = []
f_e = []
lista_nomes = []
r_c = []
im = []

for i in range(1012, 1851):
    for l in range(0, 56):

        g_real = []
        arr_mean = []
        arr_var=[]
        arr_energy = []

        try:

            caminho = '/home/daniel/PycharmProjects/TCC/Imagens_recortadas/st' + str(i) + '_' + str(l) + '.ppm'
            img = io.imread(caminho)

            im = np.zeros((img.shape[0], img.shape[1]))
            for m in range(0, img.shape[0]):
                for n in range(0, img.shape[1]):
                    (b, g, r) = img[m, n]
                    b = float(b)
                    g = float(g)
                    r = float(r)
                    media_rgb = ((b + g + r) / 3)
                    im[m, n] = media_rgb / 255

            x = str(i) + '_' + str(l)
            print('Filtrando a Imagem st' + x)
            lista_nomes.append(x)

            for t in range(0, 8):
                for f in range(2, 10):
                    filt_real, filt_imag = gabor(im, theta=0.3927 * t, frequency=f / 10)

                    g_real = np.array(filt_real)

                    arr_mean.append(g_real.mean())
                    arr_var.append(g_real.var())
                    arr_energy.append(g_real.sum() * g_real.sum())

            f_m.append(arr_mean)
            f_a.append(arr_var)
            f_e.append((arr_energy))


        except:

            print('erro')


for n in (['M_', 'V_', 'E_']):
    for tr in range(0, 8):
        tc = 0.3927 * tr
        for fr in range(2, 10):
            fc = fr / 10
            r_c.append(n + 'T' + str(tc) + '_F' + str(fc))


df_m = pd.DataFrame(f_m)
df_v = pd.DataFrame(f_a)
df_e = pd.DataFrame(f_e)
df_l = pd.DataFrame(lista_nomes)


df_total = pd.concat([df_m, df_v, df_e], axis=1)
df_total.columns = r_c
df_total['Imagem'] = lista_nomes
df_total = df_total.set_index(['Imagem'])


df_m.to_csv(r'/home/daniel/PycharmProjects/TCC/Features_gabor_MediaRGB/Media.csv')
df_v.to_csv(r'/home/daniel/PycharmProjects/TCC/Features_gabor_MediaRGB/Variancia.csv')
df_e.to_csv(r'/home/daniel/PycharmProjects/TCC/Features_gabor_MediaRGB/Energia.csv')
df_l.to_csv(r'/home/daniel/PycharmProjects/TCC/Features_gabor_MediaRGB/Nomes.csv')
df_total.to_csv(r'/home/daniel/PycharmProjects/TCC/Features_gabor_MediaRGB/Resultado_total.csv')

