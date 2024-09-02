import os
os.system("cls || clear")

"""
9. CRIANDO UM RETÂNGULO COM ASTERISCOS
Enunciado: Desenvolva um programa que utilize dois laços `for` (um dentro do outro) para imprimir um retângulo de 4 linhas por 6  colunas de asteriscos (`*`).

Dica: Use um laço para cada linha e outro para cada coluna dentro da linha.
"""

# Número de linhas e colunas
num_linhas = 4
num_colunas = 6

for i in range(num_linhas):

    for i in range(num_colunas):
        print('*', end='')
    print()
