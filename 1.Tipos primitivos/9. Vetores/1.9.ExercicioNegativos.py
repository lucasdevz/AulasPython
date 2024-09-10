"""
Crie um algoritmo que preencha um vetor com 10 números reais.
Calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.


# Função para preencher o vetor com números reais
def preencher_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        numero = float(input(f"Digite o {i+1}º número real: "))
        vetor.append(numero)
    return vetor

# Função para calcular a quantidade de números negativos e a soma dos positivos
def analisar_vetor(vetor):
    quantidade_negativos = 0
    soma_positivos = 0.0
    
    for numero in vetor:
        if numero < 0:
            quantidade_negativos += 1
        elif numero > 0:
            soma_positivos += numero
    
    return quantidade_negativos, soma_positivos

# Main
def main():
    tamanho_vetor = 10
    vetor = preencher_vetor(tamanho_vetor)
    quantidade_negativos, soma_positivos = analisar_vetor(vetor)
    
    print(f


"""
import os
os.system("cls || clear")

# Entrada 
QUANTIDADE_NUMEROS = 10
lista_numeros =[]

quantidade_negativos = 0
soma_positivos = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f"Digite o {i+1}° número: "))
    if numero < 0:
             quantidade_negativos += 1
    elif numero > 0:
         soma_positivos += numero

# Saída
for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}° número: {numero} ")


print(f"Quantos são negativos: {quantidade_negativos}")
print(f"Soma Positivos: {soma_positivos}")