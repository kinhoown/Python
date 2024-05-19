pessoa = {
    'nome' : 'Erick',
    'sobrenome' : 'Lima'
}
'''
a, b = pessoa   #aqui vai me passar o nome da chave
c, d = pessoa.values()  #aqui vai me passar o valor da chave
(e1,e2), f = pessoa.items()   #aqui vai me passar um tupla de com a chave e o valor dentro
for chave, valor in pessoa.items(): #pode ser dessa forma tambem
    print(chave, valor)
'''

#---unir dicionarios ---#

dados_pessoais = {
    'idade' : 26,
    'altura' : 1.69
}


dados_competos = {**pessoa, **dados_pessoais}

print(dados_competos)