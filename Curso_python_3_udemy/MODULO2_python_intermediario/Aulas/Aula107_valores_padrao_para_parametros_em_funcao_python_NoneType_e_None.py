'''
Valores padrão para parâmetro
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
'''

def soma(x,y,z=None):
    res = x+y   #se atentar que quanto o codigo é lido ele ainda não recebeu o numero pro z ent ele não pode esta assim --> res = x+y+z pos da TypeError:.
    if z is None:
        print('Não foi atribuido um número a variavel Z.')
    else:
        print(f'Foi atribuido um numero a Z e o reltado da conta é {res + z}.')
soma(1,2)
soma(2,2)
soma(1,3)
soma(3,3)
soma(1,2,3)

'''
isso pode ser usado pra saber se recebeu um numero ou não.
'''