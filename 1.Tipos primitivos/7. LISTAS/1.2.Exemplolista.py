import os
os.system("cls || clear")

print("""


░██████╗███████╗███╗░░██╗░█████╗░██╗
██╔════╝██╔════╝████╗░██║██╔══██╗██║
╚█████╗░█████╗░░██╔██╗██║███████║██║
░╚═══██╗██╔══╝░░██║╚████║██╔══██║██║
██████╔╝███████╗██║░╚███║██║░░██║██║
╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝

""")

# Função com retorno
def somar(n1, n2):
    soma = n1 + n2
    return soma
    
primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

soma = somar(primeiro_numero, segundo_numero)

print(f"soma: {soma}")