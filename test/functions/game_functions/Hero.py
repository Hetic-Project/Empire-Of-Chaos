# Une class qui gère le statu du héro et ces coordonnées sur la map
from functions.game_functions.stages.Stage import *


class Hero:

    # Status du héro
    level = 20
    life = 300
    maxlife = 300
    progressHeroPv = 100
    strength = 250
    defense = 230
    exp = 0
    progressEXP = 0
    direction = ""
    inventaire = []
    
    x = 0
    y = 1    

    front = "background: url(test/sprites/hero/Hero_front-left-right.png);" + \
        "background-position: center"

    front_left = "background: url(test/sprites/hero/Hero_front-left-right.png);" + \
        "background-position: left" 

    front_right = "background: url(test/sprites/hero/Hero_front-left-right.png);" + \
        "background-position: right"          

    back = "background: url(test/sprites/hero/Hero_back-back-right-back-left.png);" + \
        "background-position: center"

    back_left = "background: url(test/sprites/hero/Hero_back-back-right-back-left.png);" + \
        "background-position: left" 

    back_right = "background: url(test/sprites/hero/Hero_back-back-right-back-left.png);" + \
        "background-position: right"       

    left = "background: url(test/sprites/hero/Hero_left-left-left.png);" + \
        "background-position: center"

    left_left = "background: url(test/sprites/hero/Hero_left-left-left.png);" + \
        "background-position: left"

    left_right = "background: url(test/sprites/hero/Hero_left-left-left.png);" + \
        "background-position: right"          

    right = "background: url(test/sprites/hero/Hero_right-right-right.png);" + \
        "background-position: center"

    right_left = "background: url(test/sprites/hero/Hero_right-right-right.png);" + \
        "background-position: left"

    right_right = "background: url(test/sprites/hero/Hero_right-right-right.png);" + \
        "background-position: right"          
