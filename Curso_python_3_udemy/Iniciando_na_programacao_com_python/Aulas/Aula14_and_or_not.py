'''
{and} siganifica (e),
{or} significa (ou) e 
{not} significa (não).
'''

#and
login = input('Login: ')
senha = input('Senha: ')

if login == 'erick' and senha == '12345':
    print('Acesso liberado!')
else:
    print('Acesso negado!')

#or
login = input('Login: ')
senha = input('Senha: ')

if (login == 'erick' or login == 'ERICK' or login == 'alexandre') and (senha == '12345'):
    print('Acesso liberado!')
else:
    print('Acesso negado!')

#not
'''
tudo que é positivo ele torna negativo.
tudo q é negativo torna porsitivo.

ex: not 10==10
    R: False

    not 10!=10
    R: True
'''