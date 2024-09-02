import os
os.system("cls || clear")

"""
10. SOMA DOS NÚMEROS ÍMPARES
Enunciado: Escreva um programa que calcule a soma dos números ímpares de 1 a 9 utilizando um laço `for`.

Dica: Verifique
se um número é ímpar usando o operador `%` e adicione esses números a uma
variável de soma.

"""

soma = 0

for i in range(1,10):
    numeros = float(input("Digite um número: "))
    if numeros % 1 == 0:
        soma = soma + numeros

    print(f"Soma: {soma}")