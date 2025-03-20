
#basic foundation of Item
class Item():
    def __init__(self,name:str, itemCode:int, itemType:int, description:str, target) -> None:
        self.name = name
        self.__itemData = (itemCode,itemType)
        self.target = target
        self.description = description

    def useItem(self):
        pass

    def introduce(self):
        return self.description
    
    def returnData(self):
        return self.__itemData

#healpack은 player가 사용함. -> 적에게 힐팩을 주지 않는 이상 힐팩은 항상 유저한테 넘어가야함
#if all of item are used by player, don't have to make paramter get player
class Healpack(Item):
    itemCode = 1
    Texts = {1 :('best Heal pack', 'Hp + 10'), 2 :('wrost Heal pack', "Hp + 5")}
    Details = {1: 10, 2: 5}
    
    """
    I'm not sure that how can I fix it.
    First time, I didn't intend that user parameter recieve player object. <- I found the way!
    But I don't know what would be better way. 
    """
    def __init__(self, itemType = 1, user = None) -> None:
        if user:
            p =user
        else:
            #for avoid circular error
            from PlayerLogic import getUser
            p = getUser()
        
        name, text = Healpack.Texts[itemType]
        self.heal = Healpack.Details[itemType]
        super().__init__(name = name, itemCode= Healpack.itemCode, itemType = itemType, description = text, target = p)

    def useItem(self):
        self.target.addHp(self.heal)
        
#this will make project more difficulty
"""class attackboost(Item):
    
    boostertexts = {1:('best booster pack','+3 additional damage'),2:('wrost booster pack','+1 additional damgae')}
    boostertype = {1:3, 2:1}

    def __init__(self, type : int, user) -> None:
        self.type = type
        name, text = self.boostertexts[type]
        self.user = user
        super().__init__(name, text)
"""



#when loading game file, json return a list.
# So, I needed something returning data.
#  But it works at healpack yet.
#the healpack works only about player.
def itemMaker(itemData = (1,1),player = None,weaponboost = None) -> Item:
    itemCode, itemType = itemData
    if itemCode == 1:
        return Healpack(itemType= itemType, user= player)
