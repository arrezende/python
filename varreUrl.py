#html5lib
'''from selenium import webdriver
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
'''

#LISTAR TODOS OS HEADING TAGS DA PAGINA
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

def url(url,tag):
    #html = urlopen(url)
    req = Request(url=url, headers=headers) 
    tag = tag.split(',')
    html = urlopen(req).read()
    bs = BeautifulSoup(html, "html.parser")
    titles = bs.find_all(tag)
    print('Resultados Obtidos :', *titles, sep='\n\n')


'''def url(url, tag):
	
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
'''