"""
Utilizando Lambidas

Conhecidas por Expressões Lambidas, ou simplesmente Lambidas, são
funções sem nome, ou seja, funções anônimas.

# Função em Python

def soma(a, b):
    return a + b

"""
"""
# Declaração e Utilização Inicial
"""
#
# def funcao(x):
#     return 3 * x + 1
#
# print(funcao(4))
# print(funcao(7))
#
# # Expressão Lambda
# lambda x: 3 * x + 1
#
# # Como utilizar a expressão lambida?
# calc = lambda x: 3 * x + 1
#
# print(calc(4))
# print(calc(7))

"""
# Podemos ter expressões lambidas com múltiplas entradas.
"""
#
# nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
#
# print(nome_completo(' angelina', 'JOLIE'))
# print(nome_completo(' FELICITY'         , ' jones '))


"""
Em funções python podemos ter nenhuma ou várias entradas em lambdas também
"""
#
# amar = lambda: 'Como não amar Python? '
# uma = lambda x: 3 * x + 1
# duas = lambda x, y: (x * y) ** 0.5
# tres = lambda x, y, z: 3 / (1 / x + 1/ y + 1 / z)
# # n = lambda x1, x1, ..., xn, <expressão>
#
# print(amar())
# print(uma(6))
# print(duas(5, 7))
# print(tres(3, 6, 9))
#
# # OBS: Se passarmos mais argumentos do que parâmetros esperados, teremos TypeError

"""
Outro Exemplo
"""
autores = ['Isaac Asimov', 'Ray Bradnury', 'Robert Heinlein',
           'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adamns', 'H. G. Wells','Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)