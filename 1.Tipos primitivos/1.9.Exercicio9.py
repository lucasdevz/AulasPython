"""
9. CADASTRO DE NÚMEROS ÍMPARES E CONTAGEM
Enunciado:
1. Crie um programa que peça ao usuário para inserir números inteiros até que a soma dos números ímpares inseridos seja maior que 200.
2. O programa deve exibir o total de números ímpares inseridos e a soma desses números. 

Dica: Utilize um laço while para somar os números ímpares e contar quantos foram inseridos. Pare quando a soma exceder 200.

"""
import os
os.system("cls || clear")

soma = 0
contador = 0

while soma <= 200:
    numero = int(input("Digite um número inteiro: "))
   
    if numero % 2 != 0:
        soma += numero
        contador += 1

print(f"Total de números ímpares inseridos: {contador}")
print(f"Soma dos números ímpares: {soma}")


