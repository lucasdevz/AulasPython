import os
os.system("cls || clear")
"""
1. Escreva um programa que solicite ao usuário o ano de nascimento.
2. Utilizando uma função, retorne com a idade do usuário.

"""
def calcular_idade(ano_nascimento):
    subtracao = 2024 - ano_nascimento
    idade = subtracao
    return idade

# Entrada

ano_nascimento = int(input("Insira o ano de nascimento: "))
idade = calcular_idade(ano_nascimento)

# Processamento

# Saída

print(f"A sua idade é {idade}: ")