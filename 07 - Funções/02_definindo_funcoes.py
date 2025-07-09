"""
Definindo Funções

- Funções são pequenos partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados
- São muito uteis para executar procedimentos similares por repedidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

- Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.

# Mas então, como definir funções?

# Em Python a forma geral de definir uma função é:

def nome_da_funcao (parametro_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se form nome composto, separado por underline (Snake Case);
parâmetros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função utilizamos a palavra reservada 'def', informando ao Python que
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é
utilizado em Python para definir blocos.

"""


"""
# Exemplo de utilizaçao de Funções
"""
#
# cores = ['verde', 'amarelo', 'azul', 'branco']
#
# # Utilizando a funçao integrada (Built-in) do Python print()
#
# print(cores)
#
# curso = 'Programação em Python: Essencial'
#
# print(curso)
#
# cores.append('roxo')
#
# print(cores)
#
# # curso.append('Mais dados...') # AttributeError
# # print(curso)
#
# cores.clear()
# print(cores)


"""
# Difinindo a primeira função
"""
#
# # Definição
# def diz_oi():
#     print('oi')

# OBS:
# 1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
# 2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
# 3 - Veja que esta função não recebe nenhum parametro de entrada;
# 4 - Veja que esta função não retorna nada.


"""
Ultilizando função
"""
#
# # Chamada de execução
# diz_oi()

"""
ATENÇÃO:
"""
#
# Nunca esqueça de utilizar o parêntese ao executar uma função.
#
# Exemplo 1:
#
# # Errado!
# diz_oi
#
# # Certo
# diz_oi()
#
# # Errado!
# diz_oi ()


# Exemplo 2
def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data queria')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')
    print(' ')

# for n in range (5):
#     cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável

canta = cantar_parabens
canta()
