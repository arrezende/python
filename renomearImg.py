import os

def renomear():
	sequenciaInicial = 1
	novoNome = str(input('digite o novo nome das imagens: '))
	print('Agora digite o endereço onde estão as imagens')
	diretorio = input('Digite o endereço: ')
	os.chdir(r'''{}'''.format(diretorio))
	sequenciaInicial = 0
	for arquivos in os.listdir():
		if arquivos.endswith('.jpg') or arquivos.endswith('.png'): #verifica se os arquivos são png ou jpg
			sequenciaInicial += 1
			nome_arquivo, extensao_arquivo = os.path.splitext(arquivos) #separa a extensão do nome
			novo_nome_do_arquivo = '{}-{}{}'.format(novoNome,sequenciaInicial,extensao_arquivo) #novo nome gerado
			os.rename(arquivos, novo_nome_do_arquivo) #renomeia os arquivos
	print('imagens renomeadas!!')
