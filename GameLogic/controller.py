from gamelogic.ItemLogic import Item, Healpack
from gamelogic.WeaponLogic import Weapon
from gamelogic.PlayerLogic import Player,getUser
from EventController import get_besthealpack,get_wrosthealpack
import random
#load
user = getUser()
user.status()
user.name = "Steve"
gameOn = 1
while gameOn:
    userchoice = int(input("1/2/3  (0): "))

    if userchoice == 1:
        if random.choice([True,False]):
            get_wrosthealpack()
        else:
            get_besthealpack()
    elif userchoice == 2:
        #after you get item onGame, you can't use it. after restarting , you can use it. it is bug!
        # I think the item maker(roading part) is correct. but return item part has some error
        user.useItem((1,2))
    elif userchoice == 3:
        user.status()
    elif userchoice == 4:
        user.useItem((1,1))
    elif userchoice == 5:
        print("Hp -10")
        user.addHp(-10)
    else:
        gameOn = 0
