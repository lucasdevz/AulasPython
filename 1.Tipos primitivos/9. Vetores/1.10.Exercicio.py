"""
Crie um algoritmo que receba do usuário valores e armazene em um vetor 5 números.
Caso seja infotmado um valor negativo, atribua o valor 0.
Liste os valores do vetor.
def ler_valores():
    valores = []
    while len(valores) < 6:
        try:
            valor = int(input("Digite um valor inteiro positivo e par: "))
            if valor > 0 and valor % 2 == 0:
                valores.append(valor)
            else:
                print("O valor deve ser inteiro, positivo e par. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um valor inteiro.")
    return valores

def main():
    valores = ler_valores()
    print("Valores na ordem inversa:")
    for valor in reversed(valores):
        print(valor)

if __name__ == "__main__":
    main()

"""
import os
os.system("cls || clear")

vetor = []

for i in range(5):
    valor = float(input("Digite um número: "))
    if valor < 0:
        vetor.append(0)
    else:
        vetor.append(valor)

# Saída
print("Valores do vetor:", vetor)
