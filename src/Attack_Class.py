from Element_Class import *


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
    def damage(self, userStat:int, weaknessMulti:int = 1):
        totalDamage:float = 0

        totalDamage = (self.power/100) * userStat * weaknessMulti

        return totalDamage

#Abbreaveations for the attacking stats
STR_ABB = "STR"
DEX_ABB = "DEX"
INT_ABB = "INT"
SPI_ABB = "SPI"


fireBolt = Attack("Fire Bolt", [getFire()], 40, INTEL, INT_ABB, INT_COL)
waterBolt = Attack("Water Bolt", [getWater()], 40, INTEL, INT_ABB, INT_COL)
vineWhip = Attack("Vine Whip", [getPlant(), getBludge(True)], 40, SPI, SPI_ABB, SPI_COL)
slashAttack = Attack("Slash", [getNeut(),getSlash()], 40, STRENGTH, STR_ABB, STR_COL)
