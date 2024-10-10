"""
Tuplas (tuple)

Tplas são bastante parecidas com listas

Existem basicamente duas diferenças

1 - As tuplas são representadas por parenteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda.
Toda operação em uma tupla, gera uma nova tupla.
"""
from operator import index

# CUIDADO 1: As tuplas são representadas por parênteses (), mas veja:
# tupla1 = (1, 2, 3, 4, 5, 6)
# print(tupla1)
# print(type(tupla1))
#
# tupla2 = 1, 2, 3, 4, 5, 6
# print(tupla2)
# print(type(tupla2))
#
# # VUIDADO 2: Tuplas com 1 elemento
# tupla3 = (4) # Isso não é uma tupla!
# print(tupla3)
# print(type(tupla3))
#
# tupla4 = (4,) # Isso é uma tupla!
# print(tupla4)
# print(type(tupla4))
#
# tupla5 = 4, # Isso é uma tupla!
# print(tupla5)
# print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas por vírgulas e não pelo uso do parênteses.

#Podemos gerar uma tupla dinamicamente com range(início,fim,passo)
# tupla = tuple(range(11))
# print(tupla)
# print(type(tupla))

# Desempacotamento de tuplas
# tupla = ('Python Project', 'Airton Cavalcante')
# projeto, aluno = tupla
# print(projeto)
# print(aluno)
# Gera erro (ValueError) se colocarmos um numero diferente de elementos para desempacotar.

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais.
# tupla = (1, 2, 3, 4, 5, 6)
# print(sum(tupla))
# print(max(tupla))
# print(min(tupla))
# print(len(tupla))

# Concatenação de tuplas
# tupla1 = (1, 2, 3)
# print(tupla1)
#
# tupla2 = (4, 5, 6)
# print(tupla2)
#
# print(tupla1 + tupla2) # Tuplas são imutáveis
#
# print(tupla1)
# print(tupla2)
#
# tupla1 = tupla1 + tupla2 # Tuplas são imutáveis, mas podemos sobrescrever seus valores.
# print(tupla1)

# Verificar se determinado elemento está contido na tupla
# tupla = (1, 2, 3)
# print(33 in tupla)

# Iterando sobre uma tupla
# tupla = (1, 2, 3)
# for n in tupla:
#     print(n)
#
# for i, valor in enumerate(tupla):
#     print(i, valor)

# Contando elementos dentro de uma tupla
# tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
# print(tupla.count('a'))
#
# projeto = tuple('Python Project')
# print(projeto)
# print(projeto.count('o'))

# Dicas na utilização de tuplas
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outrubo', 'Novembro', 'Dezembro')
print(meses)

# O acesso de elementos em uma tupla também é semelhante a de uma lista
# print(meses[5])
#
# # Iterar com while
# i = 0
# while i < len(meses):
#     print(meses[i])
#     i = i + 1

# Verificamos em qual índice um elemento está na tupla
# print(meses.index('Junho'))

# Slicing
# tupal[inicio,fim,passo]
# print(meses[::2])

# Por quê utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro*.

# * Isso porque trabalhar com elementos imutáveis traz mais segurança para o código.

# Copiando uma tupla para outra
# tupla = (1, 2, 3)
# print(tupla)
#
# nova = tupla # Na tup´la não temos o problema de Shallow Copy
#
# print(nova)
# print(tupla)
#
# outra = (4, 5, 6)
# nova = nova+ outra
#
# print(nova)
# print(tupla)
