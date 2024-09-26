"""
# CRUD

# CREATE
# READ
# UPDATE
# DELETE

# a = Add

# w = Write

"""


import os
from dataclasses import dataclass

os.system("cls || clear")

# Estrutura de dados.
@dataclass

class Aluno:
    nome: str
    idade: int

QUANTIDADE_ALUNOS = 2
lista_de_alunos = []

for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: "))
    )
    lista_de_alunos.append(aluno)

print("\n===Exibindo dados dos alunos===")
for aluno in lista_de_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"idade: {aluno.idade}")

# definindo arquivo para salvar os dados.

nome_do_arquivo = "Lista_de_alunos_SENAI.txt"

#Abrindo arquivo e definindo que será feita a escrita de dados.

with open(nome_do_arquivo, "a") as arquivo_alunos:
    #Percorrendo vetor/lista.
    for aluno in lista_de_alunos:
        #escrevendo no arquivo uma linha de cada vez
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}\n")

print("dados salvos com sucesso")