"""
Mapas - Conhecidos em Python como dicionários.

Dicionários em Python são representados por chaves {}
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

# # Iterar sobre dicionários
#
# for mes in receita:
#     print(mes)
#
# for mes in receita:
#     print(receita[mes])
#
# for mes in receita:
#     print(f'Em {mes} recebi R${receita[mes]} reais') # Chave e valor

# Acessando as Chaves

# print(receita.keys()) # Discionário de chaves
#
# for chave in receita.keys():
#     print(receita[chave])

# # Acessando os Valores
# print(receita.values())
#
# for valor in receita.values():
#     print(valor)

# # Desempacotamento de Discionários
#
# print(receita.items())
#
# for chave, valor in receita.items():
#     print(f'chave={chave} e valor={valor}')

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

# print(sum(receita.values()))
# print(max(receita.values()))
# print(min(receita.values()))
# print(len(receita.values()))