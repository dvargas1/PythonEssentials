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
__version__ = "0.3"
__author__ = "Dvargas"
__license__ = "Unlicense"
import os
import sys

argumentos = {
	"lang": None,
	"count": 1
}

for args in sys.argv[1:]:
	# TODO: tratar ValueError
	key, value = args.lstrip('-').split("=")
	if key not in argumentos:
		print("Key not in arg docs")
		sys.exit()
	argumentos[key] = value

if argumentos["lang"] == None:
	# TODO: Usar Repeticao
	if "LANG" in os.environ:
		argumentos["lang"] = os.getenv("LANG")[:5]
	else:
		user_language = input("Please choose a language, usage: pt_BR, en_US -> ")
		argumentos["lang"] = user_language

msg = {
		"pt_BR":"Ola Mundo! \n",
		"it_IT":"Ciao Mondo! \n",
		"es_ES":"Hola Mundo! \n",
		"de_DE":"Hallo Welt! \n",
		"fr_FR":"Bonjour le monde! \n",
		"en_US":"Hello World! \n"
}

print(msg[argumentos["lang"]]* int(argumentos["count"]))