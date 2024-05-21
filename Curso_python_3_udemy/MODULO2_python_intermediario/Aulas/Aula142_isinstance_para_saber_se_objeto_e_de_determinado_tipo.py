lista = ['erick', 2, 1.2, [1,2,3], (1,2,3), {1,2,3}, True]

for item in lista:
    if isinstance(item, (int, list)):   ###<------------
        print('É ESSE AQUI!!!')
    else:
        print(item)