"""
3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.
"""

n1 = int(input('Digite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))
n3 = int(input('Digite o terceiro valor inteiro: '))

soma_dos_quadrados: int = ((n1*n1) + (n2*n2) + (n3*n3))
print(f'A soma dos quadrados dos valores {n1}, {n2} e {n3} é: {soma_dos_quadrados}')
