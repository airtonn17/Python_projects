"""
Tipo Foat
Tipo Real, Decimal
Casas Decimais

OBS: O separador de casas decimais na programação é o ponto e não a vírgula
"""

# Errado
valor = 1,44

# Certo
valor = 1.44

# É possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiro, nós perdemos precisão
"""
res = int(valor)
print (res)
print (type(res))

# Podemos trabalhar com numeros complexos
var = 5j
print(type(var))
