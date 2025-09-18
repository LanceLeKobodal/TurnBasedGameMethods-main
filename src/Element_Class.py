#universal character variables
from MenuColorPalette import *
"""
#Escape sequences for colors
ESCCOLOR = "\x1b"
BACK = ESC_COLOR + "[48;5;"
TEXT = ESC_COLOR + "[38;5;"
RESET = ESC_COLOR + "[0m"
BLACK_TEXT = TEXT + "16m"""
MAGIC_TEXT = BACK + "57m" + BLACK_TEXT
#List of all elements to help abbreviate and remove magic strings
#Basic Elements

neut = "Neutral"

fire = "Fire"
water = "Water"
earth = "Earth"
wind = "Wind"

ice = "Ice"
elec = "Lightning"
plant = "Plant"


#Spiritual elements
spirit = "Spirit"
death = "Death"
life = "Life"

#Attack Elements (No creatures will have these typings
pierce = "Piercing"
mPierce = "Magic Piercing"
slash = "Slashing"
mSlash = "Magic Slashing"
bludge = "Bludgeoning"
mBludge = "Magic Bludgeoning"


#Complex mode creature elements go here
river = "River"
wFire = "Wild Fire"

#Will mainly be used to determine weaknesses, resistances, immunities, and,
#SEAP (Same, Element, Action, Proficiency) #A bonus to actions increasing effectiveness
class Element:

        def __init__(self, ElName:str, ElSummary:str, ElWeaknesses:list[str], ElResistances:list[str], ElImmune:list[str],ElColor:str = ""):
            self.name = ElName
            self.summary = ElSummary
            self.weakness = ElWeaknesses
            self.resistance = ElResistances
            self.immunity = ElImmune
            self.color = ElColor

        #Will return an integer or float based on an element used
        def isWeak(self, enemyElement:str):
                #returnFate will be an int to be sent back to multiply damage
                returnFate:float = 0

                #Damage is increased if weak
                if (enemyElement in self.weakness):
                        returnFate = 2
                #Damage is reduced if resisted
                elif(enemyElement in self.resistance):
                        returnFate = 0.5
                #Damage is canceled if immune
                elif(enemyElement in self.immunity):
                        returnFate = 0
                else:
                        returnFate = 1
                
                return returnFate
        #Will return a float based on element used, actionEle must be an Element Class object
        def isSEAP(self, actionEle:str):
                #returnBoost will be an int to be sent back to multiply damage or effectiveness
                #if the move is the same element or is a supported element of an attacking element
                returnBoost = 1

                if(self.name == actionEle):
                        returnBoost = 1.5
                        
                return returnBoost

"""
#Example Element Class creation documentation
   #Name of Element# must be changed to element name
get"(Element)"():
        "(Element)"Name = ""
        "(Element)"Summary = ""
        "(Element)"Weak = []
        "(Element)"Resist = []
        "(Element)"Immune = []
        return"(Element)" = ""
                                     #This stays as Element
        return"(Element)" = Element(elementName, elementSummary, elementWeak, elementResist, elementImmune)

        return return"(Element)"

"""

#Physical Elements go here

#isMagic helps make a second physical element type without having to make a whole new method
def getPierce(isMagic:bool = False):

        pierceColor = ""
        
        if(isMagic):
                pierceName = mPierce
                pierceColor = MAGIC_TEXT
        else:
                pierceName = pierce
        pierceSummary = "Result of a tipped object thrusting into a target"
        pierceWeak:list[str] = []
        pierceResist:list[str] = []
        pierceImmune:list[str] = []
        

        returnPierce = Element(pierceName, pierceSummary, pierceWeak, pierceResist, pierceImmune, pierceColor)

        return returnPierce

#isMagic helps make a second physical element type without having to make a whole new method
def getSlash(isMagic:bool = False):

        slashColor = ""

        if(isMagic):
                slashName = mSlash
                slashColor = MAGIC_TEXT
        else:
                slashName = slash
        slashSummary = "Result of a sharp object cutting into a target"
        slashWeak:list[str] = []
        slashResist:list[str] = []
        slashImmune:list[str] = []
        

        returnSlash = Element(slashName, slashSummary, slashWeak, slashResist, slashImmune, slashColor)

        return returnSlash

#isMagic helps make a second physical element type without having to make a whole new method
def getBludge(isMagic:bool = False):

        bludgeColor = ""

        if(isMagic):
                bludgeName = mBludge
                bludgeColor = MAGIC_TEXT
        else:
                bludgeName = bludge
        bludgeSummary = "Result of a blunt object bashing into a target"
        bludgeWeak:list[str] = []
        bludgeResist:list[str] = []
        bludgeImmune:list[str] = []
        

        returnBludge = Element(bludgeName, bludgeSummary, bludgeWeak, bludgeResist, bludgeImmune, bludgeColor)

        return returnBludge

#Elements that get attached to creatures go here

def getNeut():
        neutName = neut
        neutSummary = "Lack of elemental affinity"
        neutWeak:list[str] = [fire]
        neutResist:list[str] = []
        neutImmune:list[str] = []
        neutColor = BACK + "15m" + BLACK_TEXT
                                     
        returnNeut = Element(neutName, neutSummary, neutWeak, neutResist, neutImmune, neutColor)

        return returnNeut

def getFire():
        fireName = fire
        fireSummary = "A basic element. The element of Consumption, Willpower, and Warmth"
        fireWeak:list[str] = [water, earth]
        fireResist:list[str] = [fire, plant, wind]
        fireImmune:list[str] = []
        fireColor = BACK + "166m" + BLACK_TEXT
                                     
        returnFire = Element(fireName, fireSummary, fireWeak, fireResist, fireImmune,fireColor)

        return returnFire

def getWater():
        waterName = water
        waterSummary = "A basic element. The element of Life, Cold, and Wetness"
        waterWeak:list[str] = [plant, elec]
        waterResist:list[str] = [fire, water, ice]
        waterImmune:list[str] = []
        waterColor = BACK + "33m" + BLACK_TEXT
                                     
        returnWater = Element(waterName, waterSummary, waterWeak, waterResist, waterImmune, waterColor)

        return returnWater

def getWind():
        windName = wind
        windSummary = "A basic element. The element of Air, Sky, Flight, Freedom"
        windWeak:list[str] = [earth]
        windResist:list[str] = [plant]
        windImmune:list[str] = []
                                     
        returnWind = Element(windName, windSummary, windWeak, windResist, windImmune)

        return returnWind

def getEarth():
        earthName = earth
        earthSummary = "A basic element. The element of The Ground, Sturdiness, Resilience, and Protection"
        earthWeak:list[str] = [earth, bludge, mBludge, water, plant]
        earthResist:list[str] = [wind, slash, pierce, fire, death]
        earthImmune:list[str] = [elec]
        earthColor = BACK + "130m" + BLACK_TEXT
                                     
        returnEarth = Element(earthName, earthSummary, earthWeak, earthResist, earthImmune, earthColor)

        return returnEarth

def getPlant():
        plantName = "Plant"
        plantSummary = "A gift from the ground and waters below. The element of Life, Growth, and Connection"
        plantWeak:list[str] = [fire, wind, slash, mSlash, ice]
        plantResist:list[str] = ["Water", "Plant", "Lightning"]
        plantImmune:list[str] = []
        plantColor = BACK + "2m" + BLACK_TEXT
                                     
        returnPlant = Element(plantName, plantSummary, plantWeak, plantResist, plantImmune, plantColor)

        return returnPlant
        

def getElec():
        lightningName = elec
        lightningSummary = "A gift of the skies and flames above. The element of Energy, Connection, and Electricity"
        lightningWeak:list[str] = [earth]
        lightningResist:list[str] = [plant]
        lightningImmune:list[str] = []
        lightningColor = BACK + "3m" + BLACK_TEXT
                                     
        returnLightning = Element(lightningName, lightningSummary, lightningWeak, lightningResist, lightningImmune, lightningColor)

        return returnLightning

def getSpirit():
        spiritName = spirit
        spiritSummary = "An eventual result of Life leaving the body behind. The element of Connection, Rememberance, and Life Eternal"
        spiritWeak:list[str] = [spirit]
        spiritResist:list[str] = [life, death]
        spiritImmune:list[str] = [slash, pierce, bludge]
                                     
        returnSpirit = Element(spiritName, spiritSummary, spiritWeak, spiritResist, spiritImmune)

        return returnSpirit

def getLife():
        lifeName = life
        lifeSummary = "The true source of all living energy. The element of Connection, Healing, Purity"
        lifeWeak:list[str] = [death, fire]
        lifeResist:list[str] = [life, water, plant]
        lifeImmune:list[str] = [slash, pierce, bludge]
        lifeColor = BACK + "11m" + BLACK_TEXT
                                     
        returnLife = Element(lifeName, lifeSummary, lifeWeak, lifeResist, lifeImmune, lifeColor)

        return returnLife

def getDeath():
        deathName = death
        deathSummary = "The result of the life given to a spirit given physical form hanging by a thread. The element of rebith, reconnection, and necromancy"
        deathWeak:list[str] = [life, fire, plant]
        deathResist:list[str] = [spirit, death]
        deathImmune:list[str] = [slash, pierce, bludge]

        returnDeath = Element(deathName, deathSummary, deathWeak, deathResist, deathImmune)

        return returnDeath

def getIce():
        iceName = ice
        iceSummary = "The result of water being frozen giving it a more solid form"
        iceWeak:list[str] = [fire, bludge, mBludge, earth]
        iceResist:list[str] = [plant, ice]
        iceImmune:list[str] = []

        returnIce = Element(iceName, iceSummary, iceWeak, iceResist, iceImmune)

        return returnIce

#Complex mode creature Elements go here
def getRiver():
        #riverBase = water
        
        riverName = river
        riverSummary = "Water given direction down a stream"
        riverWeak:list[str] = [ice, plant, elec]
        riverResist:list[str] = [water, fire]
        riverImmune:list[str] = []

        returnRiver = Element(riverName, riverSummary, riverWeak, riverResist, riverImmune)

        return returnRiver

def getWildFire():
        #wFireBase = fire

        wFireName = wFire
        wFireSummary = "The result of a small fire in nature gone astray burning everything in it's path"
        wFireWeak:list[str] = [fire, earth]
        wFireResist:list[str] = []
        wFireImmune:list[str] = [plant, wind]

        returnWFire = Element(wFireName, wFireSummary, wFireWeak, wFireResist, wFireImmune)

        return returnWFire