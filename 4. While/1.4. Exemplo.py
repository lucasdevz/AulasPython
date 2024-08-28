"""
Escerva um algoritimo que solicite duas notas para um aluno.
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
Calcule e mostre média aritmética do aluno.

"""

import os
os.system("cls || clear")


QUANTIDADE_NOTAS = 3 #Constante
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite {i+1}° nota: "))

        if nota >= 0 and nota <=10:
            break
        soma += nota

        media = soma/ QUANTIDADE_NOTAS

        print(f"Média: {media}")
