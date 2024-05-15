'''
Desenvolva uma função que calcule o valor final de um investimento com base em uma taxa de juros e um período de tempo.
'''
try:
    investimento = float(input('Valor de investimento.: '))
    juros = float(input('Porcentagen mensal.: '))
    tempo = int(input('Meses de investimento.: '))
    valor_do_juros = investimento
    for i in range(tempo):
        calculo_do_juros = ((valor_do_juros*juros)/100)
        valor_do_juros += calculo_do_juros
    print(valor_do_juros)
except ValueError:
    print('ValueError: Não é um valor valido.')