import os
import copy
os.system('cls')

entrada1 = int(input('Digite um numero inteiro: '))
entrada2 = int(input('Digite um numero inteiro: '))

def pular():
    print('')
pular()

def soma(x,y):
    return x+y
resultado = soma(entrada1,entrada2)
print(resultado)
pular()

lista_dicionario = [
    {'nome': 'erick','lugar': 'Brasil', 'objeto': 'teclado'},
]

lista_dicionario2 = copy.deepcopy(lista_dicionario)
print(lista_dicionario2)
pular()

lista_dicionario3 = [dicionario for dicionario in lista_dicionario]
print(lista_dicionario3)
pular()

lista_dicionario4 = lista_dicionario.copy()
print(lista_dicionario4)
pular()

