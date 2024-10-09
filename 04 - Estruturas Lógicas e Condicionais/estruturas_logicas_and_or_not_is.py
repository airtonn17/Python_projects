"""
Estruturas Lógicas: AND(e), OR(ou), NOT(não), IS(é)

Operadores Unários:
    - not;
Opersadores Binários:
    - and, or, is

Regras de Funcionamento:
Para o 'AND', ambos os valores precisam ser True.
Para o 'OR', um ou outro valor precisa ser True.
Para o 'NOT', o valor do booleano é invertido, ou seja, se for Ture vira False, se for False vira True
Para o 'IS', o valor é comparado com um segundo.
"""

ativo = False
logado = False

if ativo or logado:
    print('Bem vindo, usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# Se não estiver ativo
if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bmem vindo, usuário!')

print(not False)
