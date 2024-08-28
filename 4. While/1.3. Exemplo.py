"""
Escerva um algoritimo que solicite duas notas para um aluno.
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
Calcule e mostre média aritmética do aluno.

"""

import os
os.system("cls || clear")

nota1=0
nota2=0

while True:
        nota1 = float(input("Digite sua primeira nota: "))
        nota2 = float(input("Digite sua segunda nota: "))

        media = float(nota1+nota2)/2

        if nota1>10 or nota1<0 and nota2>10 or nota2<0:
            print("\nDigite sua nota novamente")
        else:
              break
    
print(f"primeira nota: {nota1}")
print(f"primeira nota: {nota2}")
print(f"Média: {media}")
