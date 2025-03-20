"""
Mapas - Conhecidos em Python como dicionários.

Dicionários em Python são representados por chaves {}
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

"""
# # Iterar sobre dicionários
"""
# for mes in receita:
#     print(mes) # {'jan': 100, 'fev': 250, 'mar': 400}
#
# for mes in receita:
#     print(receita[mes]) # Print de todas as chaves
#
# for mes in receita:
#     print(f'Em {mes} recebi R${receita[mes]}') # Print dos valores de cada chave

"""
# # Acessando as Chaves
"""
# print(receita.keys()) # Dicionário de chaves
#
# for chave in receita.keys():
#     print(receita[chave]) # Valor de cada chave

"""
# # Acessando os Valores
"""
# print(receita.values()) # Dicionário de valores
#
# for valor in receita.values():
#     print(valor) # Valores de cada chave

"""
# # Desempacotamento de Dicionários
"""
# print(receita.items()) # Dicionário de ítens
#
# for chave, valor in receita.items():
#     print(f'chave = {chave} e valor = {valor}')

"""
# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais
"""
# print(sum(receita.values()))
# print(max(receita.values()))
# print(min(receita.values()))
# print(len(receita.values()))
