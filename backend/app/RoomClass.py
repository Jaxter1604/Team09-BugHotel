from BugClass import Bug
from enum import Enum, auto

class Environment(Enum):
    UNDERGROUND = auto()
    OVERGROUND = auto()

def createRoom(roomNumber):
    match (roomNumber):
        case 3:
            pass
   
class Room:
    def __init__(self, size: int, environment: Environment, accessibility: int, cost: int, position: [], roomNo: int):
        self.size = size
        self.environment = environment
        self.accessibility = accessibility
        self.occupiedBy = None
        self.cost = cost
        self.position = position
        self.roomNo = roomNo
