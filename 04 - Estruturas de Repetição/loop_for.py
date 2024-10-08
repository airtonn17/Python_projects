"""
Loop for

Loop -> Estrutura de Repetição.
For -> Uma dessas estruturas.,

for item in interavel:
    //execução do loop

Ultilizamos loops para interar sequências ou sobre varoles interáveis.

Exemplos de interáveis:
- String -> nome = 'Python Project'
- Lista -> lista = [1, 3, 5, 7, 9]
- Range -> numero = range(1, 10)

Tabela de Emojis Unicodes: https://apps.timwhitlock.info/emoji/tables/unicode
"""
nome = 'Python Project'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10) # Temos que tranformar em uma lista

# Exemplo de for 1 -> Interando em uma String
# for letra in nome:
#     print(letra)

# Exemplo de for 2 -> Interando sobre uma lista
# for numero in lista:
#     print(numero)

# Exemplo de for 3 -> Interando sobre um range
"""
range (valor_inicial, valor_final)
OBS: O valor final não é incluso.
1
2
3
4
5
7
8
9
10 - Não
"""
# for numero in range (1, 10):
#     print(numero)

# for indice, letra in enumerate(nome):
#     print(nome[indice])

# for indicie, letra in enumerate(nome):
#     print(letra)

# Quando não precisamos de um valor, podemos descarta-lo ultilizando um underline (_)
# for _, letra in enumerate(nome):
#     print(letra)

# for valor in enumerate(nome):
#     print(valor)

# qtd = int(input('Quantas vezes esse loop deve rodar: '))
# soma = 0
#
# for n in range(1, qtd+1):
#     num = int(input(f'informe o {n}/{qtd} valor: '))
#     soma = soma + num
# print(f'A soma é {soma}')

# for letra in nome:
#     print(letra, end='') # Para não pular linhas

# Original: U+1F60D
# Modificado: U0001F60D

for _ in range(3):
    for num in range(1,11):
        print('\U0001F63B' * num ) # Imprimir Emoji, troca o '+' por '000'
