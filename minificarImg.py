import tinify
import os

def compactar():
    tinify.key = 'ddDiKafu3pSnpCHuqWObb7eoAfD6NZFW'
    print('Digite o endereço onde estão as imagens')
    diretorio = input('Digite o endereço: ')
    os.chdir(r'''{}'''.format(diretorio))
    sequenciaInicial = 0
    for arquivos in os.listdir():
        if arquivos.endswith('.jpg') or arquivos.endswith('.png'): #verifica se os arquivos são png ou jpg
            sequenciaInicial += 1
            origem = tinify.from_file(arquivos)
            origem.to_file('minificadas-{}'.format(arquivos))
    print('imagens Compactadas!!')