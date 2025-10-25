from enum import Enum

class Environment(Enum):
    UNDERGROUND
    OVERGROUND

def createRoom(roomNumber):
    match (roomNumber): 
        case 3:
            pass
        
class Bug:
    def __init__(size: int, Environment, accessibility: int, occupied: [], cost: int):
        self.size = size
        self.accessibility = accessibility
        self.occupied = occupied
        self.cost = cost
