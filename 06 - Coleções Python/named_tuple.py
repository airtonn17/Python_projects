"""
Módulo Collections - Named Tuple

# Recap Tupla
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros
"""

# Importando
from collections import namedtuple

"""
# Definindo nome e parâmetro.
"""
# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma2 - Declaração Named Tuple
cachorro = namedtuple('cachorro','idade, raca, nome')

# Forma3 - Declaração Named Tuple
cachorro = namedtuple('cachorro',['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade = 2, raca = 'Chow-Chow', nome = 'Ray')

print(ray)

"""
# # Acessando os Dados
"""
# forma 1
print(ray[0]) # Idade
print(ray[1]) # Nome
print(ray[2]) # Raça

# Forma 2
print(ray.idade) # Idade
print(ray.nome) # Nome
print(ray.raca) # Raça

"""
# # Formas de Fazer Acesso
"""
print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))
