import os
import json


#CASA = 'D:\\ESTUDOS\\Python\\Curso_python_3_udemy\\MODULO2_python_intermediario\\Exercicio\\'
#TRABALHO = 'C:\\ESTUDOS\\Python\\Curso_python_3_udemy\\MODULO2_python_intermediario\\Exercicio\\'

caminho_arquivo = 'D:\\ESTUDOS\\Python\\Curso_python_3_udemy\\MODULO2_python_intermediario\\Exercicio\\'

caminho_arquivo += 'Exercicio10_Aula_105-194.json'

def limpar():
    os.system('cls')

def pular_linha():
    print('')

def listar_as_tarefas(lista):
    print('LISTA DE TAREFAS:\n')
    for i in lista:
        print(f'\t- {i}')
    pular_linha()

def adicionar(entra):
    lista_de_tarefas.append(entra)

def desfazer_as_tarefas(lista_tarefa,lista_refazer):
    pular_linha()
    if not lista_tarefa:
        print('Não tem mais tarefas para desfazer.')
        return
    pular_linha()
    lista_refazer.append(lista_tarefa[-1])
    lista_tarefa.pop()

def refazer_as_taferas(lista_tarefa, lista_refazer):
    pular_linha()
    if not lista_refazer:
        print('Não tem mais tarefas para retornar.')
        return
    pular_linha()
    lista_tarefa.append(lista_refazer[-1])
    lista_refazer.pop()

def ler(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
        dados = json.load(arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'a+', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2)
    return dados

lista_de_tarefas = []
lista_refazer = []

while True:
    print('listar, desfazer, refazer')
    entradas = input('Digite uma tarefa ou comando: ').upper()

    if entradas == 'LISTAR':
        limpar()
        listar_as_tarefas(lista_de_tarefas)
        ler(lista_de_tarefas, caminho_arquivo)
    elif entradas == 'DESFAZER':
        limpar()
        desfazer_as_tarefas(lista_de_tarefas, lista_refazer)
        listar_as_tarefas(lista_de_tarefas)
        salvar(lista_de_tarefas, caminho_arquivo)
    elif entradas == 'REFAZER':
        limpar()
        refazer_as_taferas(lista_de_tarefas, lista_refazer)
        listar_as_tarefas(lista_de_tarefas)
        salvar(lista_de_tarefas, caminho_arquivo)
    else:
        limpar()
        adicionar(entradas)
        salvar(lista_de_tarefas, caminho_arquivo)