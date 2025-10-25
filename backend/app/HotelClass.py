from RoomClass import Room

class Hotel:
    def __init__(self, rows=7, cols=5):
        self.rows = rows
        self.cols = cols
        self.grid = []
        self.create_grid()

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

                room = Room(size=10, environment=environment, accessibility=accessibility, occupied=[], cost=100, position=[row, column], roomNo=roomNo)
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

    def print_room(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            room = self.grid[row][col]
            print(f"Room at ({row}, {col}):")
            print(f"  Environment: {room.environment}")
            print(f"  Accessibility: {room.accessibility}")
            print(f"  Size: {room.size}")
            print(f"  Cost: {room.cost}")
            print(f"  Occupied: {room.occupied}")
            print(f"  Room number: {room.roomNo}")
        else:
            print("Invalid room coordinates.")

Hotel().print_grid()
Hotel().print_room(1,2)
Hotel().print_grid_numbers()
