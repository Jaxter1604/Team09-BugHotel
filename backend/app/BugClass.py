from enum import Enum
import random

class PreyOrPreditor(Enum):
    PREDATOR = "Predator"
    PREY = "Prey"

class Environment(Enum):
    UNDERGROUND = "Underground"
    OVERGROUND = "Overground" 

class Bug:
    def __init__(self, species: str, budget: int, preyOrPredator, agression: int, canFly: bool, preferredEnvironment, size: int):
        self.species = species
        self.budget = budget
        self.preyOrPredator = preyOrPredator
        self.agression = agression
        self.canFly = canFly
        self.size = size

class Spider(Bug):
    def __init__(self):
        budget = random.randrange(50,201,10)
        size = random.randrange(6,10)
        super().__init__(
            species=Spider,
            budget=budget,
            preyOrPredator=PreyOrPreditor.PREDATOR,
            agression=10,
            canFly=False,
            size=size,
            preferredEnvironment=Environment.OVERGROUND
        )
