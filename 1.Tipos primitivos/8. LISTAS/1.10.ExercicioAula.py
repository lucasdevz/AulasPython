import os
os.system("cls || clear")
"""
1. Escreva um programa que permita ler 2 notas de um aluno e:
2. Informe por meio de uma função a média;
3. Informe por meio de uma função se a média for maior ou igual a 7, o aluno estará aprovado, caso contrario, estará reprovado.

"""
def calcular_media(nota1, nota2):
    soma = nota1 + nota2
    media = soma /2
    return media
def verificar_resultado(media):
    if media >=7:
        return "Aprovado"
    else:
        return "Reprovado"

# Entrada

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
# Processamento
media = nota1 + nota2 /2
resultado = verificar_resultado(media)

media = calcular_media(nota1, nota2)

# Saída
