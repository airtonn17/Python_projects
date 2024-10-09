"""
Listas

Listas em python, funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possue tamanho fixo:
Ou seja, podemos criar a lista e simplesmente ir adicionando os elementos;
- Qualquer tipo de dado: Não possuem tipo de dao fixo:
Ou seja, podemos colocar qualquer tipo de dado;

As listas em python são representadas por colchetes: []
"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'j', 'e', 'c', 't']
litsa3 = []
lista4 = list(range(11))
lista5 = list('Pytho Project')

# Podemos facilmente checar se determinado valor está contido na lista
# num = 7

# if num in lista4:
#     print(f'Encontrei o número {num}')
# else:
#     print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
# lista1.sort()
# print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista.
# print(lista1.count(1))
# print(lista5.count('t'))

# Adicionar elementos em listas
"""
Para adicionar elementos em lista, ultilizamos a função apend
"""
# print(lista1)
# lista1.append(42)
# print(lista1)

# OBS: Com o append nós só conseguimos adicionar 1 elemento por vez
# lista1.append(12, 34, 56) # Erro

# lista1.append([8, 3, 1]) # Adiciona uma lista como elemento único (sub lista)
# print(lista1)

# if [8, 3, 1] in lista1:
#     print('Encontrei a lista')
# else:
#     print('Não encontrei a lista')

# lista1.extend([123, 44, 67]) # Adiciona cada elemento na lista como valor adicional a lista
# print(lista1)

# Podemos inserir um no elemento na lista informando a posição do índice
# Isso não substitue o valor inicial. O mesmo será deslocado para a direita da lista.
# lista1.insert(2, 'novo valor')
# print(lista1)

# Podemos facilmente junstar duas listas
# lista6 = lista1 + lista2
# print(lista6)

# Podemos facilmente inverter uma lista

# Forma 1
# lista1.reverse()
# lista2.reverse()
# print(lista1)
# print(lista2)

# Forma 2
# print(lista1[::-1])
# print(lista2[::-1])

# Copiar uma lista
# lista6 = lista2.copy()
# print(lista6)

#Podemos contar quantos elementos existem dentro da lista
# print(len(lista1))

# Podemos remover facilmente o último elemento de uma lista
# O pop não somente remove o último elemento, mas também o retorna
# print(lista5)
# lista5.pop()
# print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos serão descocados para a esquerda.
# OBS: Se não houver elemento no índice informado, teremos o erro IndexError.
# lista5.pop(2)
# print(lista5)

# Podemos remover todos os elementos (zerar a lista)
# print(lista5)
# lista5.clear()
# print(lista5)

# Podemos facilmente repetir elementos em uma lista
# nova = [1, 2, 3]
# print(nova)
# nova = nova * 3
# print(nova)

# Podemos facilmente converter uma String para uma lista
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

# Convertendo uma lista em uma String
# lista6 = ['Python', 'Project', 'Airton', 'Cavalcante']
# print(lista6)

# Adiciona espaço entre cada elemento na lista e transforma em uma String
# curso = ' '.join(lista6)
# print(curso)

