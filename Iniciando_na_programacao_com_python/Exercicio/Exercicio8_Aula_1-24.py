"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra = 'eriick'.upper()
letra_acertadas = ''
cont = 0
while True:
    letra = input('Digite uma letra: ').upper()
    cont += 1

    if len(letra) > 1:
        print('É para digitar apenas uma letra!')
        continue

    if letra in palavra:
        letra_acertadas += letra

    palavra_formada = ''
    for letra in palavra:
        if letra in letra_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print(f'Palavra formada é {palavra_formada}')

    if palavra_formada == palavra:
        os.system('cls')
        print('VOCÊ GANHOUUU!!!!')
        print(f'VOCÊ TENTO {cont} VEZES.')
        letra_acertadas = ''
        cont = 0