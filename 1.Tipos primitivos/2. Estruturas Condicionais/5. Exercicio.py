# Elabore um algoritmo usando operação lógicas para informar se uma pessoa é obrigada a votar. Considere que a regra é que menores de 18 e maiores que 65 

import os
os.system("cls || clear")


# Solicita a idade do usuário

idade = int(input("Digite a sua idade: "))

if idade < 18 or idade > 65:
        print("Não é obrigado a votar.")
else:
        print("É obrigado a votar.")
