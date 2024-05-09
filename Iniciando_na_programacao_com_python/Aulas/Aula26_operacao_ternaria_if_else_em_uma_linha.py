"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
#exemplo 1
condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)


#exemplo 2
'''
digito = 9  # > 9 = 0
novo_digito = digito if digito <= 9 else 0 #esse
novo_digito = 0 if digito > 9 else digito #ou esse
print(novo_digito)
'''


#exemplo 3
'''
print('Valor' if False else 'Outro valor' if False else 'Fim')'''