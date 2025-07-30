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

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

# Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:
# - A primeira parte: for numero in numeros
# - A segunda parte: numero * 10

