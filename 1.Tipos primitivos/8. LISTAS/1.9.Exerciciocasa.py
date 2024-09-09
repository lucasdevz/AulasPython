import os
os.system("cls || clear")
"""
Fazer um programa que solicita o preço de um produto e inflaciona esse preço em 10% se sele for menor que 100 e 20% se ele for maior ou igual a 100.
Utilize uma função para obter o resultado solicitado.

# Entrada



"""
# Entrada

def inflacionar_preco(preco):
    if preco < 100:
        preco_inflacionado = preco * 1.10
    else:
        preco_inflacionado = preco * 1.20 
    return preco_inflacionado

preco_original = float(input("Digite o preço do produto: "))
preco_final = inflacionar_preco(preco_original)
print(f"O preço do produto com inflação é: R${preco_final:.2f}")
print("Insira um valor numérico válido.")
