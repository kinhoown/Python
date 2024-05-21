#149-(part 1) try e except para tratar exceções.

''' try, except e finally'''

try:
    a = 1
    #b = 0
    c = a/b
    print(c)

except NameError:   #aqui estou tratando um erro 
    print('Faça isso pq deu erro no nome da variavel')
    #vai continuar acontecendo erro pos so foi tratado um erro e ainda tem outro erro o erro: ZeroDivisionError e para tratar esse erro temos q criar outro except
except ZeroDivisionError:
    print('Faça isso pq deu erro 0 nao pode ser divisivel.')

except Exception:   #aqui é uma clase de erro q junta todos os erros. se vc ja sabe todos os pissiveis erros pode colocar isso se nao vai descobnrindo qual os erros e tratando.
    print('ERRO DESCONHECIDO.')


#150-(part 2) try e except para tratar exceções.

'''
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')
'''