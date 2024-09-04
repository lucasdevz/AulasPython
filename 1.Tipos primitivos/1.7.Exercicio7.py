"""
7. CADASTRO DE USUÁRIO COM CONFIRMAÇÃO DE SENHA

Enunciado:
1. Crie um programa que solicite ao usuário criar uma senha.
2. O programa deve então pedir para confirmar a senha e garantir que ambas as senhas coincidam.
3. Se as senhas não coincidirem, o programa deve continuar pedindo para o usuário inserir e confirmar a  tenha até que ambas sejam iguais.

Dica: Utilize variáveis para armazenar a senha e a confirmação, e um laço while para verificar se as duas senhas coincidem.

"""
import os
os.system("cls || clear")

def cadastrar_usuario():
    while True:
        senha = input("Crie uma senha: ")
        confirmacao = input("Confirme a senha: ")

        if senha == confirmacao:
            print("Senha criada com sucesso!")
            break
        else:
            print("As senhas não coincidem. Tente novamente.")
cadastrar_usuario()



