import random
from BugClass import Bug, PreyOrPredator, Environment
from HotelClass import Hotel
from RoomClass import Room

def CalcHappiness():
    
    budget = Bug().budget / Room().cost
    size = 1 + ((Room().size - Bug().size)/2)
    agro = calcAgro(Room(),Bug())
    if Bug().canFly:
        access = 1
    elif Bug().prefferedEnvironment == Environment.UNDERGROUND:
        access = 1
    else:
        access = (Room().accessibility - 10) * (-1/5)

    if Room().environment == Bug().prefferedEnvironment:
        happiness = 5 * budget * size * agro * access
    else:
        happiness = 5 * budget * size * agro * access - 2
    
def CalcHotelHappiness():
    for i in range()
