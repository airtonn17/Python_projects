"""
Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui.
"""
"""
# # Minha Solução
"""
lista: list[int] = []
pares: int = 0

while len(lista) < 10:
    valor: int = int(input(f'Digite o valor {len(lista) + 1}/10: '))
    lista.append(valor)

for valor in lista:
    if valor % 2 == 0:
        pares = pares + 1

if pares > 0:
    print(f'A lista {lista}, possue {pares} pares')
else:
    print(f'A lista {lista} não possue valores pares')

"""
# # Solução do Professor
"""
# lista: list[int] = []
# contador_pares: int = 0
#
# while len(lista) < 10:
#     valor: int = int(input(f'Informe o valor {len(lista) + 1}/10: '))
#     lista.append(valor)
#
#     if valor % 2 == 0:
#         contador_pares = contador_pares + 1
#
#
# if contador_pares > 0:
#     print(f'A lista {lista} possui {contador_pares} pares.')
# else:
#     print(f'A lista {lista} nao possui valor pares.')
