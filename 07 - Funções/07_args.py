"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá
chamar de qualque coisa, desde que comece com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para defili-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.
"""

"""
# Exemplo
"""
#
# def soma_todos_numeros(num1, num2, num3):
#     return num1 + num2 + num3
#
# print(soma_todos_numeros(4, 6, 9))
# # print(soma_todos_numeros(4, 6)) # TypeError
# # print(soma_todos_numeros(4, 6, 9, 5)) # TypeError


"""
# Entendendo o args
"""
#
# def soma_todos_numeros(nome, email, *args):
#     return sum(args)
#
# print(soma_todos_numeros('Angelina', 'Jolie'))
# print(soma_todos_numeros('Angelina', 'Jolie', 1))
# print(soma_todos_numeros('Angelina', 'Jolie', 2, 3))
# print(soma_todos_numeros('Angelina', 'Jolie', 2, 3, 4))
# print(soma_todos_numeros('Angelina', 'Jolie', 3, 4, 5, 6))
#
# print(soma_todos_numeros('Angelina', 'Jolie', 23.4, 123.5))


"""
# Outro exemplo de utilização do *args
"""
#
# def verifica_info(*args):
#     if 'Airton' in args and 'Cavalcante' in args:
#         return 'Bem-vindo Airton!'
#     return 'Eu não tenho certeza quem você é ...'
#
# print(verifica_info())
# print(verifica_info(1, True, 'Airton', 'Cavalcante'))
# print(verifica_info(1, 'Cavalcante', 3.145))


"""
# Desempacotador
"""

def soma_todos_numeros(*args):
    return sum(args)
#
# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))
#
# numeros = [1, 2, 3, 4, 5, 6, 7]
#
# print(soma_todos_numeros(*numeros))
#
# # OBS: O asterisco serve para que informemos ao Python que estamos
# # passando como argumento uma coleção de dados. Desta forma, ele saberá
# # que precisará antes desempacotar estes dados.