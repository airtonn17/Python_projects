"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com o loop for.

Ranges ~sao ultilizados para gerar sequências numérica, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1
range(valor_de_parada)
OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Forma 2
range (valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

# Forma 3
raneg (valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Forma 4 (Inversa)
raneg (valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

"""
# Exemplo Forma 1
for numero in range(11): # 0 ao 10
    print(numero)

# Exemplo Forma 2
for numero in range (1,11): # 1 ao 10
    print(numero)

# Exemplo Forma 3
for numero in range(1, 10, 2): # 1, 3, 5, 7, 9
    print(numero)

# Exemplo Forma 4
for numero in range(10,0,-1): # Contagem ivertida - Do 10 ao 1
    print(numero)
