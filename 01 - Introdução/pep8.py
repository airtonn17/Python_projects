"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Phyton

import this

A idéia da PEP8 é que possamos escrever códigos Python de forma Pythónica.


[1] - Ultilize Camel Case para nomes de classes;

class Calculadora:
    pass

class CalculadoraCientifica:
    pass


[2] - Ultilize nomes em minúsculo, separados por underlines para funções ou variáveis;

def soma():
    pass
def soma_dois():
    pass
numero = 4
numero_impar = 5


[3] - Ultilize 4 espaços para identação! (NÃO use tab)

if 'a' in 'banana':
    print('Tem')


[4] - Linhas em branco

- Separar funções e definicões de classes com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados por uma única linha em branco;


[5] - Imports devem sempre ser feitos em linhas separadas;

# Import Errado

import sys, os

#Import Certo

import sys
import os
from ctypes import SetPointerType

# Não há problemas em ultilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetPointe,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings
# Antes de constantes ou variáveis globais.


[6] - Espaços em expressões e instruções:

# Não faça:
funcao ( algo[ 1 ], { outro 2 })

# Faça:
funcao(algo[1], {outro 2})

# Não faça:
dict ['chave'] = lista [indice]

# Faça:
dictc['chave'] = lista[indice]

# Não faça:
x =              1
y =              3
variavel_longa = 5

# Faça:
x = 1
y = 3
variavel_longa = 5


[7] - Termine sempre uma instrução com uma nova linha

"""

import this

