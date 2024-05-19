'''
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno.

Criando um set
set(iterável) ou {1, 2, 3}
'''
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados





'''
Sets são eficientes para remover valores duplicados
de iteráveis.
- Não aceitam valores mutáveis;
- Seus valores serão sempre únicos;
- não tem índexes;
- não garantem ordem;
- são iteráveis (for, in, not in)
'''
# teste = {'e', 'e', 'e','e', 'c','c',1,1,1,2,2,3}
# print(teste)





'''
Métodos úteis:
add, update, clear, discard
'''
# teste = set()
# teste.add('erick')  #add so da pra adicionar um por vez
# teste.add(69)    #add so da pra adicionar um por vez
# teste.update(('Olá, mundo!',1,2,3,4,5,6,7,8,9,10))  #update é usando para adicionar mais de um elemento ao meu set
# teste.discard('erick')  #discard éusado para remover um elemento especifico do meu set
# print(teste)





'''
Operadores úteis:
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
'''
# teste1 = {1,2,3}
# teste2 = {2,3,4}
# teste3 = teste1 | teste2    # | é usado para unir 2 set's
# teste4 = teste1 & teste2    # & é usado para achar os itens q se repetem em ambos os set's
# teste5 = teste1 - teste2    # - é usado para mostrar os itens que so se encontram na esqueda. ex: x - y = vai mostrar so o do x se quiser so o do y tem q colocar : y - x.
# teste6 = teste1 ^ teste2    # ^ é usado para mostrar os itens q so tem nos set's individuais.
# print(teste6)   # resposta = {1,4}





'''
Exemplo de uso dos set's
'''

letras = set()
while True:
    letra = input('Digite uma letra: ').upper()
    letras.add(letra)
    if 'W' in letras:
        print('Achou a letra misteriosa.')
        break
    print(letras)