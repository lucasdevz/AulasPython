"""
Crie um programa de leia 3 notas, armazenando em um vetor e mostre as notas informadas.
"""
import os
os.system("cls || clear")

# Entrada 
QUANTIDADE_NOTAS = 3
lista_notas =[]

for i in range(QUANTIDADE_NOTAS):
    nota=float(input("Digite sua nota: "))
    lista_notas.append(nota)

# Processamento
soma = sum(lista_notas)
media= soma/QUANTIDADE_NOTAS

# Saída
for contador, nota in enumerate(lista_notas):
    print(f"{contador+1}° nota: {nota} ")


print(f"media: {media}")