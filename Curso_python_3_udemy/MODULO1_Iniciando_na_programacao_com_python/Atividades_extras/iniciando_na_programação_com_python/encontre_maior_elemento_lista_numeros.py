'''
Escreva um programa que encontre o maior elemento em uma lista de números.
'''

lista = [1,2,3,4,5,6,7,8,9,10]
cont = 0
for n in lista:
    if n > cont:
        cont = n
print(cont)