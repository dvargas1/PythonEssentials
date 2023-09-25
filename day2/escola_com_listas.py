#!/usr/bin/env python3
"""Exibe relatorio de criancas por atividade

"""
__version__ = "0.1"
__author__ = "Dvargas"


sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

aulas = [("Ingles",aula_ingles), ("Musica", aula_musica), ("Danca",aula_danca)]

for atividade, tipo in aulas:
	print("*" * 20)
	print(f"Sala de {atividade}")
	from_sala1 = []
	from_sala2 = []
	for aluno in tipo:
		if aluno in sala1:
			from_sala1.append(aluno)
		elif aluno in sala2:
			from_sala2.append(aluno)
	print(from_sala1)
	print(from_sala2)
	print("-" * 20)
	print()