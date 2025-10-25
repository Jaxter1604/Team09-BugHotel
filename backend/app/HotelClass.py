from RoomClass import Room

class Hotel:
    def __init__(self, rows=6, cols=5):
        self.rows = rows
        self.cols = cols
        self.grid = []
        self.create_grid()

    def create_grid(self):
        for row in range(self.rows):
            row_list = []
            for column in range(self.cols):
                if row == self.rows - 1:
                    environment = "UNDERGROUND"
                else:
                    environment = "OVERGROUND"

                edge_distance = min(row, column, self.rows - 1 - row, self.cols - 1 - column)
                max_edge_distance = (min(self.rows, self.cols) // 2)
                if max_edge_distance == 0:
                    accessibility = 10
                elif environment == "UNDERGROUND":
                    accessibility = 0
                else:
                    accessibility = round(10 * (1 - edge_distance / max_edge_distance))

                room = Room(size=10, environment=environment, accessibility=accessibility, occupied=[], cost=100, position=[row, column])
                row_list.append(room)
            self.grid.append(row_list)

    def print_grid(self):
        for row in self.grid:
            for room in row:
                env_symbol = "U" if room.environment == "UNDERGROUND" else "O"
                print(f"{env_symbol}:{room.accessibility:3d}", end="  ")
            print()

Hotel().print_grid()