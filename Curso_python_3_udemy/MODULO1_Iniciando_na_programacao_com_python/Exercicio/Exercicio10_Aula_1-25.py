import os

lista_de_compras = []
while True:
    funcao = input('Selecione uma opção \n [i]nserir [a]pagar [l]istar: \n').lower()
    if funcao == 'i':
        os.system('cls')
        inserir = input('O que deseja inserir?\n: \n').capitalize()
        os.system('cls')
        lista_de_compras.append(inserir)

    elif funcao == 'a':
        os.system('cls')
        try:
            apagar = int(input('O que deseja apagar ?\nDigite a posição do item.\n: \n'))
            if apagar > (len(lista_de_compras)-1):
                print('Esse item não existe!!!\n')
            else:
                lista_de_compras.pop(apagar)
        except:
            print('Esse item não existe!!!\nPor favor digite um numero!!!')

    elif funcao == 'l':
        os.system('cls')
        if len(lista_de_compras) == 0:
            print('Sua lista de compras está vazia!!!\n')
        else:
            for indice, nome in enumerate(lista_de_compras):
                print(indice, nome)
    else:
        print('Digite i, a ou l.')