from Entity_Class import *
from MenuColorPalette import * 
from typing import List

def startBattle(teamPlayer:List[Monster], teamEnemy:List[Monster]):
    turnFlipper = True
    enemyColor = TEXT + "13m"
    playerColor = TEXT + "33m"
    allTeams = [teamPlayer, teamEnemy]
    allTeamColors = [playerColor, enemyColor]

    while len(allTeams) > 1:
        #This cleans up the menu screen and clears it
        clearConsole()
        teamCount = 0
        #This is where the field display is calculated
        while(turnFlipper):
            teamCount = 0
            for _ in teamPlayer:
            
                clearConsole()
                getBattleField(allTeams, allTeamColors)
                getPlayerDisplay(teamPlayer,teamCount)
                input("")
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
        
        print(str(moveCount) + ". " + moves.elementType[0].color + moves.name, end= RESET + "\t")
        print("POW: " + str(moves.power), end=" ")
        print(str(moves.statColor) + "(" + str(moves.statName) + ")" + RESET, end="\t")

        elementCount = 1
        for element in moves.elementType:
            if(len(moves.elementType)== elementCount):
               print(element.color + element.name, end=RESET+".\n")
            elif(elementCount < len(moves.elementType)):
                print(element.color + element.name, end=RESET+"/")
                elementCount = elementCount + 1
    
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