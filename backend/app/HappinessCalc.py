import random
from BugClass import Bug, PreyOrPredator, Environment
from RoomClass import Room


def CalcHappiness(bug: Bug, room: Room, prey_penalty, pred_bonus):
    
    budget = bug.budget / room.cost
    size = 1 + ((room.size - bug.size)/2)
    
    if bug.preyOrPredator == PreyOrPredator.PREY:
        agro = pred_bonus[room.position[0]][room.position[1]]
    else:
        agro = prey_penalty[room.position[0]][room.position[1]]

    if bug.canFly:
        access = 1
    elif bug.prefferedEnvironment == Environment.UNDERGROUND:
        access = 1
    else:
        access = (room.accessibility - 10) * (-1/5)

    # add agro back
    if room.environment == bug.prefferedEnvironment:
        happiness = 5 * budget * size * access * agro
    else:
        happiness = 5 * budget * size * access * agro - 2

    if happiness < 0:
        return 0
    
    if happiness > 5:
        return 5

    return happiness