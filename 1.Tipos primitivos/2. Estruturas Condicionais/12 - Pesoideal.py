# Faça um programa que calcule o "peso ideal" de um usuário de acordo com um caractere identificadorde sexo ("M" para masculino ou "F" para feminino) inserido pelo mesmo.
# A fórmula para cada um dos dois casos está definida abaixo.

# Caso "M", utilize a fórmula:
# (72.7 xaltura) - 58

#Caso "F", utilize a fórmula:
# (62.1 x altura) - 44.7

import os
os.system("cls || clear")

peso_ideal = 0

# Solicitando dados

altura = float(input("Digite sua altura"))

sexo = (input("Digite seu sexo(M ou F)"))

# Verificando.

match sexo:
    case "M":
        peso_ideal = (72.7 * altura) - 58
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
    case _:
        print("Opção invalida")
        





