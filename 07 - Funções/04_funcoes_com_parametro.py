"""
Funções com parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem sáida;
- Possuem entrada, mas não possuem saída;
- Não possuem entrada, mas possuem saída;
- Possuem entrada e saída;

"""
"""
# # Refatorando uma função
"""
#
# def quadrado(numero):
#     # return numero * numero
#     return numero ** 2
#
# print(quadrado(7))
# print(quadrado(2))
# print(quadrado(5))
#
# ret = quadrado(6)
# print(ret)

# def cantar_parabens(aniversariante):
#     print('Parabéns pra você')
#     print('Nesta data queria')
#     print('Muitas felicidades')
#     print('Muitos anos de vida')
#     print(f'Viva o/a {aniversariante}')
#     print(' ')
#
# cantar_parabens('Patricia')

"""
# # Funções podem ter n parametros de entrada. Ou seja, podemos receber como entrada
# # em uma função, quantos parâmetros forem necessários. Eles são separados por vírgula.
"""
#
# # Exemplos
#
# def soma(a, b): # a e b aqui são chamados parâmetros
#     return a + b
#
# def multiplica(num1, num2):
#     return num1 * num2
#
# def outra (num1, b, msg):
#     return(num1 + b) * msg
#
# print(soma(2, 5)) # 2 e 5 aqui são chamados de argumentos. Valores atribuídos aos parâmetros a e b
# print(soma(10, 20))
#
# print(multiplica(4, 5))
# print(multiplica(2, 8))
#
# print(outra(3, 2, 'Airton '))
# print(outra(5, 4, 'Cavalcante '))
#
# # OBS: Se a gente informar um número errado de parâmetros ou argumentos, teremos TypeError
#
# # print(soma(2, 3, 4)) # TypeError - Passando argumentos a mais
# # print(soma(4)) # TypeError - Passando argumentos a menos

"""
# Nomeando Parametros
"""
#
# def nome_completo(nome, sobrenome):
#     return f'Seu nome completo é {nome} {sobrenome}'
#
# print(nome_completo('Angelina', 'Jolie'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;


"""
# A ordem dos parâmetros importa!
"""
#
# def nome_completo(nome, sobrenome):
#     return f'Seu nome completo é {nome} {sobrenome}'
#
# nome = 'Felicity'
# sobrenome = 'Jones'
#
# print(nome_completo(sobrenome, nome))

"""
 # Argumentos nomeados
"""
#
# # Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# # utilizar qualquer ordem
#
# def nome_completo(nome, sobrenome):
#     return f'Seu nome completo é {nome} {sobrenome}'
#
# nome = 'Felicity'
# sobrenome = 'Jones'
#
# print(nome_completo(nome = 'Angelina', sobrenome = 'Jolie'))
# print(nome_completo(nome = nome, sobrenome = sobrenome))
# print(nome_completo(sobrenome = 'Marques', nome = 'Marcia'))

"""
# Erro comum na ultilização do return
"""
#
# def soma_impares(numeros):
#     total = 0
#     for num in numeros:
#         if num % 2 != 0:
#             total = total + num
#     return total
#
# lista = [1, 2, 3, 4, 5, 6, 7]
# print(soma_impares(lista))
#
# tupla = 1, 2, 3, 4, 5, 6, 7
# print(soma_impares(tupla))
