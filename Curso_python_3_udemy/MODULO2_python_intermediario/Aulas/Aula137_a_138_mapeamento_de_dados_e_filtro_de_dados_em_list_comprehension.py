    #MAPEAMENTO DE DADOS EM LIST COMPREHENSION

produtos = [
    {'nome' : 'p1', 'preco' : 10,},
    {'nome' : 'p2', 'preco' : 20,},
    {'nome' : 'p3', 'preco' : 30,},
]

novos_produtos = [
    {**produto, 'preco' : produto['preco'] * 2}
    if produto['preco'] < 30 else {**produto}
    for produto in produtos
    ]
print(*novos_produtos, sep='\n')
    #mapeamento é pra criar uma nova lista alterando os dados q estam dentro

#-----------------------------------------------------------------------------------------------------------------------------------
def pular_linhas(p):
    print()
for p in range(10):
    pular_linhas(p)
#-----------------------------------------------------------------------------------------------------------------------------------

    #FILTRO DE DADOS EM LIST COMPREHENSION

lista = [n for n in range(10) if n > 4]
print(lista)

    #filtro é a condição dps do FOR