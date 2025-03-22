"""
Módulo Collections - Default Dict

# Recap Dicionário

dicionario = {'Curso': 'Python Project'}
print(dicionario)
print(dicionario['Curso'])
print(dicionario['Outro']) # ??? KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lâmbida para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuido.

OBS: lambdas são funções sem nome, que podem ou não receber parâmetro de entrada
e retornar valores.
"""

# Fazendo Import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario) # defaultdict(<function <lambda> at 0x000001B86D7C8AE0>, {})

dicionario['curso'] = 'Python Project'
print(dicionario) # defaultdict(<function <lambda> at 0x000001B86D7C8AE0>, {'curso': 'Python Project'})

print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não.
print(dicionario) # defaultdict(<function <lambda> at 0x000001B86D7C8AE0>, {'curso': 'Python Project', 'outro': 0})
