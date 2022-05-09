from bs4 import BeautifulSoup
import requests
from time import sleep

site = requests.get(input('Informe o site conforme o exemplo: "https://www.nomedosite.com" : ')).content

soup = BeautifulSoup(site, 'html.parser')

pref = input('Deseja procurar por algo específico? S/N : ').strip().upper()
if pref == 'S':
    oq = input('O que? ')
    print(soup.find(oq))

else:
    sleep(0.5)
    print('Ok, o conteúdo será exibido por completo...')
    sleep(3)
    print(soup.prettify())