import os
import threading

from bs4 import BeautifulSoup
import requests


def downloadChapterN(n):
    linkCapitolo = "https://www.readdemonslayerarc.com/demon-slayer-chapter-" + str(n)
    soup = BeautifulSoup(requests.get(linkCapitolo).content, 'html.parser')
    path = os.path.join(basePath, linkCapitolo.split("/")[-1])

    if not os.path.exists(path):
        os.mkdir(path)

    immagini = soup.find_all('img')
    immagini.pop(0)

    for immagine in immagini:
        links = immagine['src'].split('\t')
        for link in links:
            path = os.path.join(basePath, linkCapitolo.split("/")[-1], link.split("/")[-1])

            if (
                    link != 'data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 800 '
                            '1160%22/%3E'):
                file = open(path, "wb")
                print("downaloading chapter: " + linkCapitolo.split('/')[-1] + ", page: " + link.split('/')[-1])
                file.write(requests.get(link).content)
                file.close()


basePath = os.path.join(os.getcwd(), "DemonSlayerChapters")

if not os.path.exists(basePath):
    os.mkdir(basePath)

threads = []
for n in range(1, 205):
    threads.append(threading.Thread(target=downloadChapterN, args=(n,), daemon=True))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
