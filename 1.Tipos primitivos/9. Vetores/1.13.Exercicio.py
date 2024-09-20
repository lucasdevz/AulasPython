"""
Crie um algoritmo que leia 5 números inteiros e, em seguida, mostre na tela:

1. A quantidade de números pares e ímpares;
2. A quantidade de números positivos e negativos;
3 - A quantidade de números inseridos.

"""
import os
os.system("cls || clear")

# Entrada

QUANTIDADE_NUMEROS = 5
lista_numeros =[]

pares = 0
impares = 0
quantidade_negativos = 0
quantidade_positivos = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f"Digite o {i+1}° número: "))
    if numero % 2 == 0:
        pares +=1
    else:
        impares +=1

for i in range(QUANTIDADE_NUMEROS):
    if numero < 0:
             quantidade_negativos += 1
    elif numero > 0:
         quantidade_positivos += 1

# Saída
for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}° número: {numero} ")


print(f"Quantos são pares: {pares}")
print(f"Quantos são impares: {impares}")
print(f"Quantos são negativos: {quantidade_negativos}")
print(f"Quantos são positivos: {quantidade_positivos}")