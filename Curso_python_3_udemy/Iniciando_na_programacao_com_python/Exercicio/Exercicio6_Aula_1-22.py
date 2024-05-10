# #atividade 1 aula 64 e 65

# nome = input('Digite seu nome: ')
# cont = 0
# nome_res = ''
# while len(nome) > cont:
#     nome_res = nome_res + (f'*{nome[cont]}')
#     cont +=1
# print(nome_res)

# #atividade 2 aula 66

numero_1 = float(input('Numero: '))
operador = input('Operador: ')
numero_2 = float(input('Numero: '))

if operador == '+':
    print(numero_1 + numero_2)
elif operador == '-':
    print(numero_1 - numero_2)
elif operador == '*':
    print(numero_1 * numero_2)
elif operador == '/':
    print(numero_1 / numero_2)