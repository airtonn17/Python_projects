"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Python Project'
- Aspas duplas -> "Python Project"
- Aspas simples triplas -> '''Python Project'''
"""
# Aspas duplas triplas: """Python Project"""

# Entrada de dados
nome = input("Qual seu nome? ")

print("Seja bem vindo,", nome)

idade = int(input("Qual sua idade? "))

#Processamento

# Sáida de dados
print(nome, "tem", idade, "anos")

"""
# int(idade) => cast
Cast é a "conversão" de um tipo de dado para outro.
"""
print(f"{nome} nasceu em {2024 - idade} anos")

# É possivel fazer dupla atribuição
valor1, valor2 = 1, 44