import signal
import sys
import time
import random
from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QWidget, QLabel
from functions.interface_functions.centralWindow import *
from functions.game_functions.stages.Stage import *
from functions.game_functions.addMonsterInMap import *
from functions.game_functions.gameScreen import *
from functions.game_functions.pickUpFunction import *
from functions.game_functions.createMonsterPanel import *
from functions.game_functions.Monster import *
from functions.game_functions.addSprite import *
from functions.interface_functions.gameMainTitleScreen import *
from functions.game_functions.addAttackIndication import *
from functions.game_functions.closeFunction import *
from functions.game_functions.stages.nextStage import *
from functions.game_functions.stages.nextStage import *




class WelcomeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Info")
        self.setMinimumSize(600, 250)
        self.setWindowIcon(QIcon("test/icons/rpg.png"))
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

        close_game_signal = Signal()

        centralArea = centralWindow(self)

        def launchGame():
            self.welcome_dialog = WelcomeDialog()
            self.welcome_dialog.show()
            panelMainTitle.deleteLater()
            generateRandomCoordinate()
            centralArea = centralWindow(self)
            gameScreen(centralArea , Stage.countMonster , len(Stage.randomMonsterInMap) , Stage.countKey , len(Stage.keyMapArray), "Hello player")

<<<<<<< HEAD
=======
           
>>>>>>> c20f23aa1d48002c875e6ebd482bb2566b11b815

        def show_credits():
            credits_window = QDialog()
            credits_window.setWindowTitle("Credits")
            credits_window.setMinimumSize(400, 250) 
            credits_window.setWindowIcon(QIcon("test/icons/rpg.png"))
            credits_label = QLabel("Développeurs : \n\n\nWilliam Vandal\nLucas Yalman\nMohamed Yaich\nKen's", credits_window)
            credits_label.move(250, 50)
            credits_label.setStyleSheet("color : white;" "background : black;")
            credits_window.show()
            close_game_signal.connect(show_credits)


        font = QFont(" ")

        panelMainTitle = QWidget(self)
        panelMainTitle.setGeometry(0, 0, 1175, 900)
        panelMainTitle.setStyleSheet("background: url(home.jpg) no-repeat center;")

        StartGame = QPushButton("Start", panelMainTitle)
        StartGame.setGeometry(435, 360, 300, 40)
        StartGame.clicked.connect(launchGame)
        StartGame.setStyleSheet(f"""
                QPushButton {{
                            background : black;
                            color : white;
                }}
                QPushButton:pressed {{
                                    background : white; 
                                    color: #f31d58; 
                                    font-weight: bold; 
                                    font-size : 18px; 
                                    border: none;}}
                                    """)

        credits = QPushButton("Credits", panelMainTitle)
        credits.setGeometry(435, 400, 300, 40)
        credits.clicked.connect(show_credits) 
        credits.setFont(font)
        credits.setStyleSheet("color : white;" "background : black;")
        credits.setStyleSheet(f"""
                QPushButton {{
                            background : black;
                            color : white;
                }}
                QPushButton:pressed {{
                                    background : white; 
                                    color: #f31d58; 
                                    font-weight: bold; 
                                    font-size : 18px; 
                                    border: none;}}
                                    """)
        

        Exit = QPushButton("Exit", panelMainTitle)
        Exit.setGeometry(435, 440, 300, 40)
        #Exit.setStyleSheet("background : black;"  "color : white;")
        Exit.setStyleSheet(f"""
                QPushButton {{
                            background : black;
                            color : white;
                }}
                QPushButton:pressed {{
                                    background : white; 
                                    color: #f31d58; 
                                    font-weight: bold; 
                                    font-size : 18px; 
                                    border: none;}}
                                    """)
        Exit.clicked.connect(self.exitGame)

    def exitGame(self):
        choice = QMessageBox.question(self, "Exit", "Êtes-vous sûrs de vouloir quitter ?",
                                      QMessageBox.   Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    # keyPressEvent est une fonction native a Qt elle permet de gérer les évènement
    def keyPressEvent(self, event):
       
        centralArea = centralWindow(self)
        gameScreenWindow = gameScreen(centralArea , Stage.countMonster , len(Stage.randomMonsterInMap) , Stage.countKey , len(Stage.keyMapArray) , "Hello player")
        createHeroPanel(gameScreenWindow)

        # j'appelle borderMap pour qu'elle soit connue de ma fonction keyPressEvent
        mapCell = drawGameMap(gameScreenWindow, Hero.front)[1]

        # aller a droite
        if event.key() == 16777236:  # si l'utilisateur appuie sur la fleche droite
            # cette ligne empèche le personnage de sortir de la map
            if Hero.x <= 12:
                if "'Monster-[{}, {}]".format(Hero.y, Hero.x+1) in str(Stage.infoMonsters):
                    for i in Stage.infoMonsters:
                        if i["y"] == Hero.y and i["x"] == Hero.x+1:
                            # Voire les stats du monstre
                            if i["life"] > 0 :
                                createMonsterPanel(
                                    gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                                addAttackIndication(gameScreenWindow, "green")
                                drawGameMap(gameScreenWindow, Hero.right)
                                return
                            else:
                                Hero.x = Hero.x + 1 
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
                            if i["life"] > 0 :
                                createMonsterPanel(
                                    gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                                addAttackIndication(gameScreenWindow, "green")    
                                drawGameMap(gameScreenWindow, Hero.back)
                            else:
                                Hero.y = Hero.y -1
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
                                if i["life"] > 0 :
                                    createMonsterPanel(
                                        gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                                    addAttackIndication(gameScreenWindow, "green")    
                                    drawGameMap(gameScreenWindow, Hero.front)

                                else:
                                    Hero.y = Hero.y + 1 
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
                            if i["life"] > 0 :
                                createMonsterPanel(
                                    gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                                addAttackIndication(gameScreenWindow, "green")    
                                drawGameMap(gameScreenWindow, Hero.left)
                            else:
                                Hero.x = Hero.x - 1 
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
#Droite ========================================================================================================================================
        # si j'appuie sur entrer j'attaque
        elif event.key() == 16777220 :
            for i in Stage.infoMonsters:

                if i["y"] == Hero.y and i["x"] == Hero.x+1:
                    createMonsterPanel(
                        gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                    addAttackIndication(gameScreenWindow, "green")

                    if i["life"] <= 0:
                        print("le monstre est mort")
                        addAttackIndication(gameScreenWindow, "white")
                        drawGameMap(gameScreenWindow, Hero.right)
                        return

                    else:
   
                        attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        hit = QWidget(mapCell[i["y"]][i["x"]])
                        hit.setGeometry(0,0,50,50)
                        hit.setStyleSheet("border: 1px solid black ")


                        addTextBox(gameScreenWindow,"vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))

                        drawGameMap(gameScreenWindow, Hero.right)

                        time.sleep(2)

                        attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                        Hero.life = Hero.life - attackBack

                        addTextBox(gameScreenWindow,"Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))

                        if i["life"] <= 0:
                            i["statut"] = "dead"
                            print(i)
                            addTextBox(gameScreenWindow,"bravos le monstre a été vaincu, vous avez gagner XX d'exp")
                            RAND = random.randint(0,len(Items.dropItems)-1)
                            Stage.countMonster = Stage.countMonster + 1
                           
                            if RAND == 0:
                                addTextBox(gameScreenWindow,"aucun objet reçus !")
                            else:
                                addTextBox(gameScreenWindow,"{},reçus et ranger dans l'inventaire".format(Items.dropItems[RAND]))
                                if Items.dropItems[RAND] in Items.dropInfo :
                                    Items.SaveDropItems.append(Items.dropInfo["{}".format(Items.dropItems[RAND])]["image"])

                                    
                                
                                


                        drawGameMap(gameScreenWindow, Hero.right)               
                    return
#==========================================================================================================================================
#Monter===========================================================================================================================================
                elif i["y"] == Hero.y-1 and i["x"] == Hero.x:
                    createMonsterPanel(
                        gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                    if i["life"] <= 0:
                        addTextBox(gameScreenWindow,"le monstre est mort")
                        drawGameMap(gameScreenWindow, Hero.back)
                    else:

                        attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack

                        addTextBox(gameScreenWindow,"vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))

                        if i["life"] <= 0:
                            print("bravos le monstre a été vaincu, vous avez gagner XX d'exp")

                            RAND = random.randint(0,len(Items.dropItems)-1)
                            Stage.countMonster = Stage.countMonster + 1
                           
                            if RAND == 0:
                                addTextBox(gameScreenWindow,"aucun objet reçus !")
                            else:
                                addTextBox(gameScreenWindow,"{},reçus et ranger dans l'inventaire".format(Items.dropItems[RAND]))    

                        drawGameMap(gameScreenWindow, Hero.back)

                        time.sleep(2)

                        attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                        Hero.life = Hero.life - attackBack

                        addTextBox(gameScreenWindow,"Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))

                        if i["life"] <= 0:
                            addTextBox(gameScreenWindow,"bravos le monstre a été vaincu, vous avez gagner XX d'exp")

                            RAND = random.randint(0,len(Items.dropItems)-1)
                           
                            if RAND == 0:
                                addTextBox(gameScreenWindow,"aucun objet reçus !")
                            else:
                                addTextBox(gameScreenWindow,"{}reçus et ranger dans l'inventaire".format(Items.dropItems[RAND]))  

                        drawGameMap(gameScreenWindow, Hero.back)               
                    return
#Bas=============================================================================================================================================
                elif i["y"] == Hero.y+1 and i["x"] == Hero.x:
                    createMonsterPanel(
                        gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)

                    if i["life"] <= 0:
                        addTextBox(gameScreenWindow,"le monstre est mort")
                        drawGameMap(gameScreenWindow, Hero.front)
                    else:
                        attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack

                        addTextBox(gameScreenWindow,"vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))

                        drawGameMap(gameScreenWindow, Hero.front)

                        time.sleep(2)

                        attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                        Hero.life = Hero.life - attackBack

                        addTextBox(gameScreenWindow,"Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))

                        if i["life"] <= 0:
                            addTextBox(gameScreenWindow,"bravos le monstre a été vaincu, vous avez gagner XX d'exp")

                            RAND = random.randint(0,len(Items.dropItems)-1)
                            Stage.countMonster = Stage.countMonster + 1
                           
                            if RAND == 0:
                                addTextBox(gameScreenWindow,"aucun objet reçus !")
                            else:
                                addTextBox(gameScreenWindow,"{}reçus et ranger dans l'inventaire".format(Items.dropItems[RAND]))  

                        drawGameMap(gameScreenWindow, Hero.front)               
                    return
#Gauche============================================================================================================================================
                elif i["y"] == Hero.y and i["x"] == Hero.x-1:
                    createMonsterPanel(
                        gameScreenWindow, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                    if i["life"] <= 0:
                        addTextBox(gameScreenWindow,"le monstre est mort")
                        drawGameMap(gameScreenWindow, Hero.left)
                    else:

                        attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack

                        addTextBox(gameScreenWindow,"vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))

                        drawGameMap(gameScreenWindow, Hero.left)

                        time.sleep(2)

                        attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                        Hero.life = Hero.life - attackBack

                        addTextBox(gameScreenWindow,"Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))

                        if i["life"] <= 0:
                            addTextBox(gameScreenWindow,"bravos le monstre a été vaincu, vous avez gagner XX d'exp")
                            RAND = random.randint(0,len(Items.dropItems)-1)
                            Stage.countMonster = Stage.countMonster + 1
                            
                            if RAND == 0:
                                addTextBox(gameScreenWindow,"aucun objet reçus !")
                            else:
                                addTextBox(gameScreenWindow,"{}reçus et ranger dans l'inventaire".format(Items.dropItems[RAND]))   


                        drawGameMap(gameScreenWindow, Hero.left)               
                    return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())
