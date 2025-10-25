from fastapi import FastAPI
from BugClass import *
from HotelClass import Hotel
from RoomClass import Room
from BugQueue import generate_queue

app = FastAPI(title="Bug Hotel")

def game():
    hotel = Hotel()
    bugs = generate_queue(35)

    hotel.print_grid_numbers()

    for bug in bugs:
        print(f"\nNext bug: {bug.species}")
        print(f"    Budget: {bug.budget}")
        print(f"    Prefers: {bug.prefferedEnvironment.name}")
        print(f"    Can fly?: {bug.canFly}")
        print(f"    Is Predator or Prey: {bug.preyOrPredator.name}")
        print(f"    Size: {bug.size}")

        while True:
            try:
                room_num = int(input("Enter a room number to assign this bug: "))
                room_coords = hotel.find_room_coords(room_num)
                if hotel.add_bug_to_room(bug, room_coords[0], room_coords[1]):
                    break
            except ValueError:
                print("Please enter a room number between 1 and 35, that is not occupied")

    final = hotel.FinalAverage()
    print(f"\n Your final score is {final}")
    

game()
