"""
Crie um programa de leia 4 notas, armazenando em um vetor e calcule a média aritmética.
verifique a situação do aluno considerando:
1. Média maior ou igual a 7: Aprovado.
2. Média maior igual a 5: Recuperação
3. Média menor que 5: Reprovado.

Mostre as 4 notas informadas pelo usuário e informe a média.
"""
import os
os.system("cls || clear")

# Entrada 
QUANTIDADE_NOTAS = 4
lista_notas =[]

for i in range(QUANTIDADE_NOTAS):
    nota=float(input("Digite sua nota: "))
    lista_notas.append(nota)

# Processamento
soma = sum(lista_notas)
media= soma/QUANTIDADE_NOTAS

if media >=7:
    print("Aprovado")
elif media >=5:
    print("Recuperação")
else:
    print("Reprovado")

# Saída
for contador, nota in enumerate(lista_notas):
    print(f"{contador+1}° nota: {nota} ")


print(f"media: {media}")