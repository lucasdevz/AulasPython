"""
1. CONTANDO NÚMEROS NEGATIVOS


Enunciado:

1. Desenvolva um programa que conte quantos números negativos foram inseridos pelo usuário usando um laço while.
2.O programa deve parar quando o usuário inserir 0 ou um número positivo.
3. Mostre a quantidade de números negativos.

Dica: Utilize uma variável para contar os números negativos e continue solicitando números até que um número positivo ou 0 seja inserido.

"""

import os
os.system("cls || clear")

contador = 0

while True:
    numero = int(input("Digite um número (0 ou positivo para parar): "))

    if numero >=0:
        break

    contador += 1

print(f"Quantidade de números negativos inseridos: {contador}")