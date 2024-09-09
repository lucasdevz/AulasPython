import os
os.system("cls || clear")
"""
Crie um programa que leia 6 numeros e informe por meio de uma função:
Quantos numeros são pares;
Quantos numeros são impares.

"""
def verificar_pares_impares():
    pares=0
    impares=0

    for i in range(6):
           numero = int(input("Digite um número: "))
           if numero % 2 == 0:
            pares +=1
            else:
            impares +=1

print(f"Quantidade pares: {pares})
print(f"Quantidade impares: {impares})