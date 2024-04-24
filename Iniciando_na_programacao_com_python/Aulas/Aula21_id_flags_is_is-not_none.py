#id
'''
id vai dizer o numero do id da variavel na memoria.
'''

variavel_1 = 'a'
variavel_2 = 'a'
variavel_3 = 'b'

print(id(variavel_1))
print(id(variavel_2))
print(id(variavel_3))

'''
R:  140734488026336
    140734488026336
    140734488027392

    ele usa o msm local da memoral pra variaveis com o msm valor. como vemos na resposta 1 e 2.
'''

#Flags
'''
Flags (Sinalizadores): O termo "flags" geralmente se refere a variáveis que são usadas como indicadores ou sinalizadores em um programa para controlar seu fluxo. Essas variáveis geralmente têm valores booleanos (verdadeiro ou falso) e ajudam a controlar o comportamento do código.
'''

#is  e  is not
'''
is e is not: Em Python, is e is not são operadores de identidade que verificam se dois objetos têm o mesmo ou diferentes endereços de memória, respectivamente. Eles são diferentes dos operadores == e !=, que verificam se os valores dos objetos são iguais ou diferentes. O uso de is é comum ao lidar com objetos imutáveis como None.
'''

#none
'''
None: None é um valor especial em Python que representa a ausência de valor. É comumente usado para inicializar variáveis antes de atribuir um valor real a elas. Além disso, pode ser usado em verificações de condição para indicar que uma variável não foi definida ou que não possui um valor específico.
'''




# Exemplo de Flags e None
flag = True  # Flag como indicador

if flag is True:
    print("A flag está ativada.")
else:
    print("A flag está desativada.")

# Exemplo com None
nome = None

if nome is None:
    print("O nome ainda não foi definido.")
else:
    print("O nome é:", nome)