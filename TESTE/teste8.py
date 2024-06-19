import json

caminho_arquivo = 'D:\\ESTUDOS\\Python\\TESTE\\'
caminho_arquivo += 'teste8.json'

def salvar(dados,caminho):
    with open(caminho, 'a+', encoding='utf8') as arquivo:
        json.dump(dados, arquivo, indent=2)

while True:
    entrada = input('Digite seu nome :  ')

    pessoa = {'nome' : entrada}

    salvar(pessoa, caminho_arquivo)