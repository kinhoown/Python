def soma(x,y):
    return x+y

def mult(x,y):
    return x*y

def executar(funcao,x):
    def interna(y):
        return funcao(x,y)
    return interna

soma_33 = executar(soma, 33)
mult_777 = executar(mult, 777)

print(soma_33(10))
print(mult_777(10))