# Exercícios com funções

#Exercicio--1--
'''
Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável.
'''
x = [1,2,3,4,5,6,7,8,9,10]

def mult(*args):
    multiplicador = 1
    for n in args:
        multiplicador *= n
    return multiplicador

print(mult(*x))


#Exercicio--2--
'''
Crie uma função que fala se um número é par ou ímpar e retorne se o número é par pu ímpar.
'''