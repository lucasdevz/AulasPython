import os
os.system("cls || clear")

# Declarando variáveis.

login_salvo = "marta"
senha_salvo = "123"

# Entrada

login = input("Digite o login: ")
senha = input("Digite a senha: ")

# Processamento

if login == login_salvo and senha_salvo == 123:
    print ("Bem-vindo!")

else:
    print("Login ou senha inválidos.")