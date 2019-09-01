import csv


def openCsv(arquivo):
	arquivoPhp = open('novo-arquivo.php', 'w')
	arquivoPhp.write(str('<?php \n'))
    
	with open(arquivo, mode='r') as arquivoCsv:
		leitorCsv = csv.DictReader(arquivoCsv)
		contadorDeLinha = 0
		texto = []

		for linha in leitorCsv:
			if contadorDeLinha == 0:
				contadorDeLinha +=1
			#texto.append(str('case "{}": $title= "{}"; $description= "{}"; break;'.format(linha['URL'], linha['TITLE'], linha['DESCRIPTION'])))
			novoTexto = str('case "{}": $title= "{}"; $description= "{}"; break;'.format(linha['URL'], linha['TITLE'], linha['DESCRIPTION']))
			contadorDeLinha += 1
			texto = str(texto).strip('[]')
			arquivoPhp.write(novoTexto)
			arquivoPhp.write('\n')		
		print(str('Processado {} linhas').format(contadorDeLinha))
	
	arquivoPhp.write(str('\n?>'))
	arquivoPhp.close()
