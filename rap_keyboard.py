import pyttsx3
from bs4 import BeautifulSoup
import requests
import sys
import webbrowser
import time
from pynput import keyboard
#youtube dl

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

def main():
	entree = input("Entrer un url et une balise séparé d'un espace pour le texte : ")
	entree = entree.split(" ")
	url_source = entree[0]
	balise = entree[1]
	html_parse = website(url_source)
	parse_html(html_parse, balise)

if __name__ == "__main__" :
	main()

entreeSon= input("Entrer un url d'une prod youtube : ")
webbrowser.open(entreeSon)
engine = pyttsx3.init()
with open('/home/mars/Bureau/tweetstrump/texte.txt') as f:
        lines = f.read().splitlines()
        #time.sleep(25)

def set_engine():
	voices = engine.getProperty('voices')       #getting details of current voice
	engine.setProperty('voice', 'french')
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate+30)
	volume = engine.getProperty('volume')
	engine.setProperty('volume', volume-0.75)

def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def on_press(key):
    key_name = get_key_name(key)
    if key_name == "Key.space":
        engine.say(lines)
        engine.runAndWait()

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()
