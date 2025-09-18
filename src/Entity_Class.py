from MenuColorPalette import *
from Element_Class import Element
from Element_Class import *
from Attack_Class import Attack
from Weapon_Class import Weapon

#Class responsible for entity abilities

class Entity:
    """entityStats should be given in the order of :
    Strength, Dexterity, Vigor, Endurance, Intelligence, Mind, Faith all being
    given as integers"""
    def __init__(self, entityName:str, entityStats:list[int], entityRace:str, entityElement:list[Element]):
        #Will be used to display the name of this creature as a string
        self.name = entityName
        #stored as int
        self.strength = entityStats[0]
        #color for strength stat
        self.strColor = TEXT + "m"
        #stored as int
        self.dexterity = entityStats[1]
        #color for dexterity stat
        self.dexColor = TEXT + "3m"
        #stored as int
        self.vigor = entityStats[2]
        #color for vigor stat
        self.vigColor = TEXT + "9m"
        #stored as int
        self.endurance = entityStats[3]
        #color for endurance stat
        self.endColor = TEXT + "10m"
        #stored as int
        self.intelligence = entityStats[4]
        #color for intelligence stat
        self.intColor = TEXT + "12m"
        #stored as int
        self.mind = entityStats[5]
        #color for mind stat
        self.mindColor = TEXT + "123m"
        #stored as int
        self.spirit = entityStats[6]
        #color for spirit stat
        self.spiColor = TEXT + "11m"
        #Lists all the attacks in an easy to loop in list form likely for attacks
        self.allStats = entityStats
        #Will be used to store items that the creature is holding
        self.inventory = []
        #Active item a character is holding will be stored here as an item Class or it's children 
        self.mainHand = ""
        #race of the entity being stored as a string
        self.race = entityRace
        #calulated based on how high the vigor stat is. Do not manipulate for damage calculations
        self.healthMax = self.vigor * 10
        #manipulate this one for current health and damage taken
        self.health = self.healthMax
        #color for HP numbers
        self.hpColor = self.vigColor
        #color for HP highlight
        self.hpBACK = BACK + "124m"
        #color for SP numbers
        self.spColor = self.endColor
        #color for HP highlight
        self.spBACK = BACK + "2m"
        #calculated based on how high the mind stat is
        self.manaMax = self.mind * 15
        #manipulate this one for current mp used up
        self.mana = self.manaMax
        #color for MP numbers
        self.mpColor = self.mindColor
        #color for MP highlight
        self.mpBACK = BACK + "57m"
        #Stores the elements an entity may have
        self.elementType = entityElement
        #Stored as a list of attacks
        self.attacks:list[Attack] = []
                            #itemEquipped is stored as an item Class or any of it's children
    def equipMainHand(self, itemEquipped:Weapon):
        self.mainHand = itemEquipped

    #Displays Entity elements and formats the colors
    def elementConsoleHandler(self):
        try:
            #Testing to see if there are multiple elements in selfelementType
            x=len(self.elementType)
            for x in self.elementType:
                if(x == self.elementType[len(self.elementType)-1]):
                    print(str(x.color)+str(x.name)+RESET, end="")
                else:
                    print(str(x.color)+str(x.name)+RESET, end="/")
        except:
            print(str(self.elementType[0].color) + str(self.elementType[0].name)+RESET, end="\t")

    #Returns a string of a number converted to 3 digets
    def tripleDigitConverter(self, number:int):
        convertedNumber = str(number)
        if(number < 10):
            convertedNumber = "00" + str(number)
        elif(number < 100):
            convertedNumber = "0" + str(number)
        elif(number > 999):
            convertedNumber = "999"

        return convertedNumber

    def addAttack(self, newAttack:Attack):
        self.attacks.append(newAttack)

    


class Monster(Entity):
    def __init__(self, entityName:str, entityStats:list[int], entityRace:str, entityElement:list[Element]):
        super().__init__(entityName, entityStats, entityRace, entityElement)

    def getStatus(self):

        #Converts hp to 3 digits
        hpDisplay = self.tripleDigitConverter(self.health)
        hpMaxDisplay = self.tripleDigitConverter(self.healthMax)
        
        #Makes display for hp red
        print("("+self.hpBACK+"HP"+RESET+":"+self.hpColor+hpDisplay+RESET+"/"+self.hpColor+
              hpMaxDisplay+RESET, end=" ")

        #Converts mp to 3 digits
        mpDisplay = self.tripleDigitConverter(self.mana)
        mpMaxDisplay = self.tripleDigitConverter(self.manaMax)
        
        #Makes display for mp blue
        print(self.mpBACK+"MP"+RESET+":"+self.mpColor+mpDisplay+RESET+"/"+self.mpColor+
              mpMaxDisplay+RESET+")", end = "\t")
        #Displays any elemental types an entity has and colors accordingly
        self.elementConsoleHandler()
        #Displays the name
        print("\t"+self.name)

    def getOffensiveStats(self):
        
        #Starts the menu off with an indent
        print(end="\t")

        #fetches Strength stat
        print(STR_COL + "STR" + RESET, end=": ")
        print(self.strength, end = " ")

        #fetches Dexterity stat
        print(DEX_COL + "DEX" + RESET, end=": ")
        print(self.dexterity, end=" ")

        #fetches Intelligence stat
        print(INT_COL + "INT" + RESET, end=": ")
        print(self.intelligence, end=" ")

        #fetches Spirit stat
        print(SPI_COL + "SPI" + RESET, end=": ")
        #End sequence different here to make a new line for the next part of the menu
        print(self.spirit)