from random import randint, choice

lista_npcs = []


def criar_npc():
    level = randint(1,5)
    nome_monstro = choice(['Babidi', 'Dabura', 'Majin Boo', 'Frisar'])
    novo_npc = {'nome': nome_monstro, 'lvl': level , 'hp': 100 * level}
    lista_npcs.append(novo_npc)


def quantidade_npcs(quant):
    for i in range(quant):
        criar_npc()

quantidade_npcs(5)


for npc in lista_npcs:
    print(f"{npc['nome']} \\\\ Level: {npc['lvl']} \\\\ HP: {npc['hp']}")