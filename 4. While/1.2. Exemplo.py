import os
os.system("cls || clear")

while True:
    nota = float(input("Digite a nota do aluno (entre 0 e 10): "))

    if nota < 0 or nota > 10:
        print("\nA nota deve ser maior que 0 e menor que 10")
    else:
        break #Para o laço de repetição

    print(f"nota: {nota}")

            
