"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

if numero1 > numero2:
    print(f"O numero {numero1} eh maior que {numero2}")
elif numero1 == numero2:
    print(f"Os numeros {numero1} e {numero2} sao iguais.")
else:
    print(f"O numero {numero2} eh maior que {numero1}")