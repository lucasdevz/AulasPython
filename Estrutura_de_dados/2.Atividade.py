import os
from dataclasses import dataclass

os.system("cls || clear")

# Estrutura de dados.
@dataclass

class Cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_ALUNOS = 4
lista_carteiras = []

for i in range(QUANTIDADE_ALUNOS):
    
    cliente = Cliente(
        nome = input("Digite sua carteira: "),
        idade = int(input("Digite sua idade: "))
    )
    lista_carteiras.append(cliente)

print("\n===Exibindo dados dos alunos===")
for aluno in lista_carteiras:
    print(f"Nome: {aluno.nome}")
    print(f"idade: {aluno.idade}")

# Salvar em um arquivo chamado: carteira_de_clientes.txt

# definindo arquivo para salvar os dados.
nome_do_arquivo = "carteira_de_clientes.txt"

# Fazer leitura de dados do arquivo carteira_de_clientes.txt e mostre no terminal.

#Abrindo arquivo e definindo que será feita a escrita de dados.

with open(nome_do_arquivo, "w") as arquivo_clientes:
    #Percorrendo vetor/lista.
    for cliente in lista_carteiras:
        #escrevendo no arquivo uma linha de cada vez
        arquivo_clientes.write(f"{cliente.nome}, {cliente.idade}\n")

print("dados salvos com sucesso")
