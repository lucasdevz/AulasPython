import os
os.system("cls || clear")
"""
1. Faça um programa que imprime a tabuada de um numero informado pelo usuario de 1 a 10.
2. Utilize uma funçao para exibir o resultado.

"""
# Processsamento
def mostrar_tabuada(numero):
    for i in range(10):
        print(f"{numero} x {i} = {numero * i}")

# Entrada

numero = int(input("Digite um número: "))


# Saída
mostrar_tabuada(numero)
