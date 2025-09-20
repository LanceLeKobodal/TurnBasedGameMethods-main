from Element_Class import *
import math

STRENGTH = 0
DEX = 1
INTEL = 4
SPI = 6
class Attack:

    """atPower should be treated as a percent multiplier
a power of 40 will do 40% of the charater's attacking stat

Strength, Dexterity, Vigor, Endurance, Intelligence, Mind, Spirit
use this list when deciding the atStat number

use these to abbreviate stat types for characters
STR, DEX, VIG, END, INT, MIND, SPI
"""

    def __init__(self, atName:str, atElement:list[Element], atPower:int, atStat:int, statStr:str = "None", calledStatColor:str = ""):
        self.name = atName
        self.elementType = atElement
        self.power = atPower
        self.stat = atStat
        self.statName = statStr
        self.summary = "This is a work in progress"
        self.statColor = calledStatColor
    
    #By using self.stat a character's attacking stat can be passed as userStat and multiplied by self.power as a percentage
    def damage(self, userStat:int, weaknessMulti:float = 1):
        totalDamage:float = 0

        totalDamage = math.floor((self.power/100) * userStat * weaknessMulti)

        return totalDamage
    
    def getStatus(self, isDetaled:bool = False):
        
        print(self.elementType[0].color + self.name, end= RESET + "\t")
        print("POW: " + str(self.power), end=" ")
        print(str(self.statColor) + "(" + str(self.statName) + ")" + RESET, end="\t")

        elementCount = 1
        for element in self.elementType:
            if(len(self.elementType)== elementCount):
               print(element.color + element.name, end=RESET+".\n")
            elif(elementCount < len(self.elementType)):
                print(element.color + element.name, end=RESET+"/")
                elementCount = elementCount + 1

        if(isDetaled):
            print(self.summary)


#Abbreaveations for the attacking stats
STR_ABB = "STR"
DEX_ABB = "DEX"
INT_ABB = "INT"
SPI_ABB = "SPI"


fireBolt = Attack("Fire Bolt", [getFire()], 40, INTEL, INT_ABB, INT_COL)
waterBolt = Attack("Water Bolt", [getWater()], 40, INTEL, INT_ABB, INT_COL)
vineWhip = Attack("Vine Whip", [getPlant(), getBludge(True)], 40, SPI, SPI_ABB, SPI_COL)
slashAttack = Attack("Slash", [getNeut(),getSlash()], 40, STRENGTH, STR_ABB, STR_COL)
ram = Attack("Ram", [getNeut(), getBludge()], 40, STRENGTH, STR_ABB, STR_COL)
milkDrink = Attack("Milk Drink", [getLife()], -40, SPI, SPI_ABB, SPI_COL)
thrust = Attack("Thrust", [getNeut(), getPierce()], 40, DEX, DEX_ABB, DEX_COL)
elecBolt = Attack("Lightning Bolt", [getElec()], 80, INTEL, INT_ABB, INT_COL)
mushroomStamp = Attack("Mushroom Stamp", [getEarth(),getBludge(True)], 40, SPI, SPI_ABB, SPI_COL)
mindChatter = Attack("Mind Chatter", [getPsi()], 40, INTEL, INT_ABB, INT_COL)
