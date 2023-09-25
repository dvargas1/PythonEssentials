#!/usr/bin/env python3
"""hello.py

Dependendo da linguagem configurada no ambiente, o programa exibe a classsica
mensagem "Hello World".

Como usar:

Tenha a variavel LANG configurada:
		export LANG=pt_BR

Execute:
	python3 hello.py
	ou
	./hello.py
"""
#Dunders
__version__ = "0.2"
__author__ = "Dvargas"
__license__ = "Unlicense"
import os 

current_language = os.getenv("LANG", "en_US")[:5]
msg = {
		"pt_BR":"Ola Mundo!",
		"it_IT":"Ciao Mondo!",
		"es_ES":"Hola Mundo!",
		"de_DE":"Hallo Welt!",
		"fr_FR":"Bonjour le monde!",
		"en_US":"Hello World!"
}

print(msg[current_language])