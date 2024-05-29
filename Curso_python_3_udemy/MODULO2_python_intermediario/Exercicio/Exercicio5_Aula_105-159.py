import copy
# Exercícios
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# 1 - Aumente os preços dos produtos a seguir em 10%
'''
for produto in produtos:
    produto['preco'] = ((10 / 100) * produto['preco']) + produto['preco']
    print(produto)
'''
# 2 - Gere novos_produtos por deep copy (cópia profunda)
'''
produtos_2 = copy.deepcopy(produtos)
print(produtos_2)
'''
# 3 - Ordene os produtos por nome decrescente (do maior para menor)
'''
produtos.sort(key=lambda item: item['nome'], reverse=True)
for produto in produtos:
    print(produto)
'''
# 4 - Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
'''
produtos_2 = copy.deepcopy(produtos)
produtos_2.sort(key=lambda item: item['nome'])
for produto in produtos_2:
    print(produto)
'''
# 5 - Ordene os produtos por preco crescente (do menor para maior)
'''
produtos.sort(key=lambda item: item['preco'])
for produto in produtos:
    print(produto)
'''
# 6 - Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
'''
produtos_2 = copy.deepcopy(produtos)
produtos_2.sort(key=lambda item: item['preco'])
for produto in produtos_2:
    print(produto)
'''