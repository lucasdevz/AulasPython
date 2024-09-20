"""
1. Crie um algoritmo que aceite apenas 6 valores inteiros, positivos e pares.
2. Em seguida, mostre na tela os valores lidos na ordem inversa.
3. Caso seja informado um número diferente dos critérios apresentados acima, repita a pergunta para o usuário.
"""
import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 3
lista_pares_positivos = []


def solicitar_numero():
    for i in range(QUANTIDADE_NUMEROS):
        while True:
            numero = int(input("Digite um número"))

            if numero % 2 == 0 and numero > 0:
                lista_pares_positivos.append(numero)
                break
            else:
                print("Numero invalido")
                
    return lista_pares_positivos

#Entrada
print("nSolicitando Dados")
lista_numeros = solicitar_numero()

#Saída
for i, numero in enumerate(reversed(lista_numeros)):
    print(f"{len(lista_numeros)} {i} {numero}")