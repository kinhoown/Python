pessoa = {}
nome = input('Digite seu nome: ')
pessoa['nome'] = nome
print(pessoa)


pessoa['nome'] = 'Livia'    #alterando o nome da pessoa
print(pessoa)


del pessoa['nome']  #pagar uma chave do dicionario
print(pessoa)


print(pessoa.get('nome'))   # .get('o parametro usado') é usando para tratar um erro. se não tem um nome no dicionario ele volta None.  se não colocar o .get() o algoritimo vai quebrar.

if pessoa.get('nome') is None:
    print('NÃO EXITE UM NOME.')
else:
    print(f'EXITE UM NOME. {pessoa['nome']}')