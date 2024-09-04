"""
2. ENCONTRANDO O PRIMEIRO NÚMERO DIVISÍVEL POR 7

Enunciado:

1. Escreva um programa que use um laço while para encontrar o primeiro número maior que 50 que seja divisível por 7.

2. Exiba esse número.

Dica: Inicie com uma variável em 51 e use o operador % para verificar divisibilidade por 7. Continue até encontrar um número que satisfaça a condição.

"""

import os
os.system("cls || clear")

# Inicio
numero = 51

# Processamento

while True:
    if numero % 7 == 0:
        print(f"O primeiro número maior que 50 que é divisível por 7 é: {numero}")
        break
    # Saida
    numero += 1
