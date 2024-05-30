'''
na atividade 6 podemos ver isso melhor
'''

    #################################

'''
def fora(x):    #função pincipal
    a = x

    def dentro():   #função para parar o andamento da primeira função
        return a
    return dentro

dentro1 = fora('erick') #dentro1 se torna uma função por isso temos q chamar ela como se tivesse chamando uma função na linha 14.

print(dentro1())
'''

    #   #   #   #   #   #   #   #   #   

'''
se fizer nessa forma vai dar um erro de -> UnboundLocalError: cannot access local variable 'valor_a_ser_adicionado' where it is not associated with a value

def concatenar(string_inicial):
    valor_a_ser_adicionado = string_inicial    #essa variavel é desse escopo

    def interna(valor_a_concatenar):

        valor_a_ser_adicionado += valor_a_concatenar    #por isso não consegue ser modificada aqui. so consegue visualizar, utilizala mas não consegue modificala. para modificar tem q usar ---> nonlocal nome_da_variavel
        ai com isso vc consegue trazer a variavel completamente para o escopo.
        return valor_a_ser_adicionado
    return interna

str_inicial = concatenar('a')
print(str_inicial('b'))
print(str_inicial('c'))
print(str_inicial('d'))
print(str_inicial('e'))
'''


def concatenar(string_inicial):
    valor_a_ser_adicionado = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_a_ser_adicionado
        valor_a_ser_adicionado += valor_a_concatenar
        return valor_a_ser_adicionado
    return interna

str_inicial = concatenar('a')
print(str_inicial('b'))
print(str_inicial('c'))
print(str_inicial('d'))
print(str_inicial('e'))