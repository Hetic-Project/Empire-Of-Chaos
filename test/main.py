import sys


from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar


class MainWindow(QMainWindow):

    # j'appel la fonction constructeur
    def __init__(self):

        # je rappel le constructeur parent
        super().__init__()

        # self représente la fenètre de l'app ici je donne un titre a la fenètre
        self.setWindowTitle("Empire Of Chaos")

        # donner une taille minimum a la fenètre
        self.setMinimumSize(800, 600)

        # afficher une infobule
        self.setToolTip("Empire Of Chaos")

        # On change l'icône affichée dans le bandeau supérieur de la fenêtre.
        self.setWindowIcon(QIcon("test/icons/rpg.png"))

        # On retaille la fenêtre (800 pixels de large et 600 en hauteur).
        self.resize(800, 600)

        # Création d'une barre de prégréssion
        progressBar = QProgressBar(self)
        progressBar.setGeometry(250, 250, 300, 30)
        progressBar.setMaximum(100)
        progressBar.setValue(50)


if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # Instancier votre fenêtre graphique.
    window = MainWindow()
    # et afficher votre fenêtre graphique.
    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())
