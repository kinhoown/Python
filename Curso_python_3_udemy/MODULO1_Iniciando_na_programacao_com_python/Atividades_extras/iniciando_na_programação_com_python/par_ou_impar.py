'''
Desenvolva um programa que receba um número como entrada e determine se ele é par ou ímpar.
'''
try:
    numero = float(input('Digite um numero: '))
    par_ou_impar = 'Par' if (numero % 2) == 0 else 'Ímpar'
    print(par_ou_impar)
except ValueError:
    print('Erro: Digite apenas numeros.')