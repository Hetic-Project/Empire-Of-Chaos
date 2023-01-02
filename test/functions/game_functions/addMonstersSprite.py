def addMonstersSprite(mapCell, y, x, monsterDirection):
    monster = mapCell[y][x]
    monster.setStyleSheet(
        "{}".format(monsterDirection))
