
import random
from functions.interface_functions.centralWindow import *
from functions.game_functions.stages.Stage import *
from functions.game_functions.addSprite import *
from functions.game_functions.Hero import *



def addMonsterInMap(mapCell, world, stage):
    # ajouter des monstres de manière aléatoire sur la map

    for m in Stage.world[world]["stages"][stage]["monsters"]["coordinate"] :

        Stage.world[world]["stages"][stage]["monsters"]["info"].append({
            "y": m[0],
            "x": m[1],
            "name": Stage.world[world]["stages"][stage]["monsters"]["name"],
            "life": Stage.world[world]["stages"][stage]["monsters"]["life"],
            "strength": Stage.world[world]["stages"][stage]["monsters"]["strength"],
            "defense": Stage.world[world]["stages"][stage]["monsters"]["defense"],
            "level": Stage.world[world]["stages"][stage]["monsters"]["level"],   
        })   
        
        if m[0] == Hero.y and m[1] == Hero.x+1:
            addSprite(mapCell, m[0], m[1], Stage.world[world]["stages"][stage]["monsters"]["left"])

        elif m[0] == Hero.y and m[1] == Hero.x-1:
            addSprite(mapCell, m[0], m[1], Stage.world[world]["stages"][stage]["monsters"]["right"])

        elif m[0] == Hero.y+1 and m[1] == Hero.x:
            addSprite(mapCell, m[0], m[1], Stage.world[world]["stages"][stage]["monsters"]["back"])

        elif m[0] == Hero.y-1 and m[1] == Hero.x:
            addSprite(mapCell, m[0], m[1], Stage.world[world]["stages"][stage]["monsters"]["front"])
        else:
            addSprite(mapCell, m[0], m[1], Stage.world[world]["stages"][stage]["monsters"]["front"]) 
           

    for i in Stage.world[world]["stages"][stage]["monsters"]["info"]:

        if i["life"] <= 0:
            addSprite(mapCell, i["y"], i["x"], "")             
    

    for k in Stage.world[world]["stages"][stage]["chest"]["coordinate"]:
        addSprite(mapCell, k[0], k[1], Stage.world[world]["stages"][stage]["chest"]["image"])

    for t in Stage.world[world]["stages"][stage]["target"]["coordinate"]:
        addSprite(mapCell, t[0], t[1], Stage.world[world]["stages"][stage]["target"]["image"])
    
