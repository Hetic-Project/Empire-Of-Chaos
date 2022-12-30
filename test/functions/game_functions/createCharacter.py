
from PySide6.QtWidgets import QWidget
from game_functions.drawGameMap import drawGameMap
from interface_functions.centralWindow import centralWindow


def createCharacter(self, direction, positionX, PositionY):
    # a l'aide de mapCell je place héro sur la map
    centralArea = centralWindow(self)
    mapCell = drawGameMap(centralArea)[1]

    character = QWidget(mapCell[PositionY][positionX])
    character.setGeometry(0, 0, 125, 124)
    character.setStyleSheet(
        " {} ".format(direction))
    return character
