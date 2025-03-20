from typing import List
import sys, json, atexit
sys.path.append(r'C:\Codes\pythons\GameLogic\gamelogic')
from ItemLogic import Item, Healpack, itemMaker
from WeaponLogic import Weapon


class Player():

    def __init__(self,name : str = "someone", Hp : int = 20, maxHp : int = 20, location : str = None,weaponName : str = "fist", weaponDamage : int = 3, items : List[Item] = []):
        self.name = name
        self.Hp = Hp
        self.maxHp = maxHp
        self.weapon = Weapon(weaponName,weaponDamage)
        self.location = location
        self.Inventory = self.Backpack()
        if items:
            self.Inventory.setItems(items,self)

    def addHp(self,n : int):
        self.Hp += n
        if self.Hp >self.maxHp:
            self.Hp = self.maxHp
    
    #I tried to make Item dic for easier managing. but I think it is not necessary. 
    #   So if you decide to manage parameter as a object, it is Ok.
    def getItem(self, item : Item):
        self.Inventory.addItem(item)
    #this is same issue, maybe I already made it.
    def useItem(self,itemData=(1,1)):
        self.Inventory.useItem(itemData,user= self.name)

    def attack(self, target):
        if target:
            self.weapon.attack(target)
            print(f"{self.name} attack {target.name} with {self.weapon.name}\n{target.name} Hp is {target.Hp}")
        else:
            self.weapon.attack(self)
            print(f"{self.name} attack {self.name} with {self.weapon.name}\n{self.name} Hp is {self.Hp}")

    def status(self):
        print("\n=================")
        print(f"name: {self.name}, Hp: {self.Hp}/{self.maxHp}\nweapon: {self.weapon.name} damage: {self.weapon.damage}\nlocation: {self.location}")
        self.Inventory.showSpace()
        print("=================\n")

    def returnData(self):
        data = {
            'name':self.name,
            'Hp':self.Hp,
            'maxHp':self.maxHp,
            'weapon':{"weaponName":self.weapon.name,"weaponDamage":self.weapon.damage},
            'inventory':self.Inventory.returnData(),
            'location':self.location,
            'ability':{
                'speed':3,
                'careless':4,
                'armor':9,
                'stress':30
                }
            }
        return data

    #nested class
    class Backpack():
        def __init__(self,items : List[Item] = []) -> None:
            self.space:List[Item] = items

        #this Method return Item object address
        def searchItem(self, itemData = (1,1)) -> Item:
            item = None
            if self.isEmpty():
                print("backpack is empty")
            else:
                for i in self.space:
                    if i.returnData() == itemData:
                        item = i
                        break
            return item

        #maybe it is same issue to manage items. but it is Ok.
        def useItem(self,itemData = (1,1),user = None):
            item = self.searchItem(itemData)
            if not item:
                print("you don't have it")
            else:
                item.useItem()
                print(f'{item.name} used by {user}')
                self.__removeItem(item)
            
        #if you wanna put other events like lost event, you can turn on this Method
        def __removeItem(self,item : Item):
            self.space.remove(item)
        #inventory limit
        def addItem(self,item : Item):
            self.space.append(item)

        def showSpace(self):
            if self.isEmpty():
                print("backpack is empty")
            else:
                print(f"\nInventory [{len(self.space)} / 5] \n[",end=" ")
                for i in self.space:
                    print(f"{i.name}",end=",")
                print("]")

        #this is loading part.
        # when userData file has Inventory data, automatically append items in backpack 
        def setItems(self, Datas : list, user):
            itemDatas = []
            for d in Datas:
                data = (d[0],d[1])
                itemDatas.append(data)

            for data in itemDatas:
                self.space.append(itemMaker(data,user))

        #this is saving part
        def returnData(self):
            items = []
            if self.isEmpty():
                return None
            else:
                for item in self.space:
                    items.append(item.returnData())
                return items
        #just empty
        def isEmpty(self):
            return not self.space

useraddress = r"C:\Codes\pythons\GameLogic\jsons\ userData.json"
#data format
data = {
    'name':'someone',
    'Hp':20,
    'maxHp':20,
    'weapon':{"weaponName":"fist","weaponDamage":10},
    'inventory':[],
    'location':'the blind forest',
    'ability':{
        'speed':3,
        'careless':4,
        'armor':9,
        'stress':30
    }
}

"""
This code is for managing datas when game loading. 
need file examinaton
"""
#load
try:
    with open(useraddress, 'r', encoding='utf-8') as file:
        data = json.load(file)

except FileNotFoundError:
    with open(useraddress, "w", encoding='utf-8') as datas:
        json.dump(obj=data, fp=datas, indent=4)
    # Load the default data after creating the file
    data = json.loads(json.dumps(data))  # Use the same default data

# Now you can work with 'data' 
# make player object, "user". 
# in all files, they will use this player object
user = Player(data['name'],
              data['Hp'],
              data['maxHp'],
              data['location'],
              data['weapon']['weaponName'],data['weapon']['weaponDamage'],
              data['inventory'])


"""
Next codes are for loading and saving. 
Basically the user data will be managed in this file.
Now, you need to make New Files for controlling user data.
"""
#load
def getUser() -> Player:
    return user

#save
def saver() -> None:
    data = user.returnData()
    with open(useraddress, "w", encoding='utf-8') as datas:
        json.dump(obj=data, fp=datas, indent=4)
    print("saved")
#this code forces saving all times
atexit.register(saver)

if __name__ == "__main__":
    user.status()