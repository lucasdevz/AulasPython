"""
Crie um programa de leia 3 notas, armazenando em um vetor e mostre as notas informadas.

"""
import os
os.system("cls || clear")

# Entrada 
QUANTIDADE_NOTAS = 3
lista_notas =[]

for i in range(3):
    nota=float(input("Digite sua nota: "))
    lista_notas.append(nota)

for i, nota in enumerate(lista_notas):
    print(f"{i+1}° nota: {nota} ")