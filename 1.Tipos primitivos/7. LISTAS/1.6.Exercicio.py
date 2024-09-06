import os
os.system("cls || clear")
"""
1. Crie funções que recebam 2 números e retorne a soma, subtração, divisão e a multiplicação destes dois números informados.
Obs.: Crie uma função para cada operação.



"""
# Funções:

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        return "Erro: Divisão por zero não permitida."
    return n1 / n2

# Entrada

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# Processamento
soma = somar (n1,n2)
subtracao = subtrair (n1,n2)
multiplicacao = multiplicar (n1,n2)
divisao = dividir (n1,n2)

# Saida

print(f"Soma:", {soma})
print(f"Subtração:", {subtracao})
print(f"Multiplicação:", {multiplicacao})
print(f"Divisão:", {divisao})
