from enum import Enum, auto
import random

class PreyOrPredator(Enum):
    PREDATOR = "Predator"
    PREY = "Prey"

class Environment(Enum):
    UNDERGROUND = "Underground"
    OVERGROUND = "Overground"

class Bug:
    def __init__(self, species: str, budget: int, preyOrPredator:PreyOrPredator, canFly: bool, aggression: int, prefferedEnvironment:Environment, size: int):
        self.species = species
        self.budget = budget
        self.canFly = canFly
        self.preyOrPredator = preyOrPredator
        self.prefferedEnvironment = prefferedEnvironment
        self.aggression = aggression
        self.size = size
 
    def genRandomBug(self):
        Bugs = [Ant,Beetle,Fly,Worm,
        Bee,Wasp,Caterpillar,Butterfly,
        Moth,Grasshopper,Mosquito,Spider]

        BugNum = random.randrange(0,12)

        return Bugs[BugNum]

    def GetSpecificBug(self, bugname):
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
            preyOrPredator=PreyOrPredator.PREDATOR,
            aggression=10,
            canFly=False,
            size=size,
            prefferedEnvironment=Environment.OVERGROUND
        )

class Ant(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(1,3)
        super().__init__(
            species="Ant",
            budget=budget,
            preyOrPredator=PreyOrPredator.PREY,
            aggression=3,
            canFly=False,
            size=size,
            prefferedEnvironment=Environment.UNDERGROUND
        )

class Beetle(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(3,7)
        super().__init__(
            species="Beetle",
            budget=budget,
            preyOrPredator=PreyOrPredator.PREY,
            aggression=2,
            canFly=random.choice([True, False]),
            size=size,
            prefferedEnvironment=Environment.OVERGROUND
        )

class Fly(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(1,4)
        super().__init__(
            species="Fly",
            budget=budget,
            preyOrPredator=PreyOrPredator.PREY,
            aggression=1,
            canFly=True,
            size=size,
            prefferedEnvironment=Environment.OVERGROUND
        )

class Worm(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(4,8)
        super().__init__(
            species="Worm",
            budget=budget,
            preyOrPredator=PreyOrPredator.PREY,
            aggression=1,
            canFly=False,
            size=size,
            prefferedEnvironment=Environment.UNDERGROUND
        )

class Bee(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(3,6)
        super().__init__(
            species="Bee",
            budget=budget,
            preyOrPredator=PreyOrPredator.PREY,
            aggression=5,
            canFly=True,
            size=size,
            prefferedEnvironment=Environment.OVERGROUND
        )

class Wasp(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(4,7)
        super().__init__(
            species="Wasp",
            budget=budget,
            preyOrPredator=PreyOrPredator.PREDATOR,
            aggression=7,
            canFly=True,
            size=size,
            prefferedEnvironment=Environment.OVERGROUND
        )

class Caterpillar(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(3,7)
        super().__init__(
            species="Caterpillar",
            budget=budget,
            preyOrPredator=PreyOrPredator.PREY,
            aggression=2,
            canFly=False,
            size=size,
            prefferedEnvironment=Environment.OVERGROUND
        )

class Butterfly(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(6,10)
        super().__init__(
            species="Butterfly",
            budget=budget,
            preyOrPredator=PreyOrPredator.PREY,
            aggression=1,
            canFly=True,
            size=size,
            prefferedEnvironment=Environment.OVERGROUND
        )

class Moth(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(4,11)
        super().__init__(
            species="Moth",
            budget=budget,
            preyOrPredator=PreyOrPredator.PREY,
            aggression=3,
            canFly=True,
            size=size,
            prefferedEnvironment=Environment.OVERGROUND
        )

class Grasshopper(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(8,11)
        super().__init__(
            species="Grasshopper",
            budget=budget,
            preyOrPredator=PreyOrPredator.PREDATOR,
            aggression=9,
            canFly=False,
            size=size,
            prefferedEnvironment=Environment.OVERGROUND
        )

class Mosquito(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(4,8)
        super().__init__(
            species="Mosquito",
            budget=budget,
            preyOrPredator=PreyOrPredator.PREDATOR,
            aggression=10,
            canFly=True,
            size=size,
            prefferedEnvironment=Environment.OVERGROUND
        )
