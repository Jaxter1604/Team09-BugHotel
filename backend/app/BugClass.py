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
class Ants(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(1,3)
        super().__init__(
            species="Ant",
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREY,
            agression=3,
            canFly=False,
            size=size,
            preferredEnvironment=Environment.UNDERGROUND
        )

class Beetles(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(3,7)
        super().__init__(
            species="Beettle",
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREY,
            agression=2,
            canFly=random.choice([True, False]),
            size=size,
            preferredEnvironment=Environment.OVERGROUND
        )

class Flies(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(1,4)
        super().__init__(
            species="Fly",
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREY,
            agression=1,
            canFly=True,
            size=size,
            preferredEnvironment=Environment.OVERGROUND
        )

class Worm(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(4,8)
        super().__init__(
            species="Worm",
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREY,
            agression=1,
            canFly=False,
            size=size,
            preferredEnvironment=Environment.UNDERGROUND
        )

class Bee(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(3,6)
        super().__init__(
            species="Bee",
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREY,
            agression=5,
            canFly=True,
            size=size,
            preferredEnvironment=Environment.OVERGROUND
        )

class Wasp(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(4,7)
        super().__init__(
            species="Wasp",
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREDATOR,
            agression=7,
            canFly=True,
            size=size,
            preferredEnvironment=Environment.OVERGROUND
        )

class Caterpillar(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(3,7)
        super().__init__(
            species="Caterpillar",
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREY,
            agression=2,
            canFly=False,
            size=size,
            preferredEnvironment=Environment.OVERGROUND
        )

class Butterfly(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(6,10)
        super().__init__(
            species="Butterfly",
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREY,
            agression=1,
            canFly=True,
            size=size,
            preferredEnvironment=Environment.OVERGROUND
        )

class Moth(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(4,11)
        super().__init__(
            species="Moth",
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREY,
            agression=3,
            canFly=True,
            size=size,
            preferredEnvironment=Environment.OVERGROUND
        )

class Grasshopper(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(8,11)
        super().__init__(
            species="Grasshopper",
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREDATOR,
            agression=9,
            canFly=False,
            size=size,
            preferredEnvironment=Environment.OVERGROUND
        )

class Mosquito(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(4,8)
        super().__init__(
            species="Mosquito",
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREDATOR,
            agression=10,
            canFly=True,
            size=size,
            preferredEnvironment=Environment.OVERGROUND
        )
