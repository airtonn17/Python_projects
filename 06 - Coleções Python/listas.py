"""
Listas (list)

Listas em python, funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possue tamanho fixo:
Ou seja, podemos criar a lista e simplesmente ir adicionando os elementos;
- Qualquer tipo de dado: Não possuem tipo de dao fixo:
Ou seja, podemos colocar qualquer tipo de dado;

As listas em python são representadas por colchetes: []

Listas são mutáveis: Ou seja, elas podem mudar constantemente.
"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'j', 'e', 'c', 't']
litsa3 = []
lista4 = list(range(11))
lista5 = list('Pytho Project')

"""
 Buscar Elementos na lista
"""
# if [8, 3, 1] in lista1:
#     print('Encontrei a lista')
# else:
#     print('Não encontrei a lista')

"""
 Podemos facilmente checar se determinado valor está contido na lista
"""
# num = 7

# if num in lista4:
#     print(f'Encontrei o número {num}')
# else:
#     print(f'Não encontrei o número {num}')

"""
 Ordenar uma lista
"""
# lista1.sort()
# print(lista1)

"""
 Contar o número de ocorrências de um valor em uma lista.
"""
# print(lista1.count(1))
# print(lista5.count('t'))

"""
 Adicionar elementos em lista
"""
# Forma 1 - Apend
# OBS: Com o append nós só conseguimos adicionar 1 elemento por vez

# print(lista1)
# lista1.append(42)
# print(lista1)

# lista1.append(12, 34, 56) # Erro

# lista1.append([8, 3, 1]) # Adiciona uma lista como elemento único (sub lista)
# print(lista1)

# Forma 2 - Extend
# OBS: Adiciona cada elemento na lista como valor adicional a lista

# lista1.extend([123, 44, 67])
# print(lista1)

"""
 Inserir um novo elemento na lista informando a posição do índice
"""
# OBS: Isso não substitue o valor inicial. O mesmo será deslocado para a direita da lista.
# lista1.insert(2, 'novo valor')
# print(lista1)

"""
 Juntar duas listas
"""
# lista6 = lista1 + lista2
# print(lista6)

"""
 Inverter uma lista
"""
# Forma 1
# lista1.reverse()
# lista2.reverse()
# print(lista1)
# print(lista2)

# Forma 2
# print(lista1[::-1])
# print(lista2[::-1])

"""
 Copiar uma lista
"""
# lista6 = lista2.copy()
# print(lista6)

"""
 Contar quantos elementos existem dentro da lista
"""
# print(len(lista1))

"""
 Remover o último elemento de uma lista
"""
# OBS: O pop não somente remove o último elemento, mas também o retorna

# print(lista5)
# lista5.pop()
# print(lista5)

# Podemos remover um elemento pelo índice

# OBS: Os elementos serão descocados para a esquerda.
# OBS: Se não houver elemento no índice informado, teremos o erro IndexError.
# lista5.pop(2)
# print(lista5)

"""
 Remover todos os elementos (zerar a lista)
"""
# print(lista5)
# lista5.clear()
# print(lista5)

"""
 Repetir elementos em uma lista
"""
# nova = [1, 2, 3]
# print(nova)
# nova = nova * 3
# print(nova)

"""
 Converter uma String para uma lista
"""
# Exemplo 1

# curso = 'Pytho Project Airton Cavalcante'
# print(curso)
# curso = curso.split()
# print(curso)

#OBS: Por padrão o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2

# curso = 'Python,Project,Airton,Cavalcante'
# print(curso)
# curso = curso.split(',') # Definindo uma String como separador
# print(curso)

"""
 Convertendo uma lista em uma String
"""
# lista6 = ['Python', 'Project', 'Airton', 'Cavalcante']
# print(lista6)

## Adiciona espaço entre cada elemento na lista e transforma em uma String
# curso = ' '.join(lista6)
# print(curso)

"""
 Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
"""
# lista6 = [1, 2.34, True, 'Python', 'd', [1, 2, 3], 45345345345]
# print(lista6)
# print(type(lista6))

""""
 Iterando sobre listas
"""
# Exemplo 1 - Utilizando for

# soma = 0
# for elemento in lista1:
#     print(elemento)
#     soma = soma + elemento
# print(soma)

# Exemplo 2 - Utilizando while

# carrinho = []
# produto = ''
# while produto != 'sair':
#     produto = input("Adicione um produto na lista ou digite 'sair' para sair: ")
#     if produto != 'sair':
#         carrinho.append(produto)
#
# for produto in carrinho:
#     print(produto)

"""
 Ultilizando variáveis em listas
"""
# numeros = [1, 2, 3, 4, 5]
# print(numeros)
#
# num1 = 1
# num2 = 2
# num3 = 3
# num4 = 4
# num5 = 5
# numeros = [num1, num2, num3, num4, num5]
# print(numeros)

"""
 Fazemos acesso aos elementos de forma indexada
"""
##           0         1         2        3
# cores = ['verde', 'amarelo', 'azul', 'branco']
#
# print(cores[0]) # verde
# print(cores[1]) # amarelo
# print(cores[2]) # azul
# print(cores[3]) # branco
#
# # Fazer acesso aos elementos de forma indexada inversa
# # O final de um elemento está ligado ao início da lista
# print(cores[-1]) # brando
# print(cores[-2]) # azul
# print(cores[-3]) # amarelo
# print(cores[-4]) # verde
# # print(cores[-5]) # Erro, pois não existe índice -5

"""
Gerar índice em um for
"""
# for indice, cor in enumerate(cores):
#     print(indice, cor)

## Listas aceitam valores repetidos
# lista = []
# lista.append(42)
# lista.append(42)
# lista.append(33)
# lista.append(33)
# lista.append(42)
# print(lista)

# Outros métodos não tão importantes, mas também uteis

# #encontrar o índice de um elemento na lista
# numeros = [5, 6, 7, 5, 8, 9, 10]
# # Em qual índice da lista está o valor 6?
# print(numeros.index(6))
#
# # OBS: Retorna o ídice do primeiro elemento encontrado
# print(numeros.index(5))
#
# # Podemos fazer busca dento de um range, ou seja, de qual índice começar a buscar
# print(numeros.index(5, 1)) # Buscando a partir do índice 1
#
# # Podemos fazer busca dento de um range, início/fim
# print(numeros.index(8, 3, 6)) # Busca o índice do valor 8, entre os índices 3 a 6.

# Revisão de Slicing
# lista[inicio:fim:passo]
# range(início:fim:passo]

# Trabalhando com slice de lista com o parâmetro 'início'
# lista = [1, 2, 3, 4]
# print(lista[1:]) # Iniciando do índice 1 e pegando todos os índices restantes
#
# # Trabalhando com slice de lista com o parâmetro 'fim'
# print(lista[:2]) # Começa em 0 e pega até o índice 2 - 1
# print(lista[1:4]) # Começa em 1 e pega até o índice 4 - 1
#
# # Trabalhando com slice de lista com o parâmetro 'passo'
# print(lista[::2]) # Começa em 0, vai até o final de 2 em 2

# Invertendo valores em uma lista
# nomes = ['Python', 'Project']
# nomes.reverse()
# print(nomes)

# Soma, #Valor Máximo, Valor Mínimo, Tamanho
# * Se os valores forem todos inteiros ou reais

# lista = [1, 2, 3, 4, 5, 6]
# print(sum(lista)) # Soma
# print(max(lista)) # Máximo valor
# print(min(lista)) # Mínimo valor
# print(len(lista)) # Tamamho da lista

# Transformar uma lista em Tupla
# lista = [1, 2, 3, 4, 5, 6]
# print(lista)
# print(type(lista))
#
# tupla = tuple(lista)
# print(tupla)
# print(type(tupla))

# Desempacotamento de listas

# lista = [1, 2, 3]
# num1, num2, num3 = lista
# print(num1)
# print(num2)
# print(num3)

# OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber os dados, teremos ValueError.

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista # Cópia
print(nova)

nova.append(4)
print(lista)
print(nova)
 # Utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista
 # mas após realizar a modificação em uma das listas, essa modificação se refletiu em ambas as listas
 # Isso em Python é chamado de Sallow Copy.

# Forma 2 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy() # Cópia
print(nova)

nova.append(4)

print(lista)
print(nova)

# Ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista,
# mas elas ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra
# Em Python, isso é chamado de Deep Copy (cópia profunda)
