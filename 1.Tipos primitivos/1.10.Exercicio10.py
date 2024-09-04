"""
10. ACOMPANHAMENTO DE REFEIÇÕES EM UM PLANO DE DIETA
Enunciado:
1. Crie um programa que permita ao usuário registrar o número de calorias consumidas em cada refeição.
2. O programa deve continuar registrando as calorias até que o total de calorias consumidas ultrapasse 2000 calorias.
3. Após exceder 2000 calorias, exiba o total de calorias consumidas e o excesso.

Dica: Use um laço while para somar as calorias e parar quando o total for maior que 2000. Exiba o total e o excesso de calorias.

"""
import os
os.system("cls || clear")

def acompanhamento_refeicoes():
    total_calorias = 0
   
    while total_calorias <= 2000:
        try:
            calorias = float(input("Digite o número de calorias consumidas: "))
            total_calorias += calorias
        except ValueError:
            print("Por favor, digite um número válido.")
   
    excesso = total_calorias - 2000
    print(f"Total de calorias consumidas: {total_calorias:.2f}")
    print(f"Excesso de calorias: {excesso:.2f}")

acompanhamento_refeicoes()

