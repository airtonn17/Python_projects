"""
Módulo Colections - Counter (contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Colections Counter que é parecido
com um discionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.
"""

# Realizando o Import

from collections import Counter

# # Podemos usar qualquer iterável, aqui usamos ums Lista
# lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]
#
# # Utilizando o Counter
# res = Counter(lista)
#
# # Exemplo 1
# print(type(res)) # 'collections.Counter'
# print(res) # Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
#
# # Veja que, para cada elemento da lista, o Counter criou um chave e colocou como valor a quantidade de ocorrências.
#
# # Exemplo 2
# print(Counter('Python Project')) # ({'P': 2, 't': 2, 'o': 2, 'y': 1, 'h': 1, 'n': 1, ' ': 1, 'r': 1, 'j': 1, 'e': 1, 'c': 1})
#
# Exemplo 3
texto = """Spirit lead me where my trust is without borders
Let me walk upon the waters
Wherever You would call me
Take me deeper than my feet could ever wander
And my faith will be made stronger
In the presence of my Saviour"""

palavras = texto.split()
res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrências no texto.
print(res.most_common(5))

