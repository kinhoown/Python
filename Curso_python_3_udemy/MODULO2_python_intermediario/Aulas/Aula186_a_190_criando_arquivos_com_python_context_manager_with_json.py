import os
# Criando arquivos com Python + Context Manager with


caminho_arquivo = 'd:\\ESTUDOS\\Python\\TESTE\\'

caminho_arquivo += 'teste4.txt'


# Usamos a função open para abrir
'''
arquivo = open(caminho_arquivo, 'w')    #dessa forma o arquivo fica aberto e pode ser um problema
'''

'''
with open(caminho_arquivo, 'w') as arquivo: #dessa forma o arquivo abre e fecha .
    print('Arquivo foi aberto.')
    print('arquivo foi fechado.')
'''
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
with open(caminho_arquivo, 'a+', encoding='utf8') as arquivo:    #a diferencia entre o 'w' e o 'a' é q o W apaga tudo e escreve o q vc executou e o A acrecenta o q vc executou.
    arquivo.write('linha 1\n')  #escreve
    arquivo.write('linha 2\n')  #escreve
    arquivo.writelines(
        ('linha 3\n', 'linha 4\n', 'ação\n')
    )   #para digitar varias linhas

    arquivo.seek(0,0)   #mover o cursor para o inicio
    print(arquivo.read())   #leitura

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())   #leitura
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
################################################

# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
'''os.remove(caminho_arquivo)'''
# os.rename - troca o nome ou move o arquivo
'''os.rename(caminho_arquivo, 'd:\\ESTUDOS\\Python\\TESTE\\teste4.txt')'''
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json

# json.load