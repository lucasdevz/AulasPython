"""
8. ACOMPANHAMENTO DE METAS DE ESTUDOS
Enunciado:
1. Crie um programa para ajudar o usuário a acompanhar suas metas de estudo.
2. O usuário define uma meta de horas de estudo e o programa deve permitir que o usuário insira o número de horas estudadas até que o total atinja ou exceda a meta.
3. O programa deve  exibir o total de horas estudadas e o valor excedente.

Dica: Utilize um laço while para somar as horas de estudo até atingir a meta.

"""
import os
os.system("cls || clear")

def acompanhar_metas_estudo():
    meta = float(input("Digite sua meta de horas de estudo: "))
   
    total_estudado = 0.0
   
    while total_estudado < meta:
        horas = float(input("Digite o número de horas estudadas atualmente: "))
        total_estudado += horas
   
    excedente = total_estudado - meta
   
    print(f"Total de horas estudadas: {total_estudado:.2f} horas")
    if excedente > 0:
        print(f"Você excedeu a meta em {excedente:.2f} horas.")
    else:
        print("Você atingiu exatamente a meta.")

acompanhar_metas_estudo()



