# -*- coding: utf-8 -*-
''' Corrigir o bug dos acentos  = It's a bug while trying to print the exactly name in the utf-8 encoding. if you were using python3, you can just git clone the project and remove the decode in google_images_download/google_images_download.py like this:
print(iteration.encode('raw_unicode_escape').decode('utf-8'))
into
print(iteration.encode('raw_unicode_escape'))'''
from google_images_download import google_images_download 
import csv
#html5lib
from selenium import webdriver
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

import os
print('''
----------Coisas Úteis----------

              _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   \\
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   . |
  `,         """"'     `.              ,'         |   |  ',,|
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\\
   -" /`.         _,'     | _  _  _.|
    ""--'---"""""'        `' '! |! /
                            `" " -'


''')
print('-=-'*30)
print('Selecione a opção desejada:')

print('[0] Fazer download de imagens')
print('[1] Gerar arquivo com TITLE, DESCRIPTION')
print('[2] Buscar uma tag em uma URL')
print('[3] Renomear imgs')
escolha = int(input('Qual deseja? '))

def downloadImgGoogle(key):
	palavrasChave = key
	resposta = google_images_download.googleimagesdownload() 
	padrao = {"keywords": palavrasChave, 
			"format": "jpg", 
			"limit":4, 
			"print_urls":False, 
			"size": "medium",
			"language": "Portuguese",
			"aspect_ratio": "square"
			} 
	try: 
		resposta.download(padrao)
		
	except FileNotFoundError: 
		padrao = {"keywords": palavrasChave, 
					"format": "jpg", 
					"limit":4, 
					"print_urls":False,
					"language": "Portuguese", 
					"size": "medium"} 
					
		# Providing padrao for the searched query 
		try: 
			# Downloading the photos based 
			# on the given padrao 
			resposta.download(padrao) 
			
		except: 
			pass

def openCsv(arquivo):
	with open(arquivo, mode='r') as arquivoCsv:
		leitorCsv = csv.DictReader(arquivoCsv)
		contadorDeLinha = 0
		texto = []

		for linha in leitorCsv:
			if contadorDeLinha == 0:
				contadorDeLinha +=1
			texto.append(str('case "{}": $title= "{}"; $description= "{}"; break;'.format(linha['URL'], linha['TITLE'], linha['DESCRIPTION'])))
			contadorDeLinha += 1

		print(str('Processado {} linhas').format(contadorDeLinha))
	texto = str(texto).strip('[]')
	arquivo = open('novo-arquivo.php', 'w')
	arquivo.write(str('<?php \n'))
	arquivo.write(texto[1:-1])
	arquivo.write(str('\n?>'))
	arquivo.close()

def varreUrl(url, tag):
	
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        res = BeautifulSoup(html.read(),"html5lib")
        #tags = res.findAll("h1", {"class": "titulo-interno"})
        tags = res.findAll(tag)
        for tag in tags:
            #print(tag.getText())
            print(tag)

def renomearImg():
	sequenciaInicial = 1
	novoNome = str(input('digite o novo nome das imagens: '))
	print('Agora digite o endereço onde estão as imagens')
	print('Atenção, é preciso que troque a barra por por /')
	diretorio = input('Digite o endereço: ')

	os.chdir(diretorio)
	sequenciaInicial = 0
	for arquivos in os.listdir():
		if arquivos.endswith('.jpg') or arquivos.endswith('.png'): #verifica se os arquivos são png ou jpg
			sequenciaInicial += 1
			nome_arquivo, extensao_arquivo = os.path.splitext(arquivos) #separa a extensão do nome
			novo_nome_do_arquivo = '{}-{}{}'.format(novoNome,sequenciaInicial,extensao_arquivo) #novo nome gerado
			os.rename(arquivos, novo_nome_do_arquivo) #renomeia os arquivos
	print('imagens renomeadas!!')

if escolha == 0:
	#Fazer o download das imagens
	#Pede as palavras chave
	palavrasChave = str(input('Digite as palavas-chave separadas por virgula: '))
	palavrasChave = palavrasChave.split(',')
	for palavras in palavrasChave: 
		downloadImgGoogle(palavras)
		print() 

elif escolha == 1:
	#Gerar title, descripion
	arquivo = input(str('Digite o nome do arquivo "teste.csv": '))
	openCsv(arquivo)
elif escolha == 2:
	url = input("Digite a url: ")
	tag = input("Digite a tag: ")
	varreUrl(url, tag)
elif escolha == 3:
	renomearImg()
print('Concluído')