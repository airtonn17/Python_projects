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

"""

# Exemplo de utilizaçao de Funções

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a funçao integrada (Built-in) do Python print()

print(cores)

curso = 'Programação em Python: Essencial'

print(curso)

cores.append('roxo')

print(cores)

# curso.append('Mais dados...') # AttributeError
# print(curso)

cores.clear()
print(cores)