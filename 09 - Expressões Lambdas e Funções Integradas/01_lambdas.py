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

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo(' FELICITY'         , ' jones '))
