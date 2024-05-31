l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(l1,l2))) #aqui ele junta atravez da menor lista.





from itertools import zip_longest

print(list(zip_longest(l1,l2))) #aqui ele junta atravez da maior lista e pra isso tem q usar o import