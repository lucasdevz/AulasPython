"""
5. VERIFICANDO UM CÓDIGO DE PROMOÇÃO
Enunciado:
1. Desenvolva um programa que solicite ao usuário inserir um código de promoção para obter um desconto.
2. O código correto é "PROMO2024".
3. O usuário tem 3 tentativas para acertar o código.
4. Se o código estiver correto, exiba uma mensagem de "Código aceito" e o desconto.
5. Se o usuário errar o código nas 3 tentativas, exiba uma mensagem de "Código inválido".

Dica: Use uma variável para armazenar o código correto e um contador para as tentativas.

"""
import os
os.system("cls || clear")

codigo_correto = "PROMO2024"

maximo_tentativas = 3
tentativas = 0

while tentativas < maximo_tentativas:

    codigo = input("Insira o código de promoção: ")
    if codigo == codigo_correto:
        print("Código aceito! Você obteve um desconto de 10%.")
        break 
    else:
        tentativas += 1
        if tentativas < maximo_tentativas:
            print(f"Código incorreto. Você ainda tem {maximo_tentativas - tentativas} tentativas.")
        else:
            print("Código inválido. Você usou todas as suas tentativas.")
