import os
os.system("cls || clear")
import time

"""
2. SOMANDO NÚMEROS

Enunciado: Crie um programa que, utilizando um laço `for`, calcule a soma dos números de 1 a 5 e mostre o resultado.

Dica: Você pode criar uma variável para armazenar a soma e adicionar a ela o valor de cada número a cada iteração.

"""


soma = 0

for i in range(5):
    numeros = float(input("Digite um número: "))
    soma = soma + numeros

    print(f"Soma: {soma}")
