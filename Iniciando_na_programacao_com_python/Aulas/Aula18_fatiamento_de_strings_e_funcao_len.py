"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [start : stop : stap] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

nome = input('Digite seu nome: ')

print(f'seu nome tem {len(nome)} letras.')

print(nome[0:len(nome):2])
#tambem pode ser
print(nome[::2])
#quando deixamos o star e o stop sem parametro estamos flando a ele q é pra iniciar pelo primeiro e terminar no ultimo.