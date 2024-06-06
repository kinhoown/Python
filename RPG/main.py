from npcs import *
from player import *

quantidade_npcs(5)  #quantos npcs vai ser sumonado
for indice ,npc in enumerate(lista_npcs):
    print(f"Monstro {indice} - {npc['nome']} \\\\ Level: {npc['lvl']} \\\\ HP: {npc['hp']} \\\\ DANO: {npc['dano']}")


'''for i , v in avatar.items():
    print(f'{i} : {v}')'''  #mostrar avatar

escolher_monstro_ataque = int(input('Qual o mostro vc deseja atacar? '))