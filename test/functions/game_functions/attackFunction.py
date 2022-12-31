from functions.game_functions.stages.Stage import *
from functions.game_functions.Hero import *


def attackFunction():

    for i in Stage.infoMonsters:
        if i["y"] == Hero.y and i["x"] == Hero.x+1 or i["y"] == Hero.y and i["x"] == Hero.x-1 or i["y"] == Hero.y+1 and i["x"] == Hero.x or i["y"] == Hero.y-1 and i["x"] == Hero.x:
            print(i)
            return
