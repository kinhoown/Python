import json

caminho_arquivo = 'D:\\ESTUDOS\\Python\\TESTE\\'
caminho_arquivo += 'teste8.json'

pessoa = {
    'nome' : 'erick alexandre pessoa de lima'
}

def salvar(dados,caminho):
    with open(caminho, 'w', encoding='utf8') as arquivo:
        json.dump(dados, arquivo, indent=2)

salvar(pessoa, caminho_arquivo)