'''
Implemente um programa que verifique se uma palavra é um palíndromo, ou seja, se pode ser lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda.
'''
while True:
    palavra = input('Digite uma palavra: ').upper()
    cont = len(palavra)-1
    palindromo = ''.upper()
    while cont>=0:
        palindromo += palavra[cont]
        cont -= 1

    res = 'Sua palavra é um Palíndromo.' if palindromo == palavra else 'Sua palavra não é um Palíndromo.'
    print(res)
    continuar = input('Deseja continuar?\nDigite [S]im para continuar e qualquer coisa pra Não.').upper()
    if continuar == 'S':
        continue
    else:
        print('O programa vai ser fechado.')
        break