#html5lib
from selenium import webdriver
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def url(url, tag):
	
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