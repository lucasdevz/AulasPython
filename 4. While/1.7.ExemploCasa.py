"""
Escreva um algoritmo que leia três notas de um aluno. Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente. Após receber as notas dentro dos parâmetros acima, calcule a média e verifique se o aluno está aprovado, recuperação ou reprovado considerando os seguintes critérios:
Se a média for a partir de 7, aprovado;
Se a média for entre 5 e 6.9, o aluno está em recuperação;
Caso seja menor que 5, o aluno está reprovado.

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