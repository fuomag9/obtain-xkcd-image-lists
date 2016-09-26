import requests
import base64
import os
import urllib.request
import mmap
import os.path
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
def get_html(website):
   req = urllib.request.Request(website, headers={'User-Agent': 'Mozilla/5.0'})
   html = urllib.request.urlopen(req).read()
   soup= BeautifulSoup(html, 'html.parser')
   return soup
elenco_siti=[]
elenco_siti_corretto=[]
immagini=[]
immagini_corrette=[]
file=os.getcwd()+"/pls.txt"
for link in get_html("http://xkcd.com/archive/").find_all('a'):
    elenco_siti.append(link.get('href'))
for x in range(0,len(elenco_siti)):
    if "." not in elenco_siti[x]:
        elenco_siti_corretto.append(elenco_siti[x])
print(elenco_siti_corretto)
for x in range(3,len(elenco_siti_corretto)):
 try:
    for link in get_html("http://xkcd.com"+elenco_siti_corretto[x]).find_all('img'):
     immagini.append(link.get('src'))
     print(str(x)+"/"+str(len(elenco_siti_corretto)))
 except urllib.error.HTTPError:
        pass 
for x in range(0,len(immagini)):
    if "/s/" not in immagini[x]:
        immagini_corrette.append(immagini[x])
        print(str(x)+"/"+str(len(immagini)))
immagini=[]
for x in range(0,len(immagini_corrette)):
    if "static" not in immagini_corrette[x]:
        immagini.append(immagini_corrette[x])
        print(str(x)+"/"+str(len(immagini_corrette)))
with open(file, 'w') as f:
    for s in immagini:
        f.write("http:"+s + '\n')