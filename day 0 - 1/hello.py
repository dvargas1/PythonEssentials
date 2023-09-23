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
__version__ = "0.1"
__author__ = "Dvargas"
__license__ = "Unlicense"
import os

current_language = os.getenv("LANG", "en_US")
msg = "Hello World!"

if current_language[:5] == "pt_BR":
	msg = "Olá Mundo!"
elif current_language[:5] == "it_IT":
	msg = "Ciao Mondo!"
elif current_language[:5] == "es_ES":
	msg = "Hola Mundo!"
elif current_language[:5] == "de_DE":
	msg = "Hallo Welt!"
elif current_language[:5] == "fr_FR":
	msg = "Bonjour le monde!"



print(msg)