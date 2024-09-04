"""
6. CALCULADORA DE MÉDIA DE NOTAS

Enunciado:
1. Crie um programa que ajude um estudante a calcular a média de suas notas.
2. O programa deve permitir que o usuário insira notas de provas até que o usuário insira um valor negativo.
3. O programa deve calcular e exibir a média das notas inseridas.

Dica: Use um laço while para continuar solicitando notas até que uma nota negativa seja inserida.
Calcule a média dividindo a soma das notas pelo número de notas.

"""
import os
os.system("cls || clear")

contador = 0

while True:
    nota = int(input("Insira uma nota: "))
    media = float(nota)/2

    if nota>=0:
            print("\nDigite sua nota novamente")
    else:
        break

print(f"Nota inserida: {nota}")
print(f"Média: {media}")
