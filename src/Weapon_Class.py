
#Class responsible for weapon information

#TODO make an item class parent

class Weapon:
                        
    def __init__(self, weaponName:str, weaponBaseDamage:int = 40, weaponWeight:int = 0):
        #Will be used to display the name of the item in inventory as a string
        self.name = weaponName
        #Will be used to calculate damage from the item as a base value
        self.damage = weaponBaseDamage
        #Will be used to calculate weight load of the item
        self.weight = weaponWeight
