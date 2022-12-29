
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from drawGameMap import *
from centralWindow import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Empire Of Chaos")
        self.setMinimumSize(800, 600)
        self.setWindowIcon(QIcon("test/icons/rpg.png"))

        centralArea = centralWindow(self)

        drawGameMap(centralArea)

    # keyPressEvent est une fonction native a Qt elle permet de gérer les évènement
    def keyPressEvent(self, event):

        # aller a droite
        if event.key() == 16777236:  # si l'utilisateur appuie sur la fleche droite
            if Hero.x <= 12:  # cette ligne empèche le personnage de sortir de la map
                Hero.x = Hero.x + 1  # j'ajoute 1 sur l'axe des x du hero
                # j'appelle centralArea pour qu'elle soit connu de ma fonction drawGameMap
                centralArea = centralWindow(self)
                # j'appelle borderMap pour qu'elle soit connue de ma fonction keyPressEvent
                borderMap = drawGameMap(centralArea)
                borderMap.close()  # J'éfface la map
                # et je la redéssine la map avec les nouvelle coordonnée du héro
                drawGameMap(centralArea)

        # monter
        if event.key() == 16777235:
            if Hero.y > 0:
                Hero.y = Hero.y - 1
                centralArea = centralWindow(self)
                borderMap = drawGameMap(centralArea)
                borderMap.close()
                drawGameMap(centralArea)

        # decsendre
        if event.key() == 16777237:
            if Hero.y <= 8:
                Hero.y = Hero.y + 1
                centralArea = centralWindow(self)
                borderMap = drawGameMap(centralArea)
                borderMap.close()
                drawGameMap(centralArea)

        # aller a gauche
        if event.key() == 16777234:
            if Hero.x > 0:
                Hero.x = Hero.x - 1
                centralArea = centralWindow(self)
                borderMap = drawGameMap(centralArea)
                borderMap.close()
                drawGameMap(centralArea)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
