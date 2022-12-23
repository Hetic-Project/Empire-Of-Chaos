import sys
from PySide6.QtGui import QIcon, QKeyEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Empire Of Chaos")
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        self.setWindowIcon(QIcon("test/icons/rpg.png"))

        centralArea = QWidget()
        self.setCentralWidget(centralArea)
        centralArea.setStyleSheet("background: #419eee")

        # Une class qui gère le statu du héro et les intéraction
        class Hero:

            # intégration du sprite du héro
            hero = QWidget()
            hero.setFixedSize(50, 48)
            hero.setStyleSheet("background: url(test/sprites/sprite/Hero.png)")

            # Status du héro
            pv = 100
            mp = 100
            force = 50
            defense = 50

            # Coordonné du héro sur la map
            x = 1
            y = 1

            def move_right(map):
                map.setCellWidget(Hero.y, Hero.x+1, Hero.hero)

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

        # Fonction map qui gère la création d'une map

        def map():

            # créer un tableau
            map = QTableWidget(11, 13, centralArea)
            map.setFixedSize(800, 600)
            i = 0
            while i < 13:
                map.setColumnWidth(i, 50)
                map.setRowHeight(i, 48)
                i = i+1

            map.setCellWidget(Hero.y, Hero.x, Hero.hero)
            return map

        map()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
