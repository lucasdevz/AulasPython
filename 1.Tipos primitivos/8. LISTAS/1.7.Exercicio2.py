import os
os.system("cls || clear")
"""
Crie uma função que receba um número e mostre uma mensagem informando se o número é par ou impar.

"""
numero = int(input("Digite um número: "))

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

resultado = verificar_par_ou_impar

verificar_par_ou_impar(numero)



