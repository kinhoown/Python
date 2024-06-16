import json

caminho_arquivo = 'D:\\ESTUDOS\\Python\\TESTE\\'
caminho_arquivo += 'teste6.json'

pessoa = {
    'nome' : 'Erick',
    'sobrenome' : 'Lima',
    'idade' : 26,
    'sexo' : 'M',
}

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, indent=2)