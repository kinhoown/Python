'''
Calcule o fatorial de um número dado como entrada.
'''
while True:
    try:
        numero = int(input('Digite apenas numeros inteiros: '))
        cont = numero
        res = numero
        while cont > 1:
            res = (res * (cont-1))
            cont -= 1
        print(res)
        continuar = input('Deseja calcular outro fatorial ?\nDigite [S]im ou qualquer coisa pra Não.').upper()
        if continuar == 'S':
            continue
        else:
            print('Você saiu do programa.')
            break
    except ValueError:
        print('Erro: Digite apenas numeros inteiros.')
    
