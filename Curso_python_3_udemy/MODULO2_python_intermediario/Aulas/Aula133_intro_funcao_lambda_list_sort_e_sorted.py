'''
Introdução à função lambda (função anônima de uma linha)
A função lambda é uma função como qualquer
outra em Python. Porém, são funções anônimas
que contém apenas uma linha. Ou seja, tudo
deve ser contido dentro de uma única
expressão.


--- Esse serve para ordenar umas lista de numeros ---
mas esse não é o caso dessa aula.
lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
lista.sort(reverse=True)
print(lista)
'''
listas = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

listas.sort(key=lambda item: item['nome'])
for lista in listas:
    print(lista)