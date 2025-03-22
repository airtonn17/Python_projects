"""
Módulo Collections: Ordered Dict

OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.
"""

# Fazendo Import
from collections import OrderedDict

"""
# Em um dicionário a ordem de inserção dos elementos n é garantida
"""
# dicionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
#
# for chave, valor in dicionario.items():
#     print(f"chave = {chave} : valor = {valor}")

"""
# # OrderedDirect
"""
# dicionario = OrderedDict({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})
#
# for chave, valor in dicionario.items():
#     print(f"chave = {chave} : valor = {valor}")

"""
# # Diferença entre Dict e OrderedDict
"""
# # Dicionários Comuns
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 2, 'a': 1}
#
# print(dict1 == dict2) # True -> Já que a ordem dos elementos não importa para os dicionários.
#
# # Ordered Dict
# odict1 = OrderedDict({'a': 1, 'b': 2})
# odict2 = OrderedDict({'b': 2, 'a': 1})
#
# print(odict1 == odict2) # False -> Já que a ordem dos elementos importa para o OrderedDict.
