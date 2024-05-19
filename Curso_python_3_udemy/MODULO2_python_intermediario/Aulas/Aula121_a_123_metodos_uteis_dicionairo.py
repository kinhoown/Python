# Métodos úteis dos dicionários em Python
'''
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
'''
import copy
pessoa = {
    'nome': 'Erick',
    'sobrenome': 'Lima',
}




'''
print(len(pessoa))


print(list(pessoa.keys()))


print(list(pessoa.values()))


print(list(pessoa.items()))


pessoa.setdefault('idade', 'não tem idade') se não tiver idade vai se colocado 'não tem idade'.
'''

#Shallow Copy  vs  Deep Copy em dados mutáveis
'''
- Shallow Copy uma copia rasa
se dentro do dicionario tiver uma lista ou algo assim ele não vai ser copiado o q o python vai fazer é apontar pro msm lugar da memoria. se alterar o valor em uma lista dentro de um dicionario vai ser alterado nos dois dicionarios.

- Deep Copy uma copia profunda
faz a copia completa contando as litas e tuplas q estam dentro do dicionario.
lado negativo é q se for algo muito grande pode atrapalhar seu codigo e deixar ele pesado na hr de processar.
'''
'''
SHALLOW COPY

pessoa_2 = pessoa.copy()
pessoa_2['nome'] = 'Livia'
print(pessoa_2['nome'])
'''
'''
DEEP COPY

tem q ter um import copy no inicio do codigo

pessoa_2 = copy.deepcopy(pessoa)
print(pessoa_2)
'''

'''
print(pessoa.get('nome', 'o valor nao exite'))  #ou usa None no lugar do 'o valor nao exite'   #usar no lugar do   -   print(pessoa['nome'])


apagar = pessoa.pop('nome')
print(apagar)
print(pessoa)
ele apaga a chave mas ainda consigo utilizar


apagar_ultima_chave = pessoa.popitem()
print(apagar_ultima_chave)
print(pessoa)
ele apaga a ultima chave mas ainda consigo ultilizar


pessoa.update({
    'nome' : 'Deijair',
    'sobrenome' : 'Tompson',
    'idade' : 69,
    'endereço' : [
        {'rua' : 'Amelia', 'numero' : 24},
        {'rua' : 'Temelo o Rego', 'numero' : 64}
    ]
})
print(pessoa)
consigo tanto alterar o q ja tem tanto quanto acrecentar coisas novas ao meu dicionario
'''
pessoa.update({
    'nome' : 'Deijair',
    'sobrenome' : 'Tompson',
    'idade' : 69,
    'endereço' : [
        {'rua' : 'Amelia', 'numero' : 24},
        {'rua' : 'Temelo o Rego', 'numero' : 64}
    ]
})
print(pessoa)