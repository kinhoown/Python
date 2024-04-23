
# f-strings

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'

print(linha_1)
print(linha_2)
print(f'{imc:.2f}')


#format strings

#teste1
a = 'A'
b = 'B'
c = 1.1
formato = 'a = {}, b = {}, c = {:.2f}'.format(a,b,c)

print(formato)

#teste2
nome = 'Erick Alexandre'
lugar = 'Brasil'
objeto = 'teclado'

print('meu nome é {}, gosto do meu pais {} e tenho um {} muito legal. meu IMC é {:.2f}'.format(nome,lugar,objeto,imc))

#teste3
a = 'oi'
b = 'tim'
c = 'claro'

formato = 'essa é a {oper3}, essa é a {oper1} e essa é a {oper2}.'.format(oper1=a,oper2=b,oper3=c)
print(formato)