import signal
import sys
import time
import random
from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon, QFont, QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QWidget, QLabel
from functions.interface_functions.centralWindow import *
from functions.game_functions.stages.Stage import *
from functions.game_functions.addMonsterInMap import *
from functions.game_functions.gameScreen import *
from functions.game_functions.pickUpFunction import *
from functions.game_functions.createMonsterPanel import *
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
        self.setStyleSheet("background-color: #000000;")
        welcome_label = QLabel("Bienvenue dans Empire of Chaos, l'objectif principal du jeu est de recueillir \nles 4 clés dispersés dans les 4 biomes que vous devrez explorer ils sont gouvernés \npar des êtres puissants tout cela pour arriver à vos fins, vaincre Ouroubos, \nune créature terrifiante qui a jadis détruit votre rayaume tout entier,\nvous devez donc partir de rien pour arriver à adoucir \ncette haine que vous avez depuis tant d'années.", self)
        welcome_label.move(90, 50)
        id = QFontDatabase.addApplicationFont("test/YeonSung-Regular.ttf")
        welcome_label.setFont(QFont("Yeon Sung"))
        welcome_label.setStyleSheet("color: white;")
        close_button = QPushButton("Fermer", self)
        close_button.move(250, 200)
        id = QFontDatabase.addApplicationFont("test/YeonSung-Regular.ttf")
        close_button.setFont(QFont("Yeon Sung"))
        close_button.setStyleSheet(f"""
                QPushButton {{
                            color: white;
                            font-size: 18px;
                            background: none;
                            border: none;}}
                }}
            """)
        close_button.clicked.connect(self.close)

    def close_game(self):
        self.close()
        self.close_game_signal.emit()


class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_menu = self

        self.setWindowTitle("Empire Of Chaos")
        self.setMinimumSize(1275, 1000)
        self.setWindowIcon(QIcon("test/icons/rpg.png"))

        close_game_signal = Signal()

        centralArea = centralWindow(self)

        def launchGame():
            self.welcome_dialog = WelcomeDialog()
            self.welcome_dialog.show()
            panelMainTitle.deleteLater()
            generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
            centralArea = centralWindow(self)
            gameWindow = gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea, "Hello player")
            createHeroPanel(gameWindow, Hero.life)
            addPanelGoals(
                gameWindow, 
                Stage.countMonster, 
                Stage.currentWorld, 
                "stage {}".format(Stage.currentStage), 
                Stage.countKey
            )



        def show_credits():
            credits_window = QDialog()
            credits_window.setWindowTitle("Credits")
            credits_window.setMinimumSize(400, 250) 
            credits_window.setWindowIcon(QIcon("test/icons/rpg.png"))
            credits_label = QLabel("Développeurs : \n\n\nWilliam Vandal\nLucas Yalman\nMohamed Yaich\nKen's", credits_window)
            credits_label.move(250, 50)
            id = QFontDatabase.addApplicationFont("test/YeonSung-Regular.ttf")
            credits_label.setFont(QFont("Yeon Sung", 10))
            credits_window.setStyleSheet("color : white;" "background : black;")
            credits_window.show()
            close_game_signal.connect(show_credits)


        panelMainTitle = QWidget(self)
        panelMainTitle.setGeometry(0, 0, 1275, 900)
        panelMainTitle.setStyleSheet("background: url(home.jpg) no-repeat center;")

        StartGame = QPushButton("Start", panelMainTitle)
        StartGame.setGeometry(500, 340, 300, 40)
        StartGame.clicked.connect(launchGame)
        id = QFontDatabase.addApplicationFont("test/YeonSung-Regular.ttf")
        StartGame.setFont(QFont("Yeon Sung", 25))
        StartGame.setStyleSheet(f"""
                QPushButton {{
                            background : none;
                            border: none;}}
                }}
                QPushButton:pressed {{
                                    background : white; 
                                    color: #000000; 
                                    font-weight: bold; 
                                    font-size : 18px; 
                                    border: none;
                                    border-radius: 10px;}}
                                    """)

        credits = QPushButton("Credits", panelMainTitle)
        credits.setGeometry(500, 400, 300, 40)
        credits.clicked.connect(show_credits) 
        id = QFontDatabase.addApplicationFont("test/YeonSung-Regular.ttf")
        credits.setFont(QFont("Yeon Sung", 25))
        credits.setStyleSheet("color : white;" "background : black;")
        credits.setStyleSheet(f"""
                QPushButton {{
                            background : none;
                            border: none;}}
                }}
                QPushButton:pressed {{
                                    background : white; 
                                    color: #000000; 
                                    font-weight: bold; 
                                    font-size : 18px; 
                                    border: none;
                                    border-radius: 10px;}}
                                    """)
        

        Exit = QPushButton("Exit", panelMainTitle)
        Exit.setGeometry(500, 460, 300, 40)
        id = QFontDatabase.addApplicationFont("test/YeonSung-Regular.ttf")
        Exit.setFont(QFont("Yeon Sung", 25))
        Exit.setStyleSheet(f"""
                QPushButton {{
                            background : none;
                            border: none;}}
                }}
                QPushButton:pressed {{
                                    background : white; 
                                    color: #000000; 
                                    font-weight: bold; 
                                    font-size : 18px; 
                                    border: none;
                                    border-radius: 10px;}}
                                    """)
        Exit.clicked.connect(self.exitGame)

    def exitGame(self):
        choice = QMessageBox.question(self, "Exit", "Êtes-vous sûrs de vouloir quitter ?",
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass


    # keyPressEvent est une fonction native a Qt elle permet de gérer les évènement
    def keyPressEvent(self, event):

        centralArea = centralWindow(self)

        gameScreenWindow = gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage), centralArea , "yo bro !")
        addPanelGoals(
            gameScreenWindow, 
            Stage.countMonster, 
            Stage.currentWorld, 
            "stage {}".format(Stage.currentStage), 
            Stage.countKey
        )

        createHeroPanel(gameScreenWindow, Hero.life)

        # j'appelle borderMap pour qu'elle soit connue de ma fonction keyPressEvent
        mapCell = drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)[1]
       
        # aller a droite
        if event.key() == 16777236:  # si l'utilisateur appuie sur la fleche droite
            # cette ligne empèche le personnage de sortir de la map
            if Hero.x <= 12:
                if "[{}, {}]".format(Hero.y, Hero.x+1) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):
                    for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["info"]:
                        if i["y"] == Hero.y and i["x"] == Hero.x+1:
                            # Voire les stats du monstre
                            if i["life"] > 0:
                                createMonsterPanel(
                                    gameScreenWindow, 
                                    i["name"],
                                    i["life"],
                                    i["strength"], 
                                    i["defense"], 
                                    i["level"], 
                                    i["progressPV"],
                                    Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],
                                
                                )
            
                                drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)
                                return
                            else:
                                Hero.x = Hero.x + 1 
                                drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)  
                                return

                elif "[{}, {}]".format(Hero.y, Hero.x+1) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["coordinate"]):
                    print("un coffre !")
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)

                else:
                    # et je la redéssine la map avec les nouvelle coordonnée du héro et la direction du sprite
                    Hero.x = Hero.x + 1 
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)

        # monter
        elif event.key() == 16777235:
            if Hero.y > 0:
                if "[{}, {}]".format(Hero.y-1, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):
                    for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["info"]:
                        if i["y"] == Hero.y-1 and i["x"] == Hero.x:
                            if i["life"] > 0 :
                                createMonsterPanel(
                                    gameScreenWindow, 
                                    i["name"],
                                    i["life"],
                                    i["strength"], 
                                    i["defense"], 
                                    i["level"], 
                                    i["progressPV"],
                                    Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],
                                
                                )
                
                                drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)
                            else:
                                Hero.y = Hero.y -1
                                drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)
                            return

                elif "[{}, {}]".format(Hero.y-1, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["coordinate"]):
                    print("un coffre !")
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)
                else:
                    Hero.y = Hero.y - 1
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)

        # descendre
        elif event.key() == 16777237:
            if Hero.y <= 8:
                if "[{}, {}]".format(Hero.y+1, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):
                    for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["info"]:
                            if i["y"] == Hero.y+1 and i["x"] == Hero.x:
                                if i["life"] > 0 :
                                    createMonsterPanel(
                                        gameScreenWindow, 
                                        i["name"],
                                        i["life"],
                                        i["strength"], 
                                        i["defense"], 
                                        i["level"], 
                                        i["progressPV"],
                                        Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],
                                        
                                    )
                    
                                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)

                                else:
                                    Hero.y = Hero.y + 1 
                                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)    
                                return

                elif "[{}, {}]".format(Hero.y+1, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["coordinate"]):
                    print("un coffre !")
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)

                else:
                    Hero.y = Hero.y + 1
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)

        # aller a gauche
        elif event.key() == 16777234:
            if Hero.x > 0:
                if "[{}, {}]".format(Hero.y, Hero.x-1) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):
                    for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["info"]:
                        if i["y"] == Hero.y and i["x"] == Hero.x-1:
                            if i["life"] > 0 :
                                createMonsterPanel(
                                    gameScreenWindow, 
                                    i["name"],
                                    i["life"],
                                    i["strength"], 
                                    i["defense"], 
                                    i["level"], 
                                    i["progressPV"],
                                    Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],
                                
                                )
                
                                drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)
                            else:
                                Hero.x = Hero.x - 1 
                                drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)    
                            return

                elif "[{}, {}]".format(Hero.y, Hero.x-1) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["coordinate"]):
                    print("un coffre !")
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)


                else:
                    Hero.x = Hero.x - 1
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)
#Droite ========================================================================================================================================
        # si j'appuie sur entrer j'attaque
        elif event.key() == 16777220 :

            for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["info"]:

                if i["y"] == Hero.y and i["x"] == Hero.x+1:

                    if i["life"] <= 0:
                        addAttackIndication(gameScreenWindow, "white")
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)
                        return

                    else:              
                        attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        i["progressPV"] =  i["progressPV"] - ((attack*100)/i["life"])

                        if i["life"] <= 0:
                            i["life"] = 0
                            i["progressPV"] = 0

                        createMonsterPanel(
                        gameScreenWindow, 
                            i["name"],
                            i["life"],
                            i["strength"], 
                            i["defense"], 
                            i["level"], 
                            i["progressPV"],
                            Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],       
                        )

                        addTextBox(gameScreenWindow,"vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))

                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)

                        time.sleep(2)

                        attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                        Hero.life = Hero.life - attackBack
                        Hero.progressHeroPv = Hero.progressHeroPv - ((attackBack*100)/Hero.life)

                        createHeroPanel(gameScreenWindow, Hero.life)

                        addTextBox(gameScreenWindow,"Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))

                        if i["life"] <= 0:

                            Stage.countMonster = Stage.countMonster + 1

                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            )

                            exp = int((100/Hero.level)*Stage.currentStage)
                            Hero.progressEXP = Hero.progressEXP + exp

                            if Hero.progressEXP == 100:
                                Hero.level = Hero.level +1
                                Hero.life = Hero.life+5
                                Hero.strength = Hero.strength+5
                                Hero.defense = Hero.defense+5
                                Hero.progressEXP = 0

                            elif Hero.progressEXP > 100:
                                Hero.level = Hero.level +1
                                Hero.life = Hero.life+5
                                Hero.strength = Hero.strength+5
                                Hero.defense = Hero.defense+5
                                reste = Hero.progressEXP - exp
                                Hero.progressEXP = reste


                            createHeroPanel(gameScreenWindow, Hero.life)

                            addTextBox(gameScreenWindow,"bravos le monstre a été vaincu, vous avez gagner {} d'exp".format(exp))

                            
                            RAND = random.randint(0,len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"])-1)
                           
                            if RAND == 0:
                                addTextBox(gameScreenWindow,"aucun objet reçus !")
                            else:
                                addTextBox(gameScreenWindow,"{},reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND]))
                                Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])]["image"])
                                addInventory(gameScreenWindow)

                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)               
                        return
#==========================================================================================================================================
#Monter===========================================================================================================================================
                elif i["y"] == Hero.y-1 and i["x"] == Hero.x:

                    if i["life"] <= 0:
                        print("le monstre est mort")
                        
                    else:

                        attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        i["progressPV"] =  i["progressPV"] - ((attack*100)/i["life"])

                        if i["life"] <= 0:
                            i["life"] = 0
                            i["progressPV"] = 0

                        createMonsterPanel(
                            gameScreenWindow, 
                            i["name"],
                            i["life"],
                            i["strength"], 
                            i["defense"], 
                            i["level"], 
                            i["progressPV"],
                            Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],       
                        )

                        addTextBox(gameScreenWindow,"vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))

                        time.sleep(2)

                        attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                        Hero.life = Hero.life - attackBack
                        Hero.progressHeroPv = Hero.progressHeroPv - ((attackBack*100)/Hero.life)

                        createHeroPanel(gameScreenWindow, Hero.life)

                        addTextBox(gameScreenWindow,"Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))

                        if i["life"] <= 0:

                            Stage.countMonster = Stage.countMonster + 1

                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            )

                            exp = int((100/Hero.level)*Stage.currentStage)
                            Hero.progressEXP = Hero.progressEXP + exp

                            if Hero.progressEXP == 100:
                                Hero.level = Hero.level +1
                                Hero.life = Hero.life+5
                                Hero.strength = Hero.strength+5
                                Hero.defense = Hero.defense+5
                                Hero.progressEXP = 0

                            elif Hero.progressEXP > 100:
                                Hero.level = Hero.level +1
                                Hero.life = Hero.life+5
                                Hero.strength = Hero.strength+5
                                Hero.defense = Hero.defense+5
                                reste = Hero.progressEXP - exp
                                Hero.progressEXP = reste

                            createHeroPanel(gameScreenWindow, Hero.life)
                            addTextBox(gameScreenWindow,"bravos le monstre a été vaincu, vous avez gagner XX d'exp")

                            RAND = random.randint(0,len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"])-1)
                           
                            if RAND == 0:
                                addTextBox(gameScreenWindow,"aucun objet reçus !")
                            else:
                                addTextBox(gameScreenWindow,"{}reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND]))  
                                Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])]["image"])
                                addInventory(gameScreenWindow)

                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)               
                        return
#Bas=============================================================================================================================================
                elif i["y"] == Hero.y+1 and i["x"] == Hero.x:

                    if i["life"] <= 0:
                        print("le monstre est mort")
                        
                    else:
                 
                        attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        i["progressPV"] =  i["progressPV"] - ((attack*100)/i["life"])

                        if i["life"] <= 0:
                            i["life"] = 0
                            i["progressPV"] = 0

                        createMonsterPanel(
                            gameScreenWindow, 
                            i["name"],
                            i["life"],
                            i["strength"], 
                            i["defense"], 
                            i["level"], 
                            i["progressPV"],
                            Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],
                        )
                        

                        addTextBox(gameScreenWindow,"vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))

                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)

                        time.sleep(2)

                        attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                        Hero.life = Hero.life - attackBack
                        Hero.progressHeroPv = Hero.progressHeroPv - ((attackBack*100)/Hero.life)

                        createHeroPanel(gameScreenWindow, Hero.life)

                        addTextBox(gameScreenWindow,"Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))

                        if i["life"] <= 0:

                            Stage.countMonster = Stage.countMonster + 1

                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            )

                            exp = int((100/Hero.level)*Stage.currentStage)
                            Hero.progressEXP = Hero.progressEXP + exp

                            if Hero.progressEXP == 100:
                                Hero.level = Hero.level +1
                                Hero.life = Hero.life+5
                                Hero.strength = Hero.strength+5
                                Hero.defense = Hero.defense+5
                                Hero.progressEXP = 0

                            elif Hero.progressEXP > 100:
                                Hero.level = Hero.level +1
                                Hero.life = Hero.life+5
                                Hero.strength = Hero.strength+5
                                Hero.defense = Hero.defense+5
                                reste = Hero.progressEXP - exp
                                Hero.progressEXP = reste

                            createHeroPanel(gameScreenWindow, Hero.life)
                            addTextBox(gameScreenWindow,"bravos le monstre a été vaincu, vous avez gagner XX d'exp")

                            RAND = random.randint(0,len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"])-1)
                           
                           
                            if RAND == 0:
                                addTextBox(gameScreenWindow,"aucun objet reçus !")
                            else:
                                addTextBox(gameScreenWindow,"{}reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND]))  
                                Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])]["image"])
                                addInventory(gameScreenWindow)

                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)               
                        return
#Gauche============================================================================================================================================
                elif i["y"] == Hero.y and i["x"] == Hero.x-1:

                    if i["life"] <= 0:
                        print("le monstre est mort")
                        
                    else:

                        attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        i["progressPV"] =  i["progressPV"] - ((attack*100)/i["life"])

                        if i["life"] <= 0:
                            i["life"] = 0
                            i["progressPV"] = 0

                        createMonsterPanel(
                            gameScreenWindow, 
                            i["name"],
                            i["life"],
                            i["strength"], 
                            i["defense"], 
                            i["level"], 
                            i["progressPV"],
                            Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],
                        )

                        addTextBox(gameScreenWindow,"vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))

                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)

                        time.sleep(2)

                        attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                        Hero.life = Hero.life - attackBack
                        Hero.progressHeroPv = Hero.progressHeroPv - ((attackBack*100)/Hero.life)

                        createHeroPanel(gameScreenWindow, Hero.life)

                        addTextBox(gameScreenWindow,"Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))

                        if i["life"] <= 0:

                            Stage.countMonster = Stage.countMonster + 1

                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            )

                            exp = int((100/Hero.level)*Stage.currentStage)
                            Hero.progressEXP = Hero.progressEXP + exp

                            if Hero.progressEXP == 100:
                                Hero.level = Hero.level +1
                                Hero.life = Hero.life+5
                                Hero.strength = Hero.strength+5
                                Hero.defense = Hero.defense+5
                                Hero.progressEXP = 0

                            elif Hero.progressEXP > 100:
                                Hero.level = Hero.level +1
                                Hero.life = Hero.life+5
                                Hero.strength = Hero.strength+5
                                Hero.defense = Hero.defense+5
                                reste = Hero.progressEXP - exp
                                Hero.progressEXP = reste

                            createHeroPanel(gameScreenWindow, Hero.life)
                            addTextBox(gameScreenWindow,"bravos le monstre a été vaincu, vous avez gagner XX d'exp")

                            RAND = random.randint(0,len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"])-1)
                            
                            if RAND == 0:
                                addTextBox(gameScreenWindow,"aucun objet reçus !")
                            else:
                                addTextBox(gameScreenWindow,"{}reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND]))   
                                Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])]["image"])
                                addInventory(gameScreenWindow)

                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)               
                        return
            for k in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["coordinate"]:
                if k[0] == Hero.y and k[1] == Hero.x+1:

                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)

                    if Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):

                        if Stage.dropInfo["clée du donjon"]["image"] in str(Stage.saveDropItems):
                            print("vous avez déja la clée")
                        else:    
                            addTextBox(gameScreenWindow,"{},reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0]))
                            Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0])]["image"])
                            addInventory(gameScreenWindow)

                            Stage.countKey = Stage.countKey +1

                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            ) 


                    else:
                        print("il reste des monstre a tuer")    
                    
                elif k[0] == Hero.y-1 and k[1] == Hero.x:

                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)

                    if Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):

                        if Stage.dropInfo["clée du donjon"]["image"] in str(Stage.saveDropItems):
                            print("vous avez déja la clée")
                        else:    
                            addTextBox(gameScreenWindow,"{},reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0]))
                            Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0])]["image"])
                            addInventory(gameScreenWindow)
                    else:
                        print("il reste des monstre a tuer") 

                    
                elif k[0] == Hero.y+1 and k[1] == Hero.x:

                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)
                    if Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):

                        if Stage.dropInfo["clée du donjon"]["image"] in str(Stage.saveDropItems):
                            print("vous avez déja la clée")
                        else:    
                            addTextBox(gameScreenWindow,"{},reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0]))
                            Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0])]["image"])
                            addInventory(gameScreenWindow)
                    else:
                        print("il reste des monstre a tuer") 
                    
                elif k[0] == Hero.y and k[1] == Hero.x-1:

                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)

                    if Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):

                        if Stage.dropInfo["clée du donjon"]["image"] in str(Stage.saveDropItems):
                            print("vous avez déja la clée")
                        else:    
                            addTextBox(gameScreenWindow,"{},reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0]))
                            Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0])]["image"])
                            addInventory(gameScreenWindow)
                    else:
                        print("il reste des monstre a tuer") 
                


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())
