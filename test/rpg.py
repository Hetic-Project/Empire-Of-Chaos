import sys

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QWidget, QLabel
from functions.interface_functions.centralWindow import *
from functions.game_functions.stages.Stage import *
from functions.game_functions.addMonsterInMap import *
from functions.game_functions.gameScreen import *
from functions.game_functions.pickUpFunction import *
from functions.game_functions.createMonsterPanel import *
from functions.game_functions.Monster import *
from functions.game_functions.addMonstersSprite import *
from functions.interface_functions.gameMainTitleScreen import *
from functions.game_functions.countDown import *


class WelcomeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Information")
        self.setMinimumSize(600, 250)
        welcome_label = QLabel("Bienvenue dans Empire of Chaos, l'objectif principal du jeu est de recueillir \nles 4 clés dispersés dans les 4 biomes que vous devrez explorer ils sont gouvernés \npar des êtres puissants tout cela pour arriver à vos fins, vaincre Ouroubos, \nune créature terrifiante qui a jadis détruit votre rayaume tout entier,\nvous devez donc partir de rien pour arriver à adoucir \ncette haine que vous avez depuis tant d'années.", self)
        welcome_label.move(90, 50)

        close_button = QPushButton("Fermer", self)
        close_button.move(250, 200)
        close_button.clicked.connect(self.close)

    def close_game(self):
        self.close()
        self.close_game_signal.emit()


class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Empire Of Chaos")
        self.setMinimumSize(1275, 1000)
        self.setWindowIcon(QIcon("test/icons/rpg.png"))

        centralArea = centralWindow(self)

        def launchGame():
            # Create an instance of the welcome dialog and show it
            self.welcome_dialog = WelcomeDialog()
            # Connect the close_game_signal to the close method of the main game window
            self.welcome_dialog.show()
            panelMainTitle.deleteLater()
            generateRandomCoordinate()
            centralArea = centralWindow(self)
            gameScreen(centralArea)
           


        panelMainTitle = QWidget(self)
        panelMainTitle.setGeometry(0, 0, 1175, 900)
        panelMainTitle.setStyleSheet("background: url(home.jpg) no-repeat center;")

        StartGame = QPushButton("Start", panelMainTitle)
        StartGame.setGeometry(435, 360, 300, 40)
        StartGame.clicked.connect(launchGame)

        Credits = QPushButton("Credits", panelMainTitle)
        Credits.setGeometry(435, 400, 300, 40)

        

        Exit = QPushButton("Exit", panelMainTitle)
        Exit.setGeometry(435, 440, 300, 40)


         

    # keyPressEvent est une fonction native a Qt elle permet de gérer les évènement
    def keyPressEvent(self, event):
        
        centralArea = centralWindow(self)
        gameScreenWindow = gameScreen(centralArea)
        createHeroPanel(gameScreenWindow)

        # j'appelle borderMap pour qu'elle soit connue de ma fonction keyPressEvent
        mapCell = drawGameMap(gameScreenWindow, Hero.front)[1]

        # aller a droite
        if event.key() == 16777236:  # si l'utilisateur appuie sur la fleche droite
            # cette ligne empèche le personnage de sortir de la map
            if Hero.x <= 12:
                if "Monster-[{}, {}]".format(Hero.y, Hero.x+1) in str(Stage.infoMonsters):
                    for i in Stage.infoMonsters:

                        if i["y"] == Hero.y and i["x"] == Hero.x+1:
                            # Voire les stats du monstre
                            createMonsterPanel(
                                gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                            drawGameMap(gameScreenWindow, Hero.right)
                            return

                elif "'mapPoint': [{}, {}]".format(Hero.y, Hero.x+1) in str(Stage.infoKey):
                    print("Voila la clée")
                    # un boutton rammaser apparais
                    pickUpBTN = QPushButton("Ramasser",  gameScreenWindow)
                    pickUpBTN.setGeometry(40, 550, 125, 50)
                    pickUpBTN.clicked.connect(pickUpFunction)
                    drawGameMap(gameScreenWindow, Hero.right)

                else:
                    # et je la redéssine la map avec les nouvelle coordonnée du héro et la direction du sprite
                    Hero.x = Hero.x + 1 
                    drawGameMap(gameScreenWindow, Hero.right)

        # monter
        elif event.key() == 16777235:
            if Hero.y > 0:
                if "Monster-[{}, {}]".format(Hero.y-1, Hero.x) in str(Stage.infoMonsters):
                    for i in Stage.infoMonsters:
                        if i["y"] == Hero.y-1 and i["x"] == Hero.x:
                            createMonsterPanel(
                                gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                            drawGameMap(gameScreenWindow, Hero.back)
                            return

                elif "'mapPoint': [{}, {}]".format(Hero.y-1, Hero.x) in str(Stage.infoKey):
                    print("Voila la clée")
                    pickUpBTN = QPushButton("Ramasser",  gameScreenWindow)
                    pickUpBTN.setGeometry(40, 550, 125, 50)
                    pickUpBTN.clicked.connect(pickUpFunction)
                    drawGameMap(gameScreenWindow, Hero.back)
                else:
                    Hero.y = Hero.y - 1
                    drawGameMap(gameScreenWindow, Hero.back)

        # descendre
        elif event.key() == 16777237:
            if Hero.y <= 8:
                if "Monster-[{}, {}]".format(Hero.y+1, Hero.x) in str(Stage.infoMonsters):
                    for i in Stage.infoMonsters:
                        if i["y"] == Hero.y+1 and i["x"] == Hero.x:

                            createMonsterPanel(
                                gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                            drawGameMap(gameScreenWindow, Hero.front)
                            return

                elif "'mapPoint': [{}, {}]".format(Hero.y+1, Hero.x) in str(Stage.infoKey):
                    print("Voila la clée")
                    pickUpBTN = QPushButton("Ramasser",  gameScreenWindow)
                    pickUpBTN.setGeometry(40, 550, 125, 50)
                    pickUpBTN.clicked.connect(pickUpFunction)
                    drawGameMap(gameScreenWindow, Hero.front)

                else:
                    Hero.y = Hero.y + 1
                    drawGameMap(gameScreenWindow, Hero.front)

        # aller a gauche
        elif event.key() == 16777234:
            if Hero.x > 0:
                if "Monster-[{}, {}]".format(Hero.y, Hero.x-1) in str(Stage.infoMonsters):
                    for i in Stage.infoMonsters:
                        if i["y"] == Hero.y and i["x"] == Hero.x-1:
                            createMonsterPanel(
                                gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                            drawGameMap(gameScreenWindow, Hero.left)
                            return

                elif "'mapPoint': [{}, {}]".format(Hero.y, Hero.x-1) in str(Stage.infoKey):
                    print("Voila la clée")
                    pickUpBTN = QPushButton("Ramasser",  gameScreenWindow)
                    pickUpBTN.setGeometry(40, 550, 125, 50)
                    pickUpBTN.clicked.connect(pickUpFunction)
                    drawGameMap(gameScreenWindow, Hero.left)

                else:
                    Hero.x = Hero.x - 1
                    drawGameMap(gameScreenWindow, Hero.left)

        # si j'appuie sur entrer j'attaque
        elif event.key() == 16777220:
            for i in Stage.infoMonsters:

                if i["y"] == Hero.y and i["x"] == Hero.x+1:
                    createMonsterPanel(
                        gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)

                    if i["life"] <= 0:
                        print("le monstre est mort")
                        drawGameMap(gameScreenWindow, Hero.right)
                        # gain d'xp
                        # butin
                    else:

                        attack = int(
                            Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        drawGameMap(gameScreenWindow, Hero.right)
                        return

                elif i["y"] == Hero.y-1 and i["x"] == Hero.x:
                    createMonsterPanel(
                        gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                    if i["life"] <= 0:
                        print("le monstre est mort")
                        drawGameMap(gameScreenWindow, Hero.back)
                    else:

                        attack = int(
                            Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        drawGameMap(gameScreenWindow, Hero.back)
                    return

                elif i["y"] == Hero.y+1 and i["x"] == Hero.x:
                    createMonsterPanel(
                        gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)

                    if i["life"] <= 0:
                        print("le monstre est mort")
                        drawGameMap(gameScreenWindow, Hero.front)
                    else:
                        attack = int(
                            Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        drawGameMap(gameScreenWindow, Hero.front)
                    return

                elif i["y"] == Hero.y and i["x"] == Hero.x-1:
                    createMonsterPanel(
                        gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                    if i["life"] <= 0:
                        print("le monstre est mort")
                        drawGameMap(gameScreenWindow, Hero.left)
                    else:
                        attack = int(
                            Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        drawGameMap(gameScreenWindow, Hero.left)
                    return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())
