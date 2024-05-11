"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


'''cpf = '746.824.890-70'.replace(".", "").replace("-", "")'''
# while True:
#     cpf = input('Digite seu CPF: EX: xxx.xxx.xxx-xx  ').replace(".", "").replace("-", "")
#     try:
#         cont1 = 0
#         cont2 = 10
#         soma = 0
#         while cont2 >= 2:
#             mult = int(cpf[cont1]) * cont2
#             soma += mult
#             cont1 += 1
#             cont2 -= 1
#         res_mult = (soma * 10)%11

#         primeiro_digito = 0 if res_mult > 9 else res_mult

#         print(f'O primeiro digito do CPF é {primeiro_digito}.')
#     except:
#         print('Digite seu CPF: EX: xxx.xxx.xxx-xx\n!!!!!!!!!!APENAS NUMEROS!!!!!!!!!!')


"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import os
while True:
    try:
    #digito 1

        cpf = input('Digite seu CPF: EX: xxx.xxx.xxx-xx  ').replace(".", "").replace("-", "")
        os.system('cls')
        nove_primeiros_digitos = cpf[:9]
        cont_digito_1 = 10
        soma_digito_1 = 0
        for n in nove_primeiros_digitos:
            soma_digito_1 += int(n)*cont_digito_1
            cont_digito_1 -= 1
        mult_soma_digito_1 = (soma_digito_1 * 10)%11
        res_primeiro_digito = 0 if mult_soma_digito_1 > 9 else mult_soma_digito_1

    #digito 2

        dez_primeiros_digitos = cpf[:10]
        cont_digito_2 = 11
        soma_digito_2 = 0
        for n_2 in dez_primeiros_digitos:
            soma_digito_2 += int(n_2)*cont_digito_2
            cont_digito_2 -= 1
        mult_soma_digito_2 = (soma_digito_2 * 10)%11
        res_segundo_digito = 0 if mult_soma_digito_2 > 9 else mult_soma_digito_2

        if res_primeiro_digito == int(cpf[-2]) and res_segundo_digito == int(cpf[-1]):
            print('Seu CPF é valido!')
        else:
            print('CPF invalido!')
    except:
        print('Digite seu CPF: EX: xxx.xxx.xxx-xx\n!!!!!!!!!!APENAS NUMEROS!!!!!!!!!!')