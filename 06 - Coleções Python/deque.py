"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.
"""
# Importando
from collections import deque

"""
# Criando Deques
"""
deq = deque('python')
print(deq)

"""
# Adicionando elementos no Deque
"""
deq.append(('y')) # Adiciona no final

print(deq)

deq.appendleft('k') # Adiciona no começo
print(deq)

"""
# # Remover elementos
"""
print(deq.pop()) # Remove e retorna o ultimo elemento
print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento
print(deq)
