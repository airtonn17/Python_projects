"""
Funções com retorno

OBS: Em Python, quando uma funçao não retorna nenhum valor, o retorno é None

OBS: Funções Python que retornam valores, devem retornar estes valores com a
palavra reservada return

OBS: Não precisamos necessáriamente criar uma variável para receber o retorno
de uma função. Podemos passar execução da função para outras funções.
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

# # Vamos refatorar essa função para que ela retorne um valor
#
# def quadrado_de_7():
#     return 7 * 7
#
# # Criamos uma variável para retornar o valor da função
# ret = quadrado_de_7()
# print(f"Retorno {ret}")
#
# print(f'Retorno: {quadrado_de_7() + 1}')

# Refatorando a primeira função

def diz_oi():
    return 'Oi '

alguem = 'Pedro!'

diz_oi()
print(diz_oi() + alguem)
