'''
Implemente um programa que verifique se um número é primo, ou seja, se é divisível apenas por 1 e por ele mesmo.
'''

numero = int(input('Digite um numero: '))
divisivel = [1,2,3,5]

while True:
    if numero in divisivel:
        print('Seu número é um número primo.')
        break
    for n in divisivel:
        if n == 1:
            continue
        elif (numero % n)==0:
            print('Seu número não é um número primo.')
            break
        elif n == 5:
            print('Seu número é um número primo.')
            break
