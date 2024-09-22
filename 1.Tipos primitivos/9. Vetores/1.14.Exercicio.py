"""
Altere o algoritmo que acabou de criar e faça com que o usuário insira números inteiros até que seja inserido o número 0.

1. A quantidade de números positivos que são pares.
2. A quantidade de números ímpares;
3. A quantidade de números negativos;
4. A quantidade de números inseridos.

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
    if numero < 0:
             quantidade_negativos += 1
    elif numero > 0:
         quantidade_positivos += 1
    
    elif numero >=0:
        break
    contador += 1

print("Número 0 inserido com sucesso")

print(f"Quantidade de números inseridos: {contador}")

# Saída
for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}° número: {numero} ")


print(f"Quantos são pares: {pares}")
print(f"Quantos são impares: {impares}")
print(f"Quantos são negativos: {quantidade_negativos}")
print(f"Quantos são positivos: {quantidade_positivos}")