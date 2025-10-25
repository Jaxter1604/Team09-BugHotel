import random
from BugClass import Bug, PreyOrPredator, Environment
from RoomClass import Room


def CalcHappiness(bug: Bug, room: Room):
    
    budget = bug.budget / room.cost
    size = 1 + ((room.size - bug.size)/2)
    # agro = calcAgro(Room,Bug)
    if bug.canFly:
        access = 1
    elif bug.prefferedEnvironment == Environment.UNDERGROUND:
        access = 1
    else:
        access = (room.accessibility - 10) * (-1/5)

    # add agro back
    if room.environment == bug.prefferedEnvironment:
        happiness = 5 * budget * size * access
    else:
        happiness = 5 * budget * size * access - 2

    return happiness