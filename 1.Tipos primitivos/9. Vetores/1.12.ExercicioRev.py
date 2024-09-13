"""
1. Crie um algoritmo que aceite apenas 6 valores inteiros, positivos e pares.
2. Em seguida, mostre na tela os valores lidos na ordem inversa.
3. Caso seja informado um número diferente dos critérios apresentados acima, repita a pergunta para o usuário.
"""
import os
os.system("cls || clear")

valores = []

while len(valores) < 6:
        try:
            valor = int(input("Digite um valor inteiro positivo e par: "))
            if valor > 0 and valor % 2 == 0:
                valores.append(valor)
            else:
                print("O valor deve ser inteiro, positivo e par. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um valor inteiro.")
            print(valores)

print("\nExibindo os números na ordem inversa: ")
for valor in reversed(valores):
    print(valor)