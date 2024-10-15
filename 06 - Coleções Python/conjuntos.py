"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a Teoria dos Conjuntos
da Matemática

- Aqui no Python os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na Matemática:

- Sets (conjuntos) não possuem valores aplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se ultilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e iténs duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Discionário) em Python:
    - Um discionário tem chave/valor;
    - Um conjunto tem apenas valor;
"""

# # Definindo um Conjunto:
#
# # Forma 1
# s = set({1, 2, 3, 4, 5, 5, 6, 7,2 ,3 }) # Repare que temos valores repetidos.
# print(s)
# print(type(s))
#
# # OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# # será ignorado sem gerar erros e não fará parte do conjunto
#
# # Forma 2 - Mais Comum
# s = {1, 2, 3, 4, 5, 5}
# print(s)
# print(type(s))
#
# # Podemos verificar se determinado elemento está contido no elemento
#
# if 13 in s:
#     print('Tem o 3')
# else:
#     print('Não tem o 3')

# # Importante lembrar que além de não termos valores duplicados, não temos ordem
#
# # Listas aceitam valores duplicados, então temos 10 elementos
# lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
# print(f'Lista: {lista} com {len(lista)} elementos')
#
# # Tuplas aceitam valores duplicados, então temos 10 elementos
# tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
# print(f'Tupla: {tupla} com {len(tupla)} elementos')
#
# # Discionários não aceitam chaves duplicadas, então temos 8 elementos
# discionario = {}.fromkeys ([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
# print(f'Discionário: {discionario} com {len(discionario)} elementos')
#
# # Conjuntos não aceitam valores duplicados, então temos 8 elementos
# conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
# print(f'Conjunto: {conjunto}com {len(conjunto)} elementos')

# # Assim cmo tod outro conjunto Ptyhon podemos colocar tipos de dados misturados em Sets
#
# s = {1, 'b', True, 34.22, 44}
# print(s)
# print(type(s))
#
# # Podemos Iterar em um Set normalmente
# for valor in s:
#     print(valor)
