"""
Dicionários

OBS: Em algumas linguagens de programação, os discionários Python são conhecidos por mapas.

Discionários são coleções do tipo chave/valor.

Discionários são representados por chaves {}.

OBS: Sobre discionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados;
"""
# Criação de Discionários

# Forma 1 (Mais comum)
#
# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# print(paises)
# print(type(paises))
#
# # Forma 2 (Menos comum)
# paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
# print(paises)
# print(type(paises))

# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# # Acessando Elementos
#
# # Forma 1 - Acessando via chave, da mesma forma que lista/tupla
# print(paises['br'])
# print(paises['py'])
#
# # Forma 2 - Acessando via get - Recomendada
# print(paises.get('br'))
# OBS: Caso o get não encontre o objeto coma chave informada, será retornado o valor None e não será gerado KeyError

# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# pais = paises.get('ru')
# if pais:
#     print(f'Encontrei o país {pais}')
# else:
#     print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# pais = paises.get('ru', 'Não encontrado')
# print(f'Encontrei o país {pais}')