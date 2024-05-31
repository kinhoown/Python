from npcs import *
from player import *

quantidade_npcs(5)  #quantos npcs vai ser sumonado
for npc in lista_npcs:
    print(f"{npc['nome']} \\\\ Level: {npc['lvl']} \\\\ HP: {npc['hp']} \\\\ DANO: {npc['dano']}")


for i , v in avatar.items():
    print(f'{i} : {v}')