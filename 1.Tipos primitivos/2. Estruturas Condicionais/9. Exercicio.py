import os
os.system("cls || clear")

print(""""
    Dias da Semana
    1 - Domingo
    2 - Segunda-feira
    3 - Terça-feira
    4 - Quarta-feira
    5 - Quinta-feira
    6 - Sexta-feira
    7 - Sábado
      """)

opcao = float(input("Digite o dia da semana: "))
match opcao:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("ERROR")

        if opcao <=2 and opcao >=6:
            print("Final de semana")




        
