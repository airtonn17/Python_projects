"""
Tipo String

Em Python um dado é considerado do tipo String sempre que:

- Estiver entre aspas simples -> 'uma string'
- Estiver entre aspas duplas -> "uma string"
- Estiver entre três aspas simples -> '''uma string'''
"""
# Estiver entre três aspas triplas -> """uma string"""

nome = 'Pyhton Project'
nome = "Python's Project"
nome = "Python \n Project" # Pula uma linha
nome = "Python \" Project" # Caractere de Escape -> Barra invertida

print(nome)
print(type(nome))

print(nome.upper()) # Letras maiusculas
print(nome.lower()) # Letras Minusculas
print(nome.split()) # Cria listas

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11, 12,  13]
# ['P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'j', 'e', 'c', 't']
nome = 'Python Project'
print(nome[0:5]) # Slice de String -> '0' é o primeiro string e '5' n é impresso.

print(nome.split()[0])

"""
[::-1] -> Comece do primeiro elemento, vá até o ultimo elemento e inverta.
"""
print(nome[::-1]) # Inverte a ordem dos dtrings

print(nome.replace('j', 'g')) # Substitue um string por outro escolhido

print(type(nome))

print('socorram me subino onibus em marrocos') # Palindromo
print('socorram me subino onibus em marrocos'[::-1])