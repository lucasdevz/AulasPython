"""
Crie um programa de leia 5 numeros, armazenando em um vetor e informe qual é o menor número e o maior.
Mostre os números informados pelo usuário.
"""
import os
os.system("cls || clear")

# Entrada 
QUANTIDADE_NOTAS = 5
lista_numeros =[]

for i in range(QUANTIDADE_NOTAS):
    numero = float(input(f"Digite o {i+1}° número: "))
    lista_numeros.append(numero)

# Processamento
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)


# Saída
for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}° número: {numero} ")


print(f"\nMenor número: {menor_numero}")
print(f"Maior número: {maior_numero}")