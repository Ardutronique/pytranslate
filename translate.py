from googletrans import *

translator = Translator()
phrase = input("entrer une phrase: ")

def translate():
	#result = translator.translate(phrase, src='fr', dest='en')
	translations = translator.translate(phrase, src='fr', dest='en')
	print(' ',translations.origin, '----->', translations.text)


translate()



	

