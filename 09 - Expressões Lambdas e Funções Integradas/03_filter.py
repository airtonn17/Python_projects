"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.
"""

# valores = 1, 2, 3, 4, 5, 6
#
# media  = (sum(valores) / len(valores))
#
# print(media)

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: ', media)

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda valor: valor > media, dados)
print(list(res))
