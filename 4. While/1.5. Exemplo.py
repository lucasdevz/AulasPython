"""
Crie um programa que solicite ao usuário seu login e uma senha.
O programa deve continuar pedindo o login e a senha até que ambos estejam corretos.

"""

import os
os.system("cls || clear")

login_salvo = "Lucas"
senha_salva = "123"

while True:
    login = str(input("Digite seu login: "))
    senha = int(input("Digite sua senha: "))

    if login_salvo == login and senha_salva == senha:
        print("Bem vindo")
    else:break

print("Bem vindo")
    
  