#!/usr/bin/python

import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import urllib
import re
import sys

def infoTec(numRDI):
	numero = str(numRDI)

	#print br.response().read()

	r = br.open("http://infoweb.redeinfovias.net.br/acompanharegistro.php?codRegistro="+numero)
	soup = BeautifulSoup(r,"html.parser")

	links = soup.find("textarea", {"class":"registro"})
	tipo = soup.find("span",{"class":"cattitle"})
	for item in links:
		print tipo.get_text()
		print item


#print soup
user = str(sys.argv[1])
senha = str(sys.argv[2])

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("http://infoweb.redeinfovias.net.br/login.php?redirect=index.php")
br.select_form(nr=0)
br.form['username'] = user
br.form['password'] = senha
br.submit()

primeiro = input("Digite o primeiro RDI: ")
ultimo = input("Digite o ultimo RDI: ")
ultimo = ultimo + 1

for num in range(primeiro,ultimo):	
	#print num 
	infoTec(num)
	
