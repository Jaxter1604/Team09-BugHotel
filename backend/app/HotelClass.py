from RoomClass import Room
from BugClass import Bug
from HappinessCalc import CalcHappiness

class Hotel:
    def __init__(self, rows=7, cols=5):
        self.rows = rows
        self.cols = cols
        self.grid = []
        self.create_grid()

    def add_bug_to_room(self, newOccupant: Bug, row_index, column_index):
        room = self.grid[row_index][column_index]
        if room.occupiedBy is not None:
            print("Room already occupied")
            return False

        room.occupiedBy = newOccupant
        print(f"{newOccupant.species} added to Room {room.roomNo}")

        self.recalc_all_happiness()

        print("\nUpdated bug happiness values:")
        for row in self.grid:
            for room in row:
                if room.occupiedBy:
                    print(f"  {room.occupiedBy.species} in Room {room.roomNo} -> Happiness: {room.occupiedBy.happiness}")
        return True

    def recalc_all_happiness(self):
        for row in self.grid:
            for room in row:
                if room.occupiedBy:
                    bug = room.occupiedBy
                    bug.happiness = CalcHappiness(bug, room)

    def FinalAverage(self):
        total = 0
        count = 0
        for row in self.grid:
            for room in row:
                if room.occupiedBy:
                    total += room.occupiedBy.happiness
                    count += 1

        if count == 0:
            return 0
        return total / count

    def find_room_coords(self, room_num):
        for row_index, row in enumerate(self.grid):
            for col_index, room in enumerate(row):
                if room.roomNo == room_num:
                    return [row_index, col_index]


    def create_grid(self):
        roomNo = 0
        for row in range(self.rows):
            row_list = []
            for column in range(self.cols):
                if row == self.rows - 1:
                    environment = "UNDERGROUND"
                else:
                    environment = "OVERGROUND"

                if environment == "UNDERGROUND":
                    accessibility = -1
                else:
                    # Number of above-ground floors (excluding underground)
                    above_ground_floors = self.rows - 1

                    # Scale so that top floor = 0 and ground floor = 10
                    accessibility = round(10 * (row / (above_ground_floors - 1)))

                roomNo = roomNo + 1

                room = Room(size=10, environment=environment, accessibility=accessibility, cost=100, position=[row, column], roomNo=roomNo)
                row_list.append(room)
            self.grid.append(row_list)

    def print_grid(self):
        for row in self.grid:
            for room in row:
                env_symbol = "U" if room.environment == "UNDERGROUND" else "O"
                print(f"{env_symbol}:{room.accessibility:3d}", end="  ")
            print()

    def print_grid_numbers(self):
        for row in self.grid:
            for room in row:
                print(room.roomNo, end="  ")
            print()

    def print_room(self, room_number):
        # Find the room with the matching room number
        for row in self.grid:
            for room in row:
                if room.roomNo == room_number:
                    print(f"Room number {room.roomNo}:")
                    print(f"  Environment: {room.environment}")
                    print(f"  Accessibility: {room.accessibility}")
                    print(f"  Size: {room.size}")
                    print(f"  Cost: {room.cost}")
                    print(f"  Occupied: {room.occupiedBy}")
                    print(f"  Position: {room.position}")
                    return
        print("Invalid room number.")

"""
Hotel().print_grid()
Hotel().print_room(12)
Hotel().print_grid_numbers()
"""
