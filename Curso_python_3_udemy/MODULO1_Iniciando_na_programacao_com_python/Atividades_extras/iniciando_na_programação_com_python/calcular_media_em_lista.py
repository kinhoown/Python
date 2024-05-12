'''
Crie um programa que receba uma lista de números e retorne a média dos valores presentes na lista.
'''

#lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
try:
    lista_de_numeros = []
    while True:
        start_stop = input('Você quer adicionar um numero?\nDigite apenas [S] para sim e [N] para não.\n            ').upper()
        if start_stop == 'S':
            numero_do_usuario = int(input('Digite o numero: '))
            adicionar_numero_na_lista = lista_de_numeros.append(numero_do_usuario)

        elif start_stop == 'N':
            soma_dos_numeros = 0

            for numero in lista_de_numeros:
                soma_dos_numeros += numero

            media = soma_dos_numeros / len(lista_de_numeros)
            print(f'Sua media é : {media}')
            print('O programa vai ser encerrado!')
            break
        else:
            print('Erro: Digite uma letra valida.')
except ValueError:
    print('Erro: Digite apenas números interios.')
