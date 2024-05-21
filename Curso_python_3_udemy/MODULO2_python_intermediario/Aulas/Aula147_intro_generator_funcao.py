'''
def generator(n=0):
    yield 1
    print('continuando...')
    yield 2
    print('mais uma ...')
    yield 3
    print('vou terminar')
    return 'ACABOU 👌'

gen = generator()

for n in gen:
    print(n)
'''

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum: 
            return

gen = generator()
for n in gen:
    print(n)