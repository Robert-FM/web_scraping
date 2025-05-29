import requests
from bs4 import BeautifulSoup as bs4

resposta = requests.get('https://g1.globo.com/')

conteudo = resposta.content

site = bs4(conteudo,'html.parser')

#HTML da notícia
noticia = site.find('div',attrs={'class':'bastian-feed-item'})

#título
titulo = noticia.find('a', attrs={'class': 'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})

print(titulo.text)
#print(noticia.prettify())
