'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

ganha_po_hora = float(input('Valor pago por hora.: '))
horas_trabalhadas = int(input('Quantas horas trabalhadas por mês.: '))

total_do_salario = ganha_po_hora * horas_trabalhadas

print(total_do_salario)