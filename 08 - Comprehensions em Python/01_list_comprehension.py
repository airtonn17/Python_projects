""""
List Comprehensions

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro
iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]
"""


"""
# Exemplos
"""
#
# numeros = [1, 2, 3, 4, 5]
#
# res = [numero * 10 for numero in numeros]
#
# print(res)
#
# # Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:
# # - A primeira parte: for numero in numeros
# # - A segunda parte: numero * 10
#
# res = [numero / 2 for numero in numeros]
# print(res)
#
# def funcao(valor):
#     return valor * valor
#
# res = [funcao(numero) for numero in numeros]
# print(res)


"""
# Lis Comprehension vs Loop
"""
#
# numeros = [1, 2, 3, 4, 5]
#
# # Loop
# numeros_dobrados = []
#
# for numero in numeros:
#     numeros_dobrados.append(numero * 2)
#
# print(numeros_dobrados)
#
# # List Comprehension
# print([numero * 2 for numero in numeros])


"""
# Outros Exemplos
"""

# 01
#
# nome = 'Python Project'
#
# print([letra.upper() for letra in nome])

# 02
#
# amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
#
# print([amigo.capitalize() for amigo in amigos])
#
# # def caixa_alta(nome): # Modo que o professor fez mas achei um melhor
# #     nome = nome.replace(nome[0], nome[0].upper())
# #     return nome
# #
# # print([caixa_alta(amigo) for amigo in amigos])
#
# # 03
#
# print([numero * 3 for numero in range(1, 10)])
#
# # 04
#
# print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
#
# # 05
#
# print([str(numero) for numero in [1, 2, 3, 4, 5]])


"""
# Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension
"""

# Exemplos

# 01

numeros = [1, 2, 3, 4, 5, 6]

pares = [ numero for numero in numeros if numero % 2 == 0]
imparees = [ numero for numero in numeros if numero % 2 != 0]

print(pares)
print(imparees)