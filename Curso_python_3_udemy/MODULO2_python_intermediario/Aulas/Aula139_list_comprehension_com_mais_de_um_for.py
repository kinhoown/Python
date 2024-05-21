#lista comum

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
print(lista)

#lista comprehension

lista2 = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
print(lista2)

# com duvidas so visitar   https://www.youtube.com/watch?v=1YbTDczvqco  