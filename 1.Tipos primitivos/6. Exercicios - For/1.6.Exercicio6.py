import os
os.system("cls || clear")
import time

"""
6. EXIBINDO UMA SEQUÊNCIA
Enunciado: Desenvolva um programa que, com um laço `for`, exiba a sequência de números começando de 10 e decrementando até 1.

Dica: Para decrementar, use uma variável que diminui seu valor a cada iteração do laço.

"""

print("\nLaço de repetição - For")

for i in range(10,0,-1):
    print(f"Número: = {i}")
    time.sleep(2) # Vai esperar 2 segundos.