import json

# json.dump = Gera um arquivo json
'''
pessoa = {
    'nome' : 'Erick Lima',
    'enderecos' : [
        {'rua' : 'joaquim joaquina', 'numero' : 171},
        {'rua' : 'tio patinhas', 'numero' : 696},
    ],
    'altura' : 1.69,
    'numeros_preferidos' : (1,2,3,4,5,6,7,8,9,0),
    'dev' : True,
    'nada' : None,
}

caminho_arquivo = 'C:\\ESTUDOS\\Python\\Curso_python_3_udemy\\MODULO2_python_intermediario\\'
caminho_arquivo += 'arquivo_teste_json.json'
with open(caminho_arquivo, 'w+') as arquivo:
    json.dump(pessoa, arquivo, indent=2)

'''
# json.load
caminho_arquivo = 'C:\\ESTUDOS\\Python\\Curso_python_3_udemy\\MODULO2_python_intermediario\\'
caminho_arquivo += 'arquivo_teste_json.json'
with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)

print(pessoa)