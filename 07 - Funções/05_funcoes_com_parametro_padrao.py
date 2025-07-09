"""
Funções com parâmetro padrão (Default Paramters)

- Funções onde a passagem de parâmetros seja opcional;
"""

"""
# Exemplo de função onde a passagem por parâmetro seja opcional
"""
#
# print('Python Project')
# print()


"""
# Exemplo de função onde a passagem de parâmetro seja obrigatória
"""
#
# def quadrado(numero):
#     return numero ** 2
#
# print(quadrado(3))
# print(quadrado()) # TypeError


"""
# Exemplo de função onde a passagem de parâmetro não seja obrigatória
"""
#
# def exponecial(numero = 4, potencia = 2):
#     return numero ** potencia
#
# print(exponecial(2, 3)) # 2 * 2 * 2 = 8
# print(exponecial(3, 2)) # 3 * 3 = 9
#
# print(exponecial(3)) # Por padrão eleve ao quadrado
# print(exponecial(3, 5)) # Eleva a potência informada pelo usuário
#
# # OBS
# # Se o usuário passar somente 1 argumento, este será atribuído so parâmetro numero, será calculado o quadrado deste número;
# # Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro número e o segundo ao parâmetro potência. Então
# # será calculada esta potência.
#
# print(exponecial())


"""
#  OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.
"""
#
# # ERRO!
# def teste(potencia, num = 2):
#     return num ** potencia
#
# print(teste(6))


"""
# Outros exemplos
"""
#
# def soma(num1 = 5, num2 = 3):
#     return num1 + num2
#
# print(soma(4, 3))
# print(soma(4))
# print(soma())


"""
# Exemplo mais complexo
"""
#
# def mostra_informacao(nome = 'Airton', instrutor = False):
#     if nome == 'Airton' and instrutor:
#         return 'Bem-vindo instrutor Airton'
#     elif nome == 'Airton':
#         return 'Eu pensei que você era instrutor'
#     return f'Olá, {nome}!'
#
# print(mostra_informacao())
# print(mostra_informacao(instrutor = True))
# print(mostra_informacao(True))
# print(mostra_informacao('Ozzy'))
# print(mostra_informacao(nome = 'Stephany'))



"""
# Poruqe utilizar parâmetros com valor default?
"""