#!usr/bin/env python3
"""Imprime a tabuada de 1 a 10"""
__version__ = "0.1"
__author__ = "Dvargas"

# base = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))

# for numero in numeros:
# 	print("tabuada do", numero)
# 	for inside_numero in numeros:
# 		print(numero, "x", inside_numero, "=", numero * inside_numero)
# 	print("------------------")

for numero in numeros:
	print("{:-^25}".format(f"Tabuada do {numero}"))
	for inside_numero in numeros:
		resultado = numero * inside_numero
		print("{:^23}".format(f"{numero} x {inside_numero} = {resultado}"))
	print("#" * 25)
	print()