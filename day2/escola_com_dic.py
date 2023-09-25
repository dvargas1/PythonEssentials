#!/usr/bin/env python3
"""Exibe relatorio de criancas por atividade

"""
__version__ = "0.3"
__author__ = "Dvargas"


sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

aulas = {"Ingles":aula_ingles,
				 "Musica":aula_musica,
				 "Danca":aula_danca
}

for aula_name, atividade in aulas.items():
	print("*" * 20)
	print(f"alunos da aula de: {aula_name}")
	from_sala1 = set(sala1) & set(atividade)
	from_sala2 = set(sala2) & set(atividade)
	print(from_sala1)
	print(from_sala2)
	print("-" * 20)
	print()