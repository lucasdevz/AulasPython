# Escreva um programa utilizando o comando caso-escolha que imprima um mês do ano de acordo com o número digitado pelo usuário. Exemplo: 1 - Janeiro 2 - Fevereiro 12 -


import os
os.system("cls || clear")

print(""""
      1 - Janeiro
      2 - Fevereiro
      3 - Março
      4 - Abril
      5 - Maio
      6 - Junho
      7 - Julho
      8 - Agosto
      9 - Setembro
      10 - Outubro
      11 - Novembro
      10 - Dezembro
      """)

opcao = float(input("Digite o numero do mês: "))

match opcao:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Mês invalido")



