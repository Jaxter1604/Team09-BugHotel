from enum import Enum, auto

class Environment(Enum):
    UNDERGROUND = auto()
    OVERGROUND = auto()

def createRoom(roomNumber):
    match (roomNumber):
        case 3:
            pass
   
class Bug:
    def __init__(self, size: int, environment: Environment, accessibility: int, occupied: [], cost: int):
        self.size = size
        self.environment = environment
        self.accessibility = accessibility
        self.occupied = occupied
        self.cost = cost
