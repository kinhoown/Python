import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(10)]
generator = (n for n in range(10)) #eu crio ele com () no lugar de [] e assim eu pego um numero apos o outro.

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
print(lista)
print(generator)

for n in lista:
    print(n)
print()
for n in generator:
    print(n)