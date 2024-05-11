'''
range funciona com (star, stop, step).
ex: renge(20) --> ta dizendo q o start é 0, o stop é 20 e o step é 1.
renge(3,30) --> ta dizendo q o start é 3, o stop é 30 e o step é 1.
renge(4,40,4) --> ta dizendo q o start é 4, o stop é 40 e o step é 4.
'''

numeros = range(10, 1000, 10)

for numero in numeros:
    print(numero, numeros)

    