from colorama import just_fix_windows_console
import os

clear = lambda: os.system('cls')
just_fix_windows_console()

ESC_COLOR = "\x1b"
BACK=ESC_COLOR + "[48;5;"
TEXT=ESC_COLOR + "[38;5;"
RESET = ESC_COLOR + "[0m"

"""
#Make the bars a different color than the player team to keep different and imply as enemy's team
________________________________
1. (HP:000/000 MP:000/000) Marnmer
2. (HP:000/000 MP:000/000) Grundle Stumper 
3. (HP:000/000 MP:000/000) Xquic The All Mighty 
4. (HP:000/000 MP:000/000) Evil Centaur 
________________________________
#Title the name as Player's team to announce to user as their team
Player Team
_______________________
1. Centaur (Health: 022/022)
2. Centaur (Health: 022/022)
3. Centaur (Health: 022/022)
4. Centaur (Health: 022/022)
_______________________
Player Turn

Active character:
#Use Fraction at TEXT to represent how many members on team left
_____________________________________
1/4. Marnmer (Health: 026/026)
Strength: 4 Dexterity: 20 Constitution: 14
 Mind: 17 Wisdom: 9 Charisma: 2
_
        for x in range(256):
            print(str(x)+". " + BACK + str(x) + "m" + TEXT + str(x) + "m" + "WWWWWWWWWWW" + RESET)____________________________________

Actions:


1. Tazer Tooth


Stat used: Mind
Damage: 1-5 ('Piercing', 'Lightning') + Mind ('Piercing', 'Lightning') damage

Use teeth charged with electricity to deliver a paralyzing shock potentially reducing an enemy's dexterity



2
        for x in range(256):
            print(str(x)+". " + BACK + str(x) + "m" + TEXT + str(x) + "m" + "WWWWWWWWWWW" + RESET). Lightning Storm


Stat used: Mind
Damage: Mind*10 Lightning damage

Caster points to the sky chanting an incantation bringing forth a storm striking down lightning
  on a random creature on the field be it friend or foe


Choose Marnmer's action for the turn by choosing
the number corresponding to the action to use:

"""



def colorPalette(textType:bool = True):
    ESC_COLOR = "\x1b"
    BACK=ESC_COLOR + "[48;5;"
    TEXT=ESC_COLOR + "[38;5;"
    RESET = ESC_COLOR + "[0m"
    #textType set to true will give lines of color
    if(textType):
        for x in range(256):
            print(RESET + str(x)+". " + BACK + str(x) + "m" + TEXT + str(x) + "m" + "WWWWWWWWWWW")
    else:
        #textType set to False will give examples of text colored
        for x in range(256):
            print(str(x)+". " + TEXT + str(x) + "m" + "\tThe quick brown fox jumps over the lazy dog" + RESET)
        
    input("")
    

BLACK_TEXT = TEXT + "16m"

HP_BACK = BACK + "124m"
HP_TEXT= TEXT + "9m"

MP_BACK = BACK + "57m"
MP_TEXT = TEXT + "123m"


EARTH = BACK + "130m" + BLACK_TEXT
LIGHTNING = BACK + "11m" + BLACK_TEXT
FIRE = BACK + "166m" + BLACK_TEXT
CHICKEN = BACK + "211m" + BLACK_TEXT
NEUTRAL = BACK + "7m" + BLACK_TEXT
ENEMY = HP_TEXT
TEAM = MP_TEXT
MOVES = TEXT + "2m"
INT_COL = MP_TEXT
STR_COL = HP_TEXT
DEX_COL = TEXT + "3m"
SPI_COL = TEXT + "11m"



#Example Menu

print(ENEMY + "________________________________________________________________________________________" + RESET)
print("Enemy Team\t1/4 ("+HP_BACK+"HP"+RESET+":"+HP_TEXT+"111"+RESET+"/"+HP_TEXT+"111"+RESET+ " "+MP_BACK+"MP"+RESET+":"+MP_TEXT+"111"+RESET+"/"+MP_TEXT+"111"+RESET+") \t"+EARTH +"Earth"+RESET+"/"+ LIGHTNING+"Lightning"+RESET+" \tMarnmer")
print("\t\t2/4 ("+HP_BACK+"HP"+RESET+":"+HP_TEXT+"012"+RESET+"/"+HP_TEXT+"012"+RESET+ " "+MP_BACK+"MP"+RESET+":"+MP_TEXT+"000"+RESET+"/"+MP_TEXT+"000"+RESET+") \t"+FIRE+"Fire"+RESET+" \t\t\tGrundle Stumper")
print("\t\t3/4 ("+HP_BACK+"HP"+RESET+":"+HP_TEXT+"046"+RESET+"/"+HP_TEXT+"046"+RESET+ " "+MP_BACK+"MP"+RESET+":"+MP_TEXT+"346"+RESET+"/"+MP_TEXT+"346"+RESET+") \t"+CHICKEN+"CHICKEN"+RESET+" \t\tXquic The All Mighty")
print("\t\t4/4 ("+HP_BACK+"HP"+RESET+":"+HP_TEXT+"024"+RESET+"/"+HP_TEXT+"024"+RESET+ " "+MP_BACK+"MP"+RESET+":"+MP_TEXT+"052"+RESET+"/"+MP_TEXT+"052"+RESET+") \t"+NEUTRAL+"Neutral"+RESET+" \t\tEvil Centaur")
print(ENEMY + "________________________________________________________________________________________" + RESET)

print(TEAM + "________________________________________________________________________________________" + RESET)
print("Player Team \t1/4 ("+HP_BACK+"HP"+RESET+":"+HP_TEXT+"111"+RESET+"/"+HP_TEXT+"111"+RESET+ " "+MP_BACK+"MP"+RESET+":"+MP_TEXT+"111"+RESET+"/"+MP_TEXT+"111"+RESET+") \t"+EARTH +"Earth"+RESET+"/"+ LIGHTNING+"Lightning"+RESET+" \tMarnmer")
print("\t\t2/4 ("+HP_BACK+"HP"+RESET+":"+HP_TEXT+"012"+RESET+"/"+HP_TEXT+"012"+RESET+ " "+MP_BACK+"MP"+RESET+":"+MP_TEXT+"000"+RESET+"/"+MP_TEXT+"000"+RESET+") \t"+FIRE+"Fire"+RESET+" \t\t\tGrundle Stumper")
print("\t\t3/4 ("+HP_BACK+"HP"+RESET+":"+HP_TEXT+"046"+RESET+"/"+HP_TEXT+"046"+RESET+ " "+MP_BACK+"MP"+RESET+":"+MP_TEXT+"346"+RESET+"/"+MP_TEXT+"346"+RESET+") \t"+CHICKEN+"CHICKEN"+RESET+" \t\tXquic The All Mighty")
print("\t\t4/4 ("+HP_BACK+"HP"+RESET+":"+HP_TEXT+"024"+RESET+"/"+HP_TEXT+"024"+RESET+ " "+MP_BACK+"MP"+RESET+":"+MP_TEXT+"052"+RESET+"/"+MP_TEXT+"052"+RESET+") \t"+NEUTRAL+"Neutral"+RESET+" \t\tEvil Centaur")
print(TEAM + "________________________________________________________________________________________" + RESET)
print("ACTIVE:\t1/4 ("+HP_BACK+"HP"+RESET+":"+HP_TEXT+"111"+RESET+"/"+HP_TEXT+"111"+RESET+ " "+MP_BACK+"MP"+RESET+":"+MP_TEXT+"111"+RESET+"/"+MP_TEXT+"111"+RESET+") \t"+EARTH +"Earth"+RESET+"/"+ LIGHTNING+"Lightning"+RESET+" \tMarnmer")
print(STR_COL+"STR"+RESET+": 4 "+DEX_COL+"DEX"+RESET+": 20 "+INT_COL+"INT"+RESET+": 9 "+SPI_COL+"SPI"+RESET+": 2")

print(MOVES + "________________________________________________________________________________________" + RESET)
print("1. "+LIGHTNING+"Tazer Tooth" + RESET+"\t\tPOW:"+"1-5+"+INT_COL+"(INT)"+RESET+NEUTRAL+"\tPiercing"+RESET+"/"+LIGHTNING+"Lightning"+RESET)
print("2. "+LIGHTNING+"Lightning Storm" + RESET+"\tPOW:"+"10*"+INT_COL+"(INT)"+RESET+NEUTRAL+"\tPiercing"+RESET+"/"+LIGHTNING+"Lightning"+RESET)
print(MOVES + "________________________________________________________________________________________" + RESET)

input("")
