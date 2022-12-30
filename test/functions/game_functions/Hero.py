# Une class qui gère le statu du héro et ces coordonnées sur la map
class Hero:

    # Status du héro
    pv = 100
    mp = 100
    force = 50
    defense = 50

    # Coordonné du héro sur la map
    x = 0
    y = 0

    front = "background: url(test/sprites/sprite/hero_front-left.png);" + \
        "background-position: top"

    back = "background: url(test/sprites/sprite/hero_right-back.png);" + \
        "background-position: bottom"

    left = "background: url(test/sprites/sprite/hero_front-left.png);" + \
        "background-position: bottom"

    right = "background: url(test/sprites/sprite/hero_right-back.png);" + \
        "background-position: top"
