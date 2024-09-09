import os
os.system("cls || clear")
"""
1. Escreva um programa que solicite ao utilizador o fornecimento do seu peso em kg e de sua altura em m.
2. A partir deles, calcule o índice de massa corpórea do utilizador.


"""
def calcular_imc(peso, altura):
    return peso / (altura** 2)

def exibir (imc):
    if imc > 18.5:
        print("Você está abaixo do peso.")
    elif imc >= 18.5 and imc <=24.9:
        print("Peso ideal")
    elif imc >= 25 and imc <=29.9:
        print("Você está com sobre peso")
    elif imc >= 30 and imc <=34.9:
        print("Você está com obesidade grau 1")
    elif imc >= 35 and imc <=39.9:
        print("Você está com obesidade grau 2")
    else:
        print("GRAVE!!! Obesidade grau 3")
    
# Entrada

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
imc = calcular_imc (peso, altura)


# Saída

print(f"Seu indice de massa corporal é: {imc:.2f}")
exibir(imc)
