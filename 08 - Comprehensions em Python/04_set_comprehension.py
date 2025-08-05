"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}

"""

"""
# Exemplos
"""

numeros = {num for num in range(1, 7)}
print(numeros)

numeros = {x ** 2 for x in range(10)}
print(numeros)

# DESAFIO! Faça uma alteração na estrutura acima para gerar um dicionário ao invés de set

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Pra finalizar

letras = {letra for letra in 'Pytho Project'}
print(letras) # Imprime todos os caracteres sem repetição e sem ordenação


