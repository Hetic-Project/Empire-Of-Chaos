
import sys
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Empire Of Chaos")
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        self.setWindowIcon(QIcon("test/icons/rpg.png"))

        centralArea = QWidget()
        centralArea.setGeometry(0, 0, 800, 600)
        self.setCentralWidget(centralArea)
        centralArea.setStyleSheet("background: #419eee")

        # Une class qui gère le statu du héro et les intéraction
        class Hero:

            # Status du héro
            pv = 100
            mp = 100
            force = 50
            defense = 50

            # Coordonné du héro sur la map
            x = 51
            y = 51

            def move_right(map):
                print("Move right")
                # map.setCellWidget(Hero.y, Hero.x+1, Hero.hero)

            def move_left(map):
                map.setCellWidget(Hero.y, Hero.x-1, Hero.hero)

            def move_top(map):
                map.setCellWidget(Hero.y+1, Hero.x, Hero.hero)

            def move_down(map):
                map.setCellWidget(Hero.y-1, Hero.x, Hero.hero)

            def attack():
                pass

            def talk():
                pass

        def currentYPosition(widget):
            xPosition = 0
            global x
            global X
            x = 0
            while x < 13:
                X = QWidget(widget)
                X.setGeometry(xPosition, 0, 125, 125)
                X.setStyleSheet("border: 1px solid black;")
                xPosition = xPosition + 51
                x = x + 1

        def map():

            borderMap = QWidget(centralArea)
            borderMap.setGeometry(0, 0, 800, 576)
            borderMap.setStyleSheet(
                "border: 1px solid black;" "margin: auto;")

            yPosition = 0
            y = 0
            row = []

            while y < 10:

                Y = QWidget(borderMap)
                Y.setGeometry(0, yPosition, 800, 125)
                Y.setStyleSheet("border: 1px solid black;")
                yPosition = yPosition + 51
                y = y + 1

                row.append(Y)
                for i in row:
                    currentYPosition(i)

                hero = QWidget(borderMap)
                hero.setGeometry(Hero.x, Hero.y, 125, 124)
                hero.setStyleSheet(
                    "background: url(test/sprites/sprite/Hero.png)")
        map()

    # def keyPressEvent(gameMap, event):
    #     pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
