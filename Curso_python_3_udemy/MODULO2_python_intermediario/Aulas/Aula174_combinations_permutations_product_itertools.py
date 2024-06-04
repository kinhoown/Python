# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]
    #print_iter(list(combinations(pessoas, 2))) coloco sempre list se não vai ser so um valor salvo na memoria
     
print_iter(combinations(pessoas, 2))    #as combinações não vão se repetir ex: joão e luiz não pode ser luiz e joão
print_iter(permutations(pessoas, 2))    #as combinações podem se repetir ex: joão e luiz vai aparecer tambem luiz e joão.
print_iter(product(*camisetas)) #é usado para quando tem listas dentro de listas.