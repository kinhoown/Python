def validar_entrada(entra):
    comandos = ['listar', 'desfazer', 'refazer']
    for comando in comandos:
        if comando == entra:
            

while True:
    print('Comandos: listar, desfazer, refazer')
    validar_entrada(entrada = input('Digite uma tarefa ou comando:'))
