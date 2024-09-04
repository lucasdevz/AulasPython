"""
4. CONTROLE DE GASTOS MENSAIS
Enunciado:
1. Crie um programa que ajude um usuário a controlar seus gastos mensais.
2. O programa deve permitir que o usuário insira gastos diários até que o total gasto no mês exceda um orçamento inicial fornecido.
3. O programa deve exibir o total gasto e o valor  excedente.

Dica: Defina um orçamento e use um laço while para somar os gastos diários. Pare quando o total gasto exceder o orçamento.

"""
import os
os.system("cls || clear")

orcamento = float(input("Digite o orçamento inicial para o mês: "))
total_gasto = 0.0
numero_gastos = 0

while total_gasto <= orcamento:
    gasto_diario = float(input("Digite um gasto diário: "))
    total_gasto += gasto_diario

    numero_gastos += 1

excedente = total_gasto - orcamento

print(f"Total gasto no mês: R${total_gasto:.2f}")
print(f"Valor excedente: R${excedente:.2f}")
