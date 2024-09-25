import os
os.system("cls||clear")

print("""
ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖 𝕤𝕖𝕟𝕒𝕚
""")

opcoes = {

    1: "Lasanha",
    2: "Pizza",
    3: "Sushi",
    4: "Feijoada",
    5: "Pastel",
    6: "Bolo",
    7: "Pudim"
}

opcao_escolhida = 0

print("Menu de Pratos:")

for opcao_escolhida, nome in opcoes.items():
    print(f"{opcao_escolhida}: {nome}")

while True:
    try:
        opcao_escolhida = int(input("Digite o código do prato desejado: "))
        if opcao_escolhida in opcoes:
            print(f"Você selecionou: {opcoes[opcao_escolhida]}")
            break
        else:
            print(f"Código inválido! Por favor, tente novamente.")
    except ValueError:
        print(f"Entrada inválida! Por favor, insira um número.")

