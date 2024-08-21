import os
os.system("cls || clear")

# Entrada

login = input("Digite o login: ")
senha = input("Digite a senha: ")

# Processamento

if login == "marta" and senha == 123:
    print ("Bem-vindo!")

else:
    print("Login ou senha inválidos.")