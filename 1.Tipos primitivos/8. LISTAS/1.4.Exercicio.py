import os
os.system("cls || clear")

"""
Crie uma função que receba 2 números e usando uma função, mostre uma mensagem com a media destes dois numeros informados
"""
def calcular_media(primeiro_numero, segundo_numero):
    soma = primeiro_numero + segundo_numero /2
    resultado = soma /2
    return resultado

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite o segundo número: "))

media = calcular_media(primeiro_numero, segundo_numero)

print(f"Sua média é: {media}")