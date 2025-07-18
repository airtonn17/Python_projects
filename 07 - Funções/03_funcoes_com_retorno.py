"""
Funções com retorno

OBS: Em Python, quando uma funçao não retorna nenhum valor, o retorno é None

OBS: Funções Python que retornam valores, devem retornar estes valores com a
palavra reservada return

OBS: Não precisamos necessáriamente criar uma variável para receber o retorno
de uma função. Podemos passar execução da função para outras funções.

OBS; Sobre a palavra return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

"""

# numeros = [1, 2, 3]
#
# ret_pop = numeros.pop()
#
# print(f"Retorno de pop: {ret_pop} ")
#
# ret_pr = print(numeros)
#
# print(f"Retorno de print: {ret_pr}")


"""
# # Vamos refatorar essa função para que ela retorne um valor
"""
#
# def quadrado_de_7():
#     return 7 * 7
#
# # Criamos uma variável para retornar o valor da função
# ret = quadrado_de_7()
# print(f"Retorno {ret}")
#
# print(f'Retorno: {quadrado_de_7() + 1}')


"""
# # Refatorando a primeira função
"""
#
# def diz_oi():
#     return 'Oi '
#
# alguem = 'Pedro!'
#
# diz_oi()
# print(diz_oi() + alguem)

# # OBS; Sobre a palavra return
#
# # 1 - Ela finaliza a função, ou seja, ela sai da execução da função;
#
# def diz_oi():
#     print('Estou sendo execultado antes o retorno')
#     return 'Oi!'
#     print('Estou sendo execultado após o retorno')
#
# print(diz_oi())
#
# # 2 - Podemos ter, em uma função, diferentes returns;
#
# def nova_funcao():
#     variavel = False
#     if variavel:
#         return 4
#     elif variavel is None:
#         return 3.2
#     return 'b'
#
# print(nova_funcao())
#
# # 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;
#
# def outra_funcao():
#     return 2, 3, 4, 5
#
# # num1, num2, num3, num4 = outra_funcao()
# # print(num1, num2, num3, num4)
#
# print(outra_funcao())


"""
# # Vamos criar uma função para jugar uma moeda
"""
#
# from random import random
#
# def joga_moeda():
#     # Gera um número pseudo-randônico entre 0 e 1
#     if random() > 0.5:
#         return 'Cara'
#     return 'Coroa'
#
# print(joga_moeda())


"""
# Erros comuns na utilização oo retorno, que na verdade nem é erro, mas sim codificação desnecessária.
"""
#
# def eh_impar():
#     numero = 6
#     if numero % 2 != 0:
#         return True
#     return False
#
# print(eh_impar())
