import os
os.system("cls || clear")

def descontos_salario(salario_bruto):
    
    vale_transporte = 200
    vale_refeicao = 100
    plano_de_saude = 300

salario_bruto = float(input("Digite o valor do seu salário bruto: "))

salario_liquido = descontos_salario(salario_bruto)

print(f"Salario líquido: {salario_liquido}")