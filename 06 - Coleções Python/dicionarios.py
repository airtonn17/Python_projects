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

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Podemos verufucar se determinada chave se encontra em um discionário.
# print('br' in paises)
# print('ru' in paises)
# print('Estados Unidos' in paises)
#
# if 'ru' in paises:
#     russia = paises['ru']

# # Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, discionário, como chave
# # de discionários.
#
# # Tuplas por exemplo, são bastante interessantes de serem utilizadas como chave de discionário, pois as mesmas
# # são imutáveis.
#
# localidades = {
#     (35.6895, 39.6917): 'Escritório em Tókio',
#     (40.7128, 74.0060): 'Escritório em Nova York',
#     (37.7749, 122.4194): 'Escritório em São Paulo'
# }
#
# print(localidades)
# print(type(localidades))

# Adicionar elementos em um discionário
# receita = {'jan': 100, 'fev':120, 'mar':300}
# print(receita)
# print(type(receita))
#
# # Forma 1 - Mais comum
# receita['abr'] = 350
# print(receita)
#
# # Forma 2
# novo_dado = {'mai':500}
# receita.update(novo_dado) # receita.update({'mai': 500})
# print(receita)
#
# # Atualizando dados em um discionário
#
# # Forma 1
# receita['mai'] = 550
# print(receita)
#
# # Forma 2
# receita.update({'mais': 600})
# print(receita)
#
# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um discionário é a mesma.
# CONCLUSÃO 2: Em discionários, não podemos ter chaves repetidas.

# Como remover dados de um discionário

# receita = {'jan': 100, 'fev':120, 'mar':300}
# print(receita)
#
# # Forma 1 - Mais comum
# ret = receita.pop('mar')
# print(ret)
# print(receita)
#
# # OBS 1: Aqui precisamos sempre infomar a chave, e caso não encontre o elemento, um KeyError é retornado.
# # OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.
#
# # Forma 2
# del receita['fev']
# print(receita)
# # Neste caso o valor removido não é retornado.

# # Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.
# """
# Carrinho de Compras:
#     Produto 1:
#         - nome;
#         - quantidade;
#         - preço;
#     Produto 2:
#         - nome;
#         - quantidade;
#         - preço;
# """
# # 1 - Poderíamos utilizar uma lista para isso? Sim!
# carrinho = []
# produto1 = ['Play4', 1, 2300.00]
# produto2 = ['God Of War', 1, 150.00]
#
# carrinho.append(produto1)
# carrinho.append(produto2)
# print(carrinho)
#
# # Teríamos de saber qual é o índice de cada informação no produto.
#
# # Poderíamos utilizar uma tupla para isso? Sim!
# produto1 = ('Play4', 1, 2300.00)
# produto2 = ('God Of War 4', 1, 150.00)
# carrinho = (produto1, produto2)
# print(carrinho)
#
# # Teríamos de saber qual é o índice de cada informação no produto.
#
# # 3 - Poderíamos utilizar um discioário para isso? Sim!
#
# carrinho = []
# produto1 = {'Nome: ': 'Play4', 'Quantidade': 1, 'Valor': 2300.00}
# produto2 = {'Nome: ': 'God Of War 4', 'Quantidade': 1, 'Valor': 150.00}
#
# carrinho.append(produto1)
# carrinho.append(produto2)
# print(carrinho)
#
# # Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# # podemos ter a certeza sobre cada informação.

# Métodos de discionários.

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# # Limpar o discionário (zerar dados)
# d.clear()
# print(d)

# Copiando um discionário para outro
# # Forma 1 - Deep Copy
# novo = d.copy()
# print(novo)
#
# novo['d'] = 4
# print(d)
# print(novo)

# # Forma 2 - Shallow Copy
# novo = d
# print(novo)
#
# novo['d'] = 4
# print(d)
# print(novo)

# # Forma não usual de criação de discionários
#
# outro = {}.fromkeys('a', 'b')
#
# print(outro)
# print(type(outro))
#
# usuario = {}.fromkeys(['nome', 'pontes', 'email', 'profile'], 'desconhecido')
# print(usuario)
# print(type(usuario))
#
# # O méodo fromkeys recebe dois parâmetros: um interável e um valor.
# # Ele vai gerar para cada valor do interável uma chave e irá atribuir a essa chave o valor informado.
#
# veja = {}.fromkeys('teste', 'valor')
# print(veja) # {'t': 'valor', 'e': 'valor', 's': 'valor'}
#
# veja = {}.fromkeys(range(1, 11), 'novo')
# print(veja) # {1: 'novo', 2: 'novo', 3: 'novo', 4: 'novo', 5: 'novo', 6: 'novo', 7: 'novo', 8: 'novo', 9: 'novo', 10: 'novo'}
