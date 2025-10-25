from enum import Enum

class PreyOrPreditor(Enum):
    PREDATOR
    PREY

class Environment(Enum):
    UNDERGROUND

def createBug(bugName):
    match (bugName): 
        case "spider":
            pass
        


class Bug:
    def __init__(species: str, budget: int, preyOrPreditor, agression: int, canFly: bool, agression: int, visibility: int, preferredEnvironment, sprite_path: str, size: int):
        self.species = species
        self.preyOrPreditor = preyOrPreditor
        self.agression = agression
        self.canFly = canFly
        self.visibility = visibility
        self.sprite_path = sprite_path



