import os
os.system("cls || clear")

# Solicitando dados
numero = int(input("Digite um número para tabuada: "))

print(f"\nTabuada de multiplicação do número: {numero} ")

for i in range (7,11):
    print(f"{numero} * {i} = {numero * i}")

