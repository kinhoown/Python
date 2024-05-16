
                    #####-----1-----#####
'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Exite o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem se alcançados.
'''

x = 1

def escopo1():
    x = 10
    print(x)

escopo1()    #to chamando a função escopo e nem um x = 10. esse não é o x q está na raiz e sim uma nova vareavel x.
print(x)    #a vareavel x aqui é x = 1 pq o x q esta dentro do escopo não pode mudar o x q esta fora.




                    #####-----2-----#####
'''
Mas o escopo de dentro pode usar a variavel de fora.
'''

y = 100

def escopo2():
    z = 200
    print(y)

escopo2()
try:
    print(z)    #Aqui vai dar um NameError:. pos o valor z esta dentro do escopo. tem que esto no seu escopo ou no escopo interno para ser usado.
except:
    print('NameError:. pos o valor z esta dentro do escopo. tem que esto no seu escopo ou no escopo interno para ser usado.')




                    #####-----3-----#####
'''
Posso tornar uma variavel global. ela vai funcionar em todos os escopos.
'''

variavel = 30

def escopo3():
    global variavel #aqui estou tornando a variavel variavel em uma variavel global.
    variavel = 69
    print(variavel)
print(variavel) #aqui a variavel ainda não foi altera pos o escopo ainda não foi chamado.
escopo3()   #aquei acontece a chamada do escopo fazen ele tornar a variavel global e trocando ela por outro valor.
print(variavel) #aqui o valor ja foi alterado.
