from functions.game_functions.Items import *

def addItemsInInventory(MapCellInventory):
    # elle doit sauvegarder les items dans l'inventaire

    count = 0
    
    for i in Items.SaveDropItems:
        ItemImage = MapCellInventory[count][0]
        ItemImage.setGeometry(0 ,0 , 40 , 40)
        ItemImage.setStyleSheet(i)
        count = count + 1





        