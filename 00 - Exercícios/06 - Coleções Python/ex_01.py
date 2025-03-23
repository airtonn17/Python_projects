"""
Crie um programa que lê 6 valores inteiros,
armazena em uma lista e em seguida mostre na tela os valores lidos
"""
valores = []

for i in range(6):
    valor = input(f'Digite o valor {i + 1}: ')
    valores.append(valor)
lista = [(valores)]
print(valores)
