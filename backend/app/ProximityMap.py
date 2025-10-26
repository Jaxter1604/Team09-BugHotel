from BugClass import PreyOrPredator

PREY_UNHAPPY_WEIGHT = 1.0
PREDATOR_BONUS_WEIGHT = 0.4
PREY_SIGNAL_RADIUS = 2

def manhattan(rowA, colA, rowB, colB):
    return abs(rowA - rowB) + abs(colA - colB)

def decay(d):
    return 1.0 / (1 + d)

def radius_from_aggression(aggr):
    if aggr >= 10: return 4
    if aggr >= 8: return 3
    if aggr >= 6: return 2
    if aggr >= 4: return 1
    return 0

def compute_heatmaps(hotel):
    rows, cols = hotel.rows, hotel.cols
    prey_penalty = [[0.0 for _ in range(cols)] for _ in range(rows)]
    predator_bonus = [[0.0 for _ in range(cols)] for _ in range(rows)]

    predators = [] 
    prey = []

    for r in range(rows):
        for c in range(cols):
            room = hotel.grid[r][c]
            occs = getattr(room, "occupied", None)
            if occs is None:
                occs = []
                if getattr(room, "occupiedBy", None) is not None:
                    occs.append(room.occupiedBy)

            for occ in occs:
                if occ.preyOrPredator == PreyOrPredator.PREDATOR:
                    predators.append((r, c, occ.aggression))
                elif occ.preyOrPredator == PreyOrPredator.PREY:
                        prey.append((r, c))

    for predrow, predcol, aggression in predators:
        radius = radius_from_aggression(aggression)
        if radius == 0:
            continue
        rowmin, rowmax = max(0, predrow - radius), min(rows - 1, predrow + radius)
        colmin, colmax = max(0, predcol - radius), min(cols - 1, predcol + radius)
        for r in range(rowmin, rowmax + 1):
            for c in range(colmin, colmax + 1):
                d = manhattan(predrow, predcol, r, c)
                if d <= radius:
                    prey_penalty[r][c] -= PREY_UNHAPPY_WEIGHT * decay(d)

    for preyrow, preycol in prey:
        radius = PREY_SIGNAL_RADIUS
        rowmin, rowmax = max(0, preyrow - radius), min(rows - 1, preyrow + radius)
        colmin, colmax = max(0, preycol - radius), min(cols - 1, preycol + radius)
        for r in range(rowmin, rowmax + 1):
            for c in range(colmin, colmax + 1):
                d = manhattan(preyrow, preycol, r, c)
                if d <= radius:
                    predator_bonus[r][c] += PREDATOR_BONUS_WEIGHT * decay(d)

    print(prey_penalty)
    return prey_penalty, predator_bonus