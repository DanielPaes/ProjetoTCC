import wget

url_base = 'http://www.ee.oulu.fi/research/imag/wood/WOOD/IMAGES/'

erros_download = []

for i in range(1012, 1851):
    try:
        url = url_base + 'st' + str(i) + '.gz'
        print('\nRealizando o download do arquivo ' + 'st' + str(i) + '.gz')
        wget.download(url, '/home/daniel/Área de Trabalho/UFPR/TCC/Arquivos.gz')
    except:
        erro = 'st' + str(i)
        erros_download.append(erro)
