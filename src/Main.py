from monsters import *
from Weapon_Class import *
from Battle import *

#This will be the base greatsword character when not in use by a player
                        #Strength, Dexterity, Vigor, Endurance, Intelligence, Mind, Faith
greatswordChar = Entity("Guts", [15,8,12,13,10,8,12], "Human", [getNeut()])

#This will be the vessel weapon greatsword that will be tied to the greatsword hero
vesselGreatsword = Weapon("Vessel Greatsword", 100, 100)

#Equips the Vessel Greatsword to the Greatsword Hero
greatswordChar.equipMainHand(vesselGreatsword)

#This will be the base greatsword character when not in use by a player
lanceChar = Entity("Lance", [15,8,12,13,10,8,12], "Kobold", [getFire()])
vesselLance = Weapon("Vessel Lance", 25,  15)

#Equips the Vessel Lance to the Lance hero
lanceChar.equipMainHand(vesselLance)


#Test enemy
boogleWeasles = Monster("Boogle of Weasels", [8,15,12,10,8,12,17], "Weasel", [getNeut()])
weaselBite = Weapon("Bite", 15, 1)

boogleWeasles.equipMainHand(weaselBite)

"""
Weasels are thieves high in rewards low in exp
will steal consumables or gold on attack
They have strong belief in the boogle
"""

startBattle(team1, team2)
