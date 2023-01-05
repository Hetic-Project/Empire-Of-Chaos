import time
from functions.game_functions.addAttackIndication import addAttackIndication

def countdown(n, gameWindow, color):
   while n > 0 :
    print(n)
    n = n-1
    if n == 0:
        addAttackIndication(gameWindow, color)
    else:
        t = int(n/100000)
        print(t,"s")    