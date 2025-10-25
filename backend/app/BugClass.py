from enum import Enum, auto

class PreyOrPreditor(Enum):
    PREDATOR = auto()
    PREY = auto()

class Environment(Enum):
    UNDERGROUND

def createBug(bugName):
    match (bugName): 
        case "spider":
            pass
        


class Bug:
    def __init__(species: str, budget: int, preyOrPreditor, agression: int, canFly: bool, preferredEnvironment, sprite_path: str, size: int):
        self.species = species
        self.preyOrPreditor = preyOrPreditor
        self.agression = agression
        self.canFly = canFly
        self.sprite_path = sprite_path



