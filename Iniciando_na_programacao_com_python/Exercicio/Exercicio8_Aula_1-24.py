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
# palavra = input('Digite uma palavra: ').upper()
# palavra_chave = len(palavra)*'*'

# while True:
#     if palavra_chave == palavra:
#         palavra_chave = len(palavra)*'*'
#         print('Você venceu!')
#         break
#     cont = 0
#     letra = input('Digite uma letra: ').upper()
#     if len(letra)>1:
#         print('Digite apenas uma letra.')
#     else:
#         for i in palavra:
#             if i == letra:
#                 palavra_chave = palavra_chave[:cont]+i+palavra_chave[cont+1:]
#                 cont+=1
#                 print(f'Palavra formatada: {palavra_chave}')
#                 break
#             elif i == palavra[-1]:
#                 print(f'Palavra formatada: {palavra_chave}')
#             elif i != letra:
#                 cont+=1


palavra = 'eriick'.upper()
letra_acertadas = ''
while True:
    letra = input('Digite uma letra: ').upper()
    if len(letra) > 1:
        print('É para digitar apenas uma letra!')
        continue
    if letra in palavra:
        letra_acertadas += letra
    for letra in palavra:
        if letra in letra_acertadas:
            print(letra)
        else:
            print('*')