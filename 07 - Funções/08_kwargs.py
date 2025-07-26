""""
**kwargs

Poderíamos chamar esse parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige qye utilizemos parâmtetros nomeados, e transforma esses
parâmetros extras em um dicionários+
"""

"""
# Exemplo
"""
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')
