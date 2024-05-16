
                    #####-----1-----#####
'''
Introdução as funções (def) em Python
Funções são trechos de código usado para replicar detrerminada ação ao longo do seu código.
'''

def isso_e_uma_funcao():
    print('isso esta contecendo dentro da minha função.\n\n')

isso_e_uma_funcao()# Dessa forma estou chamando minha função.




                    #####-----2-----#####
'''
A função pode receber valores para parâmetros (argumentos) e retornar um valor específico.
'''

def isso_e_uma_funcao_com_parametro(a,b,c):
    print('Isso está acontecendo dentro da minha função com parametro.')
    '''
    posso usar os valores do parametro dentro da função
    '''
    print(a+b)
    print(a-c)

isso_e_uma_funcao_com_parametro(1,2,3)# Dessa forma estou chamando minha função, aplicando o parametro a ela.





                    #####-----3-----#####
'''
Com tudo isso posso esta colocando variaveis dentro da função.
'''

nome = input('- Nome: ')
idade = int(input('- Idade: '))
sexo = input('- Sexo: ')

def cadastro(n,i,s):
    print(f'Meu nome é {n}, tenho {i} anos e sou do sexo {s}.')

cadastro(nome,idade,sexo)




                    #####-----4-----#####
'''
se eu nao passar um parametro ele da erro TypeError:. ent podemos dizer que se não passarmos um parametro ele faça isso.
'''

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Erick')   #nesse eu passei o parametro e ele vai usar 'erick'.
saudacao()          #nesse eu não passei um nome pro parametro e por isso ele vai usar o 'Sem nome'.