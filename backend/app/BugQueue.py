import random
from BugClass import Ant, Beetle, Fly, Worm, Bee, Wasp, Caterpillar, Butterfly, Moth, Grasshopper, Mosquito, Spider
from BugClass import PreyOrPredator

class QueueNode:
    def __init__(self,value,position):
        self.value=value
        self.position=position
        self.next=None

    def increasePosition(self):
        if not self.next is None:
            self.next.increasePosition(self.next)
        self.position-=1
        #In react they adjust their position accordingly

class BugQueue:
    def __init__(self):
        self.head=None
        self.last=self.head
        self.length=-1

    def addNode(self,newNode):
        if self.head is None:
            self.head=newNode
            self.last=self.head
        else:
            self.last.next=newNode
            self.last=self.last.next
        self.length+=1
        #In react, bug added to next spot in list, they spawn from off screen and walk to (100- 35*length)x, 0 y

    def pop(self):
        if not self.head is None:
            returnNode=self.head.value
            self.head=self.head.next
            self.head.increasePosition(self.head)
            self.length-=1
            return returnNode #Negative/-1 length is empty
            #Whenever room allocation starts, first queue member popped

def generate_queue(num_bugs: int, pred_ratio: float = 0.25):
    
    bugs = [Ant, Spider, Beetle, Fly, Bee, Wasp, Worm, Caterpillar, Grasshopper, Moth, Mosquito, Butterfly]

    predators = [pred for pred in bugs if pred().preyOrPredator == PreyOrPredator.PREDATOR]
    prey = [prey for prey in bugs if prey().preyOrPredator == PreyOrPredator.PREY]

    num_pred = int(num_bugs * pred_ratio)

    pred_indexes=set(random.sample(range(0, num_bugs), num_pred))

    bug_queue = BugQueue()

    for i in range(0,num_bugs):
        if i in pred_indexes:
            BugClass = random.choice(predators)
            bug_queue.addNode(QueueNode(BugClass(),bug_queue.length+1))
        else:
            BugClass = random.choice(prey)
            bug_queue.addNode(QueueNode(BugClass(),bug_queue.length+1))

    #random.shuffle(bug_queue)
    return bug_queue


"""test code
bugs_list = generate_queue(35)
for bug in bugs_list:
    print(f"{bug.species}: {bug.preyOrPredator}, CanFly: {bug.canFly}, Aggression: {bug.agression}, Size: {bug.size}, PreferredEnv: {bug.prefferedEnvironment}")
"""
