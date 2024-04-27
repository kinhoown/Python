nome = input('Digite seu nome: ')
cont = 0
nome_res = ''
while len(nome) > cont:
    nome_res = nome_res + (f'*{nome[cont]}')
    cont +=1
print(nome_res)