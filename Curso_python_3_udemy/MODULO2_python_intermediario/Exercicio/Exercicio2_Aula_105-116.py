'''
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
'''

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

entrada = float(input('Digite um numero:'))
print(duplicar(entrada))
print(triplicar(entrada))
print(quadruplicar(entrada))