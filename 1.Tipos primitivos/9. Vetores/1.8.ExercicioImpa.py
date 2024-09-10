"""
Crie um programa de leia 6 numeros, armazenando em um vetor e informe quantos são pares e quantos são impares.
Mostre os números informados pelo usuário.

"""
import os
os.system("cls || clear")

# Entrada 
QUANTIDADE_NUMEROS = 6
lista_numeros =[]

pares = 0
impares = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f"Digite o {i+1}° número: "))
    if numero % 2 == 0:
        pares +=1
    else:
        impares +=1

# Saída
for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}° número: {numero} ")


print(f"Quantos são pares: {pares}")
print(f"Quantos são impares: {impares}")