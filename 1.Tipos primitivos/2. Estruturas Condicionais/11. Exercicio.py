#Solicite que o usuário informe o valor de um produto e a forma de pagamento.
# 1 - Pagamento à vista;
# 2 - Pagamento à prazo.

# Se o produto for pago à vista aplique um desconto de 10% antes de mostrar o valor final, senão onforme o mesmo valor do produto.
# Se for escolhida a opção de pagamento à prazo, solicite que o usuário digite a quantidade de parcelas que ele deseja pagar. Podendo parcelar em até 6 vezes.
# No final, mostre:

#Se o pagamento for avista:

#Valor do produto: R$ 100,00
#Forma de pagamento: à vista
# Valor do desconto: R$ 10,00
# Total a pagar: R$ 90,00


# Se o pagamento for à prazo:

#Valor do produto: R$ 100,00
#Forma de pagamento: à prazo
#Quantidade de parcelas: 6
# Valor por parcela: R$ 16,66
#Total à prazo: R$ 100,00


import os
os.system("cls || clear")

# Declarando Variáveis

desconto = 0
preco_final = 0
preco_parcelado =0

print("Solicitando dados para o usuário.")
preco_produto = int(input("Digite o valor do produto: "))




