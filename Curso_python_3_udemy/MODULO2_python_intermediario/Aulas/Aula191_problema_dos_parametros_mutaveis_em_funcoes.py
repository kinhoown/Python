def xd(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

x = xd('erick')
xd('joaquim',x)
xd('mario',x)
print(x)