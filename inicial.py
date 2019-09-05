# -*- coding: utf-8 -*-
''' Corrigir o bug dos acentos  = It's a bug while trying to print the exactly name in the utf-8 encoding. if you were using python3, you can just git clone the project and remove the decode in google_images_download/google_images_download.py like this:
print(iteration.encode('raw_unicode_escape').decode('utf-8'))
into
print(iteration.encode('raw_unicode_escape'))'''
import downloadImgGoogle
import geraTitleDescription
import varreUrl
import renomearImg
import minificarImg


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
print('[4] Renomear imgs')
escolha = int(input('Qual deseja? '))

if escolha == 0:
	#Fazer o download das imagens
	#Pede as palavras chave
	palavrasChave = str(input('Digite as palavas-chave separadas por virgula: '))
	palavrasChave = palavrasChave.split(',')
	for palavras in palavrasChave: 
		downloadImgGoogle.download(palavras)
		print() 

elif escolha == 1:
	#Gerar title, descripion
	arquivo = input(str('Digite o nome do arquivo "teste.csv": '))
	if arquivo.endswith('.csv'):
		arquivo = arquivo
	else:
		arquivo = str('{}.csv'.format(arquivo))
	geraTitleDescription.openCsv(arquivo)
elif escolha == 2:
	url = input("Digite a url: ")
	tag = input("Digite a tag: ")
	varreUrl.url(url, tag)
elif escolha == 3:
	renomearImg.renomear()
elif escolha == 4:
	minificarImg.compactar()
print('Concluído')