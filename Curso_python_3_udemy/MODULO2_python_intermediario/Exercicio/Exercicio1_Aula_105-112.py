# Exercícios com funções

#Exercicio--1--
'''
Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável.
'''

x = []
while True:
    validacao = input('Quer adincionar um número?\nDigite [S]im ou qualquer coisa para Não.').upper()
    if validacao == 'S':
        entrada = int(input('Digite um número inteiro.: '))
        x.append(entrada)
    else:
        break

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

def par_impar(numero):
    return f'{numero} é um número par!'if (numero%2)==0 else f'{numero} é um número ímpar!'

while True:
    entrada = int(input('Digite um número inteiro: '))
    print(par_impar(entrada))
