import pyttsx3
from bs4 import BeautifulSoup
import requests
import sys
import webbrowser
import time
#import keyboard
import sys
from qtido import *



def appel_user():
    entreeSon = input("Entrer un url d'une prod youtube : ")
    entree = input("Entrer un url et une balise séparé d'un espace pour le texte : ")
    entree = entree.split(" ")
    url_source = entree[0]
    balise = entree[1]
    webbrowser.open(entreeSon)

    return url_source, balise


def website(url):
	result = requests.get(url)
	content = result.text
	return(content)

def parse_html(data_html, balise):
	soup = BeautifulSoup(data_html, features="html.parser")
	file = open('texte.txt', 'a', encoding='utf-8')
	for i in soup.find_all(balise):
		resultat = i.string
		if resultat is not None:
			file.write(resultat + '\n')
	file.close

def son(x):
    if x == True:
        engine = pyttsx3.init()
        with open('/home/mars/Bureau/tweetstrump/texte.txt') as f:
            lines = f.read().splitlines()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', 'french')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate+30)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', volume-0.75)
        engine.say(lines)
        engine.runAndWait()

def fenetre():
    f=creer(200,200)
    e=dernier_evenement(f)
    if e==32:
        return(True)



def main():
	url, balise = appel_user()
	html_parse = website(url_source)
	parse_html(html_parse, balise)
    var = fenetre()
    son(var)


main()
