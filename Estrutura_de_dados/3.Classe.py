import os
from dataclasses import dataclass

# Limpa terminal

os.system("cls || clear")

# Criando uma estrutura de dados do tipo classe
@dataclass
class Aluno:
    nome: str
    idade: int
    media: float

# Criando lista de alunos.
lista_de_alunos = []

# Entrada de dados.
for i in range(2):
    print(f"\nSolicitando dados do {i+1}° aluno.")

    # Os dados solicitado abaixo serão solicitados para cada aluno.
    aluno = Aluno(
        nome = input("Digite o nome: "),
        idade = int(input("Digite a idade: ")),
        media = float(input("Digite a média:")) 
    )
    lista_de_alunos.append(aluno)

    # Processamento.

    lista_idades = []

    for aluno in lista_de_alunos:
        lista_idades.append(aluno.idade)

    soma_idades =sum(lista_idades)
    
    quantidade_mulheres =sum(1 for habitante in lista_habitantes if habitante ["genero"] == "Feminino" and habitante [salario] >=5000 ) 

    # Saída de dados.
    print("\nExibindo dados.")

    # Usando um ForEach para percorrer a lista
    # e mostrar os dados de cada aluno inserido na lista.
    for aluno in lista_de_alunos:
        print(f"Nome: {aluno.nome}")
        print(f"Idade: {aluno.idade}")
        print(f"Média: {aluno.media}")
        print()
        
