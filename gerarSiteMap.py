# -*- coding: utf-8 -*-
import pandas as pd
def openExcel(arquivo):
	x = pd.read_excel(arquivo, encoding = 'utf-8')

	arquivoPhp = open('mapa-do-site.php', 'w', encoding='utf-8')
	arquivoPhp.write(str('<?php \n'))
	texto = []
	for i in x.index:
		novoTexto = str('<li><a href='"{}"'>{}</a></li>'.format(x['URL'][i],x['H1'][i]))
		#novoTexto = str('case "{}": $title= "{}"; $description = "{}"; break;'.format(x['URL'][i],x['H1'][i],x['DESCRIPTION'][i]))
		

		texto = str(texto).strip('[]')
		arquivoPhp.write(novoTexto)
		arquivoPhp.write('\n')		
	print(str('Processado {} linhas').format(i))
		
	arquivoPhp.write(str('\n?>'))
	arquivoPhp.close()
arquivo = 'izamar.xls'
openExcel(arquivo)
