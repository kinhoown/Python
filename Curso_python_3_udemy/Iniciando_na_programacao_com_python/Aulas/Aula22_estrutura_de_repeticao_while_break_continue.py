'''
while signifa enquanto.
ex: enquanto uma coisa acontecer ou for uma coisa True faça isso -> ...
'''

entrada = int(input('Digite: '))
contador = 0
while entrada >= contador :
    contador +=1
    if (contador % 2) == 0:
        print('Par')
        continue
    print(contador)
    if contador == entrada / 2 :
        break



#while dentro de while

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1


print('Acabou')