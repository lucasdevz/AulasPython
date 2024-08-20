# Elabore um algoritmo para ler o nome de um aluno, sua idade e as três notas. Calcular a média do aluno. Caso a média do aluno seja menor que 7, o aluno está reprovado.
# Mostrar: nome, idade, media e se está aprovado ou reprovado.

import os
os.system("cls || clear")

# Entrada

nome = input ("Digite seu nome: ")
idade = int(input ("Digite sua idade: "))

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Media

media = (nota1 + nota2 + nota3)/3

# Processamento

if media >=7:
    print (f"Aprovado!")

else:
     print (f"Reprovado!")



