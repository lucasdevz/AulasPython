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

contador=0

codigo = float(input("Insira um código em promoção: "))
