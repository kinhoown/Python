'''
list comprehension é uma forma rápida para criar uma lista
'''

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)    #isso seria uma forma normal de criar uma lista

#list comprehension
        #aqui ----V eu to falando o que quero q seja atribuido a minha lista
nova_lista = [novo_numero for novo_numero in range(10)]
print(nova_lista)   #se conporta do msm jeito da lista anterior 
