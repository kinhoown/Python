'''
Escreva um programa que encontre o maior elemento em uma lista de palavras.
'''

lista = ['Erick','Livia','Maria','João','Deijair']
cont = ''
for palavra in lista:
    if len(palavra)> len(cont):
        cont = palavra

print(cont)