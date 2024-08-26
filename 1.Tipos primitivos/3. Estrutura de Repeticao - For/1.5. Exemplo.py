import os
os.system("cls || clear")

soma = 0

for i in range(3):
    nota = float(input("Digite uma nota: "))
    soma = soma + nota

    media = soma /3

    if nota >=7:
        print("Aprovado")

    elif nota >=4: #else in
        print("Recuperação")
    else:
        print("Reprovado")

        print("=== FIM ===")

