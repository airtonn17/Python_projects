"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis Globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis Locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja,
    seu escopo está limitado ao bloco foi declarada.

Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Pyton é uma liguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável , nós não colocamos o dtipo de dado dela.
Esse tipo é inferido ao atribuirmos o valor a mesma.

Exemplo em C ou Java:
int numero = 42;

# Reatrinuição

"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

numero = 2
# novo = 0 -> Condição para a variável funcionar fora o if, sendo declarada no escopo global.
if numero > 10:
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do blco if. Portanto é local
    print(novo)

# print(novo) # Só será impresso se a condição for verdadeira, pois se der falso a variáveil nunca existiu
