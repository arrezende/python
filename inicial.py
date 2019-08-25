# -*- coding: utf-8 -*-
from google_images_download import google_images_download 
import csv

print('-=-'*30)
print('Selecione a opção desejada:')

print('[0] Fazer download de imagens')
print('[1] Gerar arquivo com TITLE, DESCRIPTION')
escolha = int(input('Qual deseja? '))

def downloadImgGoogle(key):
	palavrasChave = key
	resposta = google_images_download.googleimagesdownload() 
	print(palavrasChave)
	padrao = {"keywords": palavrasChave, 
			"format": "jpg", 
			"limit":4, 
			"print_urls":False, 
			"size": "medium",
			"aspect_ratio": "square"
			} 
	try: 
		resposta.download(padrao)
	except FileNotFoundError: 
		padrao = {"keywords": palavrasChave, 
					"format": "jpg", 
					"limit":4, 
					"print_urls":False, 
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
			texto.append(str('case "{}": $title: "{}"; $description: "{}"; break;'.format(linha['URL'], linha['TITLE'], linha['DESCRIPTION'])))
			contadorDeLinha += 1

		print(str('Processado {} linhas').format(contadorDeLinha))
	texto = str(texto).strip('[]')
	arquivo = open('novo-arquivo.php', 'w')
	arquivo.write(str('<?php \n'))
	arquivo.write(texto[1:-1])
	arquivo.write(str('\n?>'))
	arquivo.close()

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
	
print('Concluído')