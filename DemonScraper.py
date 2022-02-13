import os
from bs4 import BeautifulSoup
import requests


basePath = r"DemonSlayerChapters"
os.mkdir(basePath)
for n in range (1,205):
    linkCapitolo = "https://www.readdemonslayerarc.com/demon-slayer-chapter-"+str(n)
    soup = BeautifulSoup(requests.get(linkCapitolo).content,'html.parser')
    os.mkdir(r""+basePath+"/"+linkCapitolo.split('/')[-1])
    immagini = soup.find_all('img')
    immagini.pop(0)
    for immagine in immagini:
        listaImmagini = list()
        links = immagine['src'].split('\t')
        for link in links:
            if(link != 'data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 800 1160%22/%3E'):
                file = open(r""+basePath+"/"+linkCapitolo.split('/')[-1]+"/"+link.split('/')[-1],"wb")
                print("downaloading chapter: "+linkCapitolo.split('/')[-1]+", page: "+link.split('/')[-1])
                file.write(requests.get(link).content)
                file.close()