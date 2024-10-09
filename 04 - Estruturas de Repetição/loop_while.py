"""
Loop While

Forma geraL

While expressão_booleana
    //execução do loop

O bloco ehile será repetido enquanto a expressão booleana for verdadeira.
Expressãqo Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:
num = 5
num < 5 -> False
num < 10 -> True

"""
# Exemplo 1

# numero = 1
#
# while numero < 1:
#     print(numero)
#     numero = numero + 1 # Critério de parada

# OBS: Em um loop while, é importante que cuidemos do critério de parada.

# Exemplo 2

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')
