"""
Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui.
"""
lista = []

for i in range(10):
    valores = input('Digite um valor: ')
    lista = lista + [valores]
print(lista)
