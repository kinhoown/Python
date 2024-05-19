'''
Closure e fuções que retornam outras funções.
'''

def criar_saudacao(saudacao):   #saudação pode ficar fixa
    def saudar(nome):   #ja nessa função o nome da pessoa pode ser varios
        return f'{saudacao}, {nome}!'
    return saudar   #o retorno da função so vai receber o parametro fora da função

falar_bomdia = criar_saudacao('Bom dia')
falar_boanoite = criar_saudacao('Boa noite')
print(falar_bomdia('Erick'))    #aqui esta passando o paremetro pra função saudar
print(falar_boanoite('Erick'))  #aqui esta passando o paremetro pra função saudar
