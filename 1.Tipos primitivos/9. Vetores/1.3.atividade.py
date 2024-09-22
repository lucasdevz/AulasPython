"""Você está fazendo parte de uma equipe de desenvolvimento e precisa corrigir um código que um de seus colegas não concluiu. 
O objetivo é criar um algoritmo que leia 5 números inteiros e, em seguida, mostre na tela.
1-A quantidade de números pares e ímpares.
2-A quantidade de números positivos e negativos.
3-A quantidade de números inseridos.
4-O maior e o menor número.
5-A média de números pares.
6-A média de números ímpares.
7-A média de todos os números inseridos.
8-Mostrar os números lidos na ordem inversa.
9-Variáveis para armazenar os números"""

import os
os.system("cls || clear")

# variaveis e contante

lista_numero=[]
QUANTIDADE=5
pares = 0
impares = 0

# Entrada

def ler_numeros(QUANTIDADE):
    for i in range(QUANTIDADE):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        lista_numero.append(numero)
    return lista_numero

def verificador_impar_par(lista_numero):
    pares = 0
    impares = 0
    for numero in lista_numero:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def verificador_media_impar_par(lista_numero):
    quantidade_impares = 0
    soma_impares = 0
    soma_pares = 0
    quantidade_pares = 0
    for numero in lista_numero:
        if numero % 2 == 0:
            quantidade_pares+=1
            soma_pares+=numero
            media_par=soma_pares/quantidade_pares
        elif numero % 2!=0:
            quantidade_impares+=1
            soma_impares+=numero
            media_impar=soma_impares/quantidade_impares
    return media_par,media_impar

def verificador_negativo(lista_numero):
    quantidade_negativos = 0
    for numero in lista_numero:
        if numero<0:
            quantidade_negativos +=1
    return quantidade_negativos

def verificador_positivo(lista_numero):
    quantidade_positivos = 0
    for numero in lista_numero:
        if numero>0:
            quantidade_positivos +=1
    return quantidade_positivos

def maior_menor(lista_numero):
    maior = max(lista_numero)
    menor = min(lista_numero)
    return maior, menor

def media(lista_numero):
    return sum(lista_numero) / len(lista_numero)

# Processamento

lista_numero = ler_numeros(QUANTIDADE)
pares, impares = verificador_impar_par(lista_numero)
media_par,media_impar=verificador_media_impar_par(lista_numero)
quantidade_positivos=verificador_positivo(lista_numero)
quantidade_negativos=verificador_negativo(lista_numero)
maior, menor = maior_menor(lista_numero)
media_numeros = media(lista_numero)
numeros_invertidos = [lista_numero]

# Saída

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Média dos números pares: {media_par:}")
print(f"Média dos números ímpares: {media_impar:}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média de todos os números: {media_numeros:}")
print(f"A quantidade de numeros digitados:{QUANTIDADE}")
for numero in reversed(lista_numero):
        print(f"Números na ordem inversa: {numero}")