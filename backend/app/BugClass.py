from enum import Enum, auto
import random

class PreyOrPreditor(Enum):
    PREDATOR = auto()
    PREY = auto()

class Environment(Enum):
    UNDERGROUND = "Underground"
    OVERGROUND = "Overground" 

class Bug:
    def __init__(self, species: str, budget: int, preyOrPredator:PreyOrPreditor, canFly: bool, agression: int, preferredEnvironment:Environment, size: int):
        self.species = species
        self.budget = budget
        self.preyOrPredator = preyOrPredator
        self.prefferedEnvironment = preferredEnvironment
        self.agression = agression
        self.size = size
    
    def genRandomBug():
        Bugs = [Ant,Beetle,Fly,Worm,
        Bee,Wasp,Caterpillar,Butterfly,
        Moth,Grasshopper,Mosquito,Spider]

        BugNum = random.randrange(0,12)

        return Bugs[BugNum]
        

    def GetSpecificBug(bugname):
        match bugname:
            case "Spider":
                return Spider
            case "Ant":
                return Ant
            case "Beetle":
                return Beetle
            case "Fly":
                return Fly
            case "Worm":
                return Worm
            case "Bee":
                return Bee
            case "Wasp":
                return Wasp
            case "Caterpillar":
                return Caterpillar
            case "Butterfly":
                return Butterfly
            case "Moth":
                return Moth
            case "Grasshopper":
                return Grasshopper
            case "Mosquito":
                return Mosquito
            
        
    



class Spider(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(6,10)
        super().__init__(
            species="Spider",
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREDATOR,
            agression=10,
            canFly=False,
            size=size,
            preferredEnvironment=Environment
        )
