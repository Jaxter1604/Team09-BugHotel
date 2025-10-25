from enum import Enum, auto

class Environment(Enum):
    UNDERGROUND = auto()
    OVERGROUND = auto()

def createRoom(roomNumber):
    match (roomNumber):
        case 3:
            pass
<<<<<<< HEAD
        
class Room:
    def __init__(self, size: int, environment, accessibility: int, occupied: [], cost: int, position: []):
=======
   
class Room:
    def __init__(self, size: int, environment: Environment, accessibility: int, occupied: [], cost: int):
>>>>>>> 4dc02f0b1d7852b8c8550342ed2a6c34c5f4dbad
        self.size = size
        self.environment = environment
        self.accessibility = accessibility
        self.occupied = occupied
        self.cost = cost
        self.position = position
