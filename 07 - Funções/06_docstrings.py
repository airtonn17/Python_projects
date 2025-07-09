"""
Documentando funções com Docstrings

OBS: Podemos ter acesso à documentação de uma função em Python
utilizando a propriedade especial __doc__
"""

#  Exemplos

def diz_oi():
     """Uma função simples que retorna a string 'Oi!'"""
     return 'Oi!'

def esponencial(numero, potencia = 2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' à 'potencia' informada.
    :param numero: Número que desejamos gerar por exponencial.
    :param potencia: Potencia que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia
