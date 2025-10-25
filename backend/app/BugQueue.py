import random
from BugClass import Ant, Beetle, Fly, Worm, Bee, Wasp, Caterpillar, Butterfly, Moth, Grasshopper, Mosquito, Spider
from BugClass import PreyOrPredator

def generate_queue(num_bugs: int, pred_ratio: float = 0.25):
    
    bugs = [Ant, Spider, Beetle, Fly, Bee, Wasp, Worm, Caterpillar, Grasshopper, Moth, Mosquito, Butterfly]

    predators = [pred for pred in bugs if pred().preyOrPredator == PreyOrPredator.PREDATOR]
    prey = [prey for prey in bugs if prey().preyOrPredator == PreyOrPredator.PREY]

    num_pred = int(num_bugs * pred_ratio)
    num_prey = num_bugs - num_pred

    bug_queue = []

    for i in range(num_pred):
        BugClass = random.choice(predators)
        bug_queue.append(BugClass())

    for i in range(num_prey):
        BugClass = random.choice(prey)
        bug_queue.append(BugClass())

    random.shuffle(bug_queue)
    return bug_queue


"""test code
bugs_list = generate_queue(35)
for bug in bugs_list:
    print(f"{bug.species}: {bug.preyOrPredator}, CanFly: {bug.canFly}, Aggression: {bug.agression}, Size: {bug.size}, PreferredEnv: {bug.prefferedEnvironment}")
"""
