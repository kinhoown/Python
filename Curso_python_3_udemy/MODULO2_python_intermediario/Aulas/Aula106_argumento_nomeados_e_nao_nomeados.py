'''
Argumentos nomeados e não nomeados em função Python
Argumento nomeado tem nome com sinal de igual.
Argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x,y):
    print(f'x={x}\n{y=}')   #pode colocar x={x} ou {y=} que funciona do msm jeito.

soma(1,2)   #esse é o argumento não nomeado que so recebe o valor na orde que está la na função.
soma(y=69,x=86) #esse é um argumento nomeado. com ele vc diz pra onde esta indo cada valor sem ter uma orde correta.