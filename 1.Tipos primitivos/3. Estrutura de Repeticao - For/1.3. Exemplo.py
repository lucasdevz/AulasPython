import os
os.system("cls || clear")

for i in range(5):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")