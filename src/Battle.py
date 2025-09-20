from Entity_Class import *
from MenuColorPalette import * 
from typing import List


#This is where the battling gets handled
def startBattle(teamPlayer:List[Monster], teamEnemy:List[Monster]):
    turnFlipper = True
    enemyColor = TEXT + "13m"
    playerColor = TEXT + "33m"
    allTeams = [teamPlayer, teamEnemy]
    allTeamColors = [playerColor, enemyColor]
    moveUsed = 0
    targetBool = False
    targetUsed = 0

    while len(allTeams) > 1:
        #This cleans up the menu screen and clears it
        clearConsole()
        
        #This is where the field display is calculated
        while(turnFlipper):
            teamCount = 0
            
            for _ in teamPlayer:
                #This will stay false until no more exceptions are shown
                isTurnComplete = False    
                #Continues the loop until a proper move option has been
                while(isTurnComplete == False):
                    clearConsole()
                    getBattleField(allTeams, allTeamColors)
                    getPlayerDisplay(teamPlayer,teamCount)
                    moveUsed = getPlayerMove(teamPlayer, teamCount)
                    if (moveUsed != -1):
                        targetUsed, targetBool = getPlayerTarget(allTeams,allTeamColors, teamPlayer[teamCount], moveUsed)
                    if (targetUsed != -1 and moveUsed != -1):
                        doPlayerTurn(allTeams, allTeamColors, teamPlayer[teamCount], teamPlayer[teamCount].attacks[moveUsed], targetUsed, targetBool)
                        isTurnComplete = True
                teamCount = teamCount + 1
                


#Handles displaying team information
def getTeamDisplay(teamStatus:List[Monster], isPlayer:bool = True):
    teamCount = 0
    if(isPlayer):
        print("Player Team")
    else:
        print("Enemy Team")

    for x in teamStatus:
        teamCount = teamCount+1
        print("\t"+str(teamCount) + "/" + str(len(teamStatus)), end="\t")
        x.getStatus()

#Handles displaying the current status and offensive stats for an active creature on team
def getActiveCreatureDisplay(activeCreature:Monster, teamNum:int, teamTotoal:int):

    print("Active Creature")
    print(str(teamNum) + "/" + str(teamTotoal), end="\t")
    activeCreature.getStatus()
    activeCreature.getOffensiveStats()

#Handles displaying attack information
def getAttackDisplay(moveList:List[Attack]):
    moveCount = 0
    print("Moves")
    for moves in moveList:
        moveCount = moveCount+1
        
        print(str(moveCount), end=" ")
        moves.getStatus()
    
def getBattleField(teams:List[List[Monster]], teamColors:List[str]):
    
    activeColor = 0
    playerBool = True
    for team in teams:
        getLine(teamColors[activeColor])
        if(activeColor != 0):
            playerBool = False
        getTeamDisplay(team, playerBool)
        getLine(teamColors[activeColor])
        activeColor = activeColor+1

    
#Makes a consistent line
def getLine(color:str = ""):
    print(color+"________________________________________________________________________________________"+RESET)


def getPlayerDisplay(playerTeam:list[Monster], activeMember:int):
    #Section that displays the stats on an active team member
    getActiveCreatureDisplay(playerTeam[activeMember], (activeMember+1), len(playerTeam))
    #Section that displays the moves on an active team member
    getLine(MOVES)
    getAttackDisplay(playerTeam[activeMember].attacks)
    getLine(MOVES)

#This helps get a choice from the player for the monster's attack being used
#This will also check if the input it valid
def getPlayerMove(fieldTeam:list[Monster], monsterAttacking:int):
                                                #Shows the max number of moves dynamically
    playerChoice = input("Choose a number between 1 and " + str(len(fieldTeam[monsterAttacking].attacks)) + " to choose an attack: ")

    try:
        playerChoice = int(playerChoice) - 1
        if fieldTeam[monsterAttacking].attacks[playerChoice].name == str:
            print(True)
    except:
        playerChoice = -1
        print("Sorry you must type a number between 1 and " + str(len(fieldTeam[monsterAttacking].attacks)) + " ")
        input("Press enter to continue...")

    print(str(playerChoice))
          
    return playerChoice

def getPlayerTarget(allFieldTeams:list[list[Monster]], allFieldTeamsColors:list[str], activeMonster:Monster, moveChosen:int):
    
    inputCheck = -1
    isAttackComplete = False
    targetChosen = 0
    isAlly = False
    activeMove = activeMonster.attacks[moveChosen]
    resetMove:bool = False
    while(isAttackComplete == False):
        clearConsole()
        getBattleField(allFieldTeams,allFieldTeamsColors)
        activeMonster.getStatus()
        activeMonster.getOffensiveStats()
        getLine(MOVES)
        print("Move used:")
        activeMove.getStatus(True)
        getLine(MOVES)

        print("To chose an enemey please type a number between 1 and " + str(len(allFieldTeams[1])))
        print("To chose an ally please type a number between -1 and -" + str(len(allFieldTeams[0])))
        print("To choose a different move type the number 0")
        targetChosen = input("Make your choice: ")

        try:
            targetChosen = int(targetChosen)
        
        except:
            targetChosen = -100

        

        #This ends the loop if a player wants to pick a different move
        if(targetChosen == inputCheck + 1):
            isAttackComplete = True
            resetMove = True
        #This converts the user choice to be compatable with list indexes
        else:
            if(targetChosen > inputCheck + 1):
                input("Sees enemy")
                targetChosen = targetChosen -1
                isAlly = False
            elif(targetChosen <= inputCheck + 1):
                input("Sees ally")
                targetChosen = targetChosen + 1
                isAlly = True

        #This is the error handler area
        #Area where it checks if any of the options given to the player were chosen
        
        #Checks if the target on the enemy side exists
    
        if(targetChosen > len(allFieldTeams[1])-1) :
            targetChosen = -100
            
        elif(targetChosen < (len(allFieldTeams[0])- 1)*-1):
            
            targetChosen = -100

        #This handles displaying the error to the user without stopping the program
        if (targetChosen == -100):
            print("Sorry you need to try again please choose a good number")
            input("Press enter to continue...")

        
        if(targetChosen != -100):
            isAttackComplete = True

    if(not resetMove):
                    
        print("Target chosen:")
        if(isAlly):
            print(allFieldTeams[0][targetChosen].name)
        elif(not isAlly):
            print(allFieldTeams[1][targetChosen].name)
        input("Press enter to continue...")
    else:
        targetChosen = -1
    return targetChosen, isAlly # pyright: ignore[reportPossiblyUnboundVariable]

def doPlayerTurn(allFieldTeams:list[list[Monster]], allFieldTeamColors:list[str],creatureAttacking:Monster, selectedMove:Attack, selectedTarget:int, isFriend:bool):
    clearConsole()

    creatureTargeted:Monster = allFieldTeams[0][0]

    #Hadles checking which side of the field is getting hit with an attack

    #If true, it'll target the player team side
    if(isFriend):
        creatureTargeted = allFieldTeams[0][selectedTarget]
    #if False it'll target the enemy team side
    if(not isFriend):
        creatureTargeted = allFieldTeams[1][selectedTarget]

    totalDamage:float = 0

    #gets multiplier from SEAP
    totalDamage = SEAPCheck(creatureAttacking, selectedMove)

    #gets multiplier from target resistances or weaknesses and multiplies it with the SEAP multiplier
    totalDamage = totalDamage * elementalInteraction(creatureTargeted, selectedMove)

    totalDamage = selectedMove.damage(creatureAttacking.allStats[selectedMove.stat], totalDamage)

    creatureTargeted.health = creatureTargeted.health - int(totalDamage)

    #this handles displaying what actually took place during the turn
    #if total damage is positive it'll show a damage message
    if(totalDamage > 0):
        print(creatureTargeted.name + " took " + str(totalDamage) + " damage to their health!")
    #if total damage is negative it'll show a healing message
    elif(totalDamage < 0):
        print(creatureTargeted.name + "healed by " + str(totalDamage * -1))

    input("Press enter to continue...")


    """
    Need to check elemental interactions for both the creature attacking for SEAP as well as
    any damage multipliers from the enemy getting hit with an elemental attack

    no need to calculate defense reductions until there is a need for armor to be added and armor may just increase stats rather than calculate damage reduction
    """

#This figures out how much of a multiplier a targeted monster will take based on the elements used in an attack vs the elements the monster has itself
def elementalInteraction(affectedMonster:Monster, actionTaken:Attack):

    elementMulti:float = 0
    totalMulti:float = 1

    eleWeak = 1.5
    eleResist = 0.5
    eleImmune = 0

    weakCol = BACK + "160m"
    resistCol = BACK + "57m"
    immuneCol = BACK + "7m" + BLACK_TEXT

    for affinity in affectedMonster.elementType:
        for moveAffinity in actionTaken.elementType:
            elementMulti = affinity.isWeak(moveAffinity.name)
            if(elementMulti == eleWeak):
                print(affectedMonster.name + " is " + weakCol + "WEAK" + RESET + " to " + moveAffinity.color + moveAffinity.name + RESET, end = "")
                print(" element due to it's affinity to " + affinity.color + affinity.name +RESET +"!")
            elif(elementMulti == eleResist):
                print(affectedMonster.name + " is " + resistCol + "RESISTANT" + RESET + " to " + moveAffinity.color + moveAffinity.name + RESET, end = "")
                print(" element due to it's affinity to " + affinity.color + affinity.name +RESET +"!")
            elif(elementMulti == eleImmune):
                print(affectedMonster.name + " is " + immuneCol + "IMMUNE" + RESET + " to " + moveAffinity.color + moveAffinity.name + RESET, end = "")
                print(" element due to it's affinity to " + affinity.color + affinity.name +RESET +"!")
            totalMulti = totalMulti * elementMulti

    return totalMulti

#This checks if the monster shares any elements with the attacks being used and returns a multiplier as float to multiply with the damage
def SEAPCheck(attackingMonster:Monster, moveCheck:Attack):
    attackMulti = 0
    totalMulti = 1

    #Selects each element separately a creature may have
    for profEle in attackingMonster.elementType:
        #selects each element separately a move may have
        for ele in moveCheck.elementType:
            attackMulti = ele.isSEAP(profEle.name)
            totalMulti = totalMulti * attackMulti

    return totalMulti