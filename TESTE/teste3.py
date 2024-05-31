def teste_fora(funcao_externa):
    def teste_dentro():
        print(1)
        funcao_externa()
        print(3)
    return teste_dentro

@teste_fora
def externo():
    print(2)

externo()