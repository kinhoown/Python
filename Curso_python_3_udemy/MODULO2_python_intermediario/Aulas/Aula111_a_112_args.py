'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''

#lembrete de desempacotamento

x,y,*resto = 1,2,3,4,5,6,7,8,9,10

print(x,y,resto)



def soma(*args):    #quando coloco *args eu to agrupando tudo q vai ser lançado pra esse arguimento soma() em uma tupla.
    for i in args:
        print(i)
    
soma(1,2,3,4,5,6,7,8,9,10)