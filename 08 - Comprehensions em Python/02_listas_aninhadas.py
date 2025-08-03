"""
Listas Aninhadas (Nested List)

- Algumas linguagens de programação possuem uma estrutura de dados chamada de arrays:
    - Unidimencionais (Array/Vetores);
    - Multidimencionais (Matrizes);

Em Python nós temos as Listas

numeros = [1, 'b', 3.234, True, 5]
"""

"""
# Exemplo
"""
#
# listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3
#
# print(listas)
# print(type(listas))


"""
#  Como fazemos para acessar os dados?
"""
#
# listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# print(listas[0][1]) # 2
# print(listas[2][1]) # 8


"""
# Iterando com loops em uma lista aninhada
"""
#
# listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for lista in listas:
#     for num in lista:
#         print(num)


"""
# List Comprehension
"""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(valor) for valor in lista] for lista in listas]

