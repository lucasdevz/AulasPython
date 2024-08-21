import os
os.system("cls || clear")

# Entrada

login = input("Digite o login: ")
senha = input("Digite a senha: ")

# Processamento

login_correto = login == "marta" #true
senha_correto = senha == "123" #false




if login_correto and senha_correto:
    print ("Bem-vindo!")

else:
    print("Login ou senha inválidos.")