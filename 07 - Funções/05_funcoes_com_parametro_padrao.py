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
# Porque utilizar parâmetros com valor default?
"""

# - Nos permite ser mais flexíveis nas funções;
# - Evita erros com parâmetros incorretos;
# - Nos permitem trabalhar com exemplos mais legíveis de código;


"""
# Quais tipos de dados podemos utilizar como valores default para parâmetros?
"""
#
# # - Qualquer tipo de dado:
#     # - Números, strings, floats, booleanos, listas, tuplas, dicionários, etc;
#
# # Exemplo
#
# def soma(num1, num2):
#     return num1 + num2
#
# def mat(num1, num2, fun = soma):
#     return fun(num1, num2)
#
# def subtracao(num1, num2):
#     return num1 - num2
#
# print(mat(2, 3))
# print(mat(2, 2, subtracao))
# print()


"""
# Escopo - Evitar problemas e confusões... 
"""
#
# # Variáveis globais
# # Variáveis locais
# instrutor = 'Airton' # Variável global
# def diz_oi():
#     instrutor = 'Python' # Variável local
#     return f'Oi, {instrutor}'
#
# print(diz_oi())
#
# # OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.


"""
# Uma variável local só é reconhecida dentro o bloco que foi criada.
"""
#
# def diz_oi():
#     prof = 'Airton' # Variável local
#     return f'Olá {prof}'
#
# print(diz_oi())
# # print(prof) # NameError

"""
# ATENÇÃO com variáveis globais (Se puder evitar, evite!)
"""
#
# total = 0
#
# def incrementa():
#     total = total + 1 # UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada)
#     return total
#
# print(incrementa())


"""
# ATENÇÃO com variáveis globais (Como resolver caso utilizar)
"""
#
# total = 0
#
# def incrementa():
#     global total # Avisando que queremos utilizar a variável global
#
#     total = total + 1
#     return total
#
# print(incrementa())
# print(incrementa())
# print(incrementa())


"""
# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável
"""
#
# def fora():
#     contador = 0
#
#     def dentro():
#         nonlocal contador
#
#         contador = contador + 1
#         return contador
#     return dentro()
#
# print(fora())
# print(fora())
# print(fora())
#
# # print(dentro()) #NameError
