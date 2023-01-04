import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QWidget, QLabel, QDialog, \
    QRadioButton, QLineEdit


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createOption = None
        self.gameOption = None
        self.credits = None
        self.gameOption = QWidget()
        self.openGameOption = self.openGameOption
        self.openCreateOption = self.openCreateOption
        self.openCredits = self.openCredits
        self.exitGame = self.exitGame

        self.setWindowTitle("Empire Of Chaos")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(1200, 1030)
        self.setToolTip("Empire Of Chaos")

        centralWidget = QWidget()

     

        self.setCentralWidget(centralWidget)




    def openCredits(self):
        credits = "Développeurs :\n Lucas YALMAN & Mohamed YAICH"
        label_credits = QLabel(credits, self)
        layout = self.layout()
        layout.addWidget(label_credits)
        centralWidget = QWidget()
        self.__button = QPushButton("Back", centralWidget)
        self.__button.setGeometry(620, 480, 300, 40)
        self.__button.clicked.connect(self.show_menu)
        self.setCentralWidget(centralWidget)

    def show_menu(self):
        centralWidget = QWidget()
        self.__button = QPushButton("Create Game", centralWidget)
        self.__button.setGeometry(620, 360, 300, 40)
        self.__button.clicked.connect(self.openCreateOption)

        self.__button = QPushButton("Load Game", centralWidget)
        self.__button.setGeometry(620, 400, 300, 40)
        self.__button.clicked.connect(self.openGameOption)

        self.__button = QPushButton("Credits", centralWidget)
        self.__button.setGeometry(620, 440, 300, 40)
        self.__button.clicked.connect(self.openCredits)

        self.__button = QPushButton("Exit", centralWidget)
        self.__button.setGeometry(620, 480, 300, 40)
        self.__button.clicked.connect(self.exitGame)
        self.setCentralWidget(centralWidget)

    def exitGame(self):
        choice = QMessageBox()
        choice.setStyleSheet("background-color: white;")
        choice = choice.question(self, "Exit", "Êtes-vous sûrs de vouloir quitter ?",
                                    QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass






if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainmenu = MainMenu()
    mainmenu.show()


    sys.exit(app.exec())