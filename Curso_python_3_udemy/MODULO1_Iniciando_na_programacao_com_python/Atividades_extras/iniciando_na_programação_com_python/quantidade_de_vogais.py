'''
Desenvolva uma função que receba uma palavra como entrada e retorne a quantidade de vogais presentes na palavra.
'''

palavra = input('Digite alguma coisa.: ')
vogais = 'aeiou'
contador_de_vogais = 0
for letra in palavra:
    if letra in vogais:
        contador_de_vogais += 1
print(contador_de_vogais)