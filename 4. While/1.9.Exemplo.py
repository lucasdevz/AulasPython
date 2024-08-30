import os
os.system("cls || clear")

soma = 0
contador = 0

while True:
    nota = float(input("Digite sua nota: "))
    contador +=1
    soma += nota

    resposta = input("Deseja inserir mais uma nota? ").upper()
    # resposta = resposta.upper() # Converter Maiusculo

    if resposta =="N":
        break

media = soma /contador
print(f"Média: {media}")