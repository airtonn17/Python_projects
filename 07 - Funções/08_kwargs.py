""""
**kwargs

Poderíamos chamar esse parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige qye utilizemos parâmtetros nomeados, e transforma esses
parâmetros extras em um dicionário.

#  Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args
- Parâmetros default (não obrigatórios
- **kwargs

"""


"""
# Exemplo
"""
#
# def cores_favoritas(**kwargs):
#     for pessoa, cor in kwargs.items():
#         print(f'A cor favorita de {pessoa.title()} é {cor}')
#
#
# cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')
#
# # OBS: OS parâmetros *args e **kwargs não são obrigatórios.
#
# cores_favoritas()
#
# cores_favoritas(python='Project')


"""
# Exemplo mais complexo
"""
#
# def cumprimento_especial(**kwargs):
#     if 'python' in kwargs and kwargs['python'] == 'Project':
#         return 'Você recebeu um cumprimento Pythonico!'
#     elif 'python' in kwargs:
#         return f"{kwargs['python']} Python!"
#     return 'Não tenho certeza quem você é ...'
#
# print(cumprimento_especial())
# print(cumprimento_especial(python='Project'))
# print(cumprimento_especial(python='Oi'))
# print(cumprimento_especial(python='especial'))


"""
#  Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args
- Parâmetros default (não obrigatórios)
- **kwargs
"""

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos') # idade e nome = parâmetros obrigatórios
    print(args) # parâmetro não obrigatório
    if solteiro: # parâmetro default (não obrigatório)
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs) # parâmetro não obrigatório

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)
