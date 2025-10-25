from enum import Enum, auto

class Environment(Enum):
    UNDERGROUND = auto()
    OVERGROUND = auto()

def createRoom(roomNumber):
    match (roomNumber):
        case 3:
            pass
   
class Room:
    def __init__(self, size: int, environment: Environment, accessibility: int, occupied: [], cost: int, position: []):
        self.size = size
        self.environment = environment
        self.accessibility = accessibility
        self.occupied = occupied
        self.cost = cost
        self.position = position
