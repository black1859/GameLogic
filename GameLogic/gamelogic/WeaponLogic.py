
#just weapon.
class Weapon():
    def __init__(self,name = 'weapon',damage = 3) -> None:
        self.name = name
        self.damage = abs(damage)
        self.additional = 0

    def attack(self,target):
        target.addHp(-(self.damage+self.additional))
        self.additional = 0
    
    #I'm not sure that it is necessary. but if u wanna put critical attack, it will be necessary.
    def boost(self,b = 0):
        self.additional = abs(b)

class Sword(Weapon):
    def __init__(self, name='sword', damage=5, sharpness = 30):
        super().__init__(name, damage)
        self.sharpness = sharpness
