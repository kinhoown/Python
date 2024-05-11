"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    numero = int(input('Digite um numero inteiro: '))
    if numero % 2 == 0:
        print('Par')
    else:
        print('impar')

except:
    print('Não é um numero inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    hora = input('Digite as horas. Ex: 23:50 . ')
    if hora[2] == ':':
        x = int(hora[0] + hora[1])
        if (x >= 12) and (x <= 17):
            print('Bom dia!')
        elif (x > 0) and (x <= 12):
            print('Boa tarde!')
        else:
            print('Boa noite')
except:
    print('Isto não é um horario correto.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = len(input('Digite seu nome: '))

if nome <= 4 :
    print('Seu nome é curto')
elif nome > 6 :
    print('Seu nome é muito grande')
else:
    print('Seu nome é normal')