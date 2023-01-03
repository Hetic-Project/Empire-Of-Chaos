import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Empire of Chaos")
        self.setWindowIcon(QIcon("icons/yes.png"))

        centralWidget = QWidget()

        self.__button1 = QPushButton("Start Game", centralWidget)
        self.__button1.setGeometry(500, 300, 200, 35)



        self.__button2 = QPushButton("Load Game", centralWidget)
        self.__button2.setGeometry(500, 350, 200, 35)



        self.__button3 = QPushButton("Credits", centralWidget)
        self.__button3.setGeometry(500, 400, 200, 35)


        self.__button4 = QPushButton("Exit", centralWidget)
        self.__button4.setGeometry(500, 450, 200, 35)

        self.setCentralWidget(centralWidget)



if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    # TODO : Instancier et afficher votre fenêtre graphique.

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())