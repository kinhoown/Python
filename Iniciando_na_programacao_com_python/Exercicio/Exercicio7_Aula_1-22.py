texto = 'aaaa                      aaaae'

contador = 0
letra_mais_repetida_total = 0
letra_mais_repetida = ' '

while contador < len(texto):   # .count('')
    quantidade_de_letras_repetidas = texto.count(texto[contador])

    if texto[contador] == ' ':
        contador +=1
        continue

    if letra_mais_repetida_total < quantidade_de_letras_repetidas:
        letra_mais_repetida_total = quantidade_de_letras_repetidas
        letra_mais_repetida = texto[contador]
        
    contador +=1

print(f'A letra que mais se repete é "{letra_mais_repetida.upper()}" com o total de {letra_mais_repetida_total} letras.')