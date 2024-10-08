"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constanytes, verdadeiro ou falso
True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiuscula
Errado -> true, false
Certo -> True, False
"""

ativo = False
print(ativo)

"""
Operações Básicas
"""
# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro, o resultado será falso,
Se for falso o resultado será verdadeiro. Ou seja, sempre o contratio.
"""
print(not ativo)

logado = False

# Ou (or):
"""
É uma operação binária, ou seja, sepende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)


# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores.
Ambos os valores devem ser verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""

print(5 > 6)
print(5 > 6 or 5 > 7)
