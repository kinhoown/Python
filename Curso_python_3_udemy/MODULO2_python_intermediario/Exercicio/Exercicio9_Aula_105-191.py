import os

lista_de_tarefas = []
lista_refazer = []

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

while True:
    print('listar, desfazer, refazer')
    entradas = input('Digite uma tarefa ou comando: ').upper()

    if entradas == 'LISTAR':
        limpar()
        listar_as_tarefas(lista_de_tarefas)
    elif entradas == 'DESFAZER':
        limpar()
        desfazer_as_tarefas(lista_de_tarefas, lista_refazer)
        listar_as_tarefas(lista_de_tarefas)
    elif entradas == 'REFAZER':
        limpar()
        refazer_as_taferas(lista_de_tarefas, lista_refazer)
        listar_as_tarefas(lista_de_tarefas)
    else:
        limpar()
        adicionar(entradas)