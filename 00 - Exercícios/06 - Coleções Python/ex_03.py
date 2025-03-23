"""
Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui.
"""
"""
# # Minha Solução
"""
# lista = []
#
# for i in range(10):
#     valores = input('Digite um valor: ')
#     lista = lista + [valores]
# print(lista)

"""
# # Solução do Professor
"""
lista: list[int] = []
contador_pares: int = 0

while len(lista) < 10:
    valor: int = int(input(f'Informe o valor {len(lista) + 1}/10: '))
    lista.append(valor)

    if valor % 2 == 0:
        contador_pares = contador_pares + 1


if contador_pares > 0:
    print(f'A lista {lista} possui {contador_pares} pares.')
else:
    print(f'A lista {lista} nao possui valor pares.')
