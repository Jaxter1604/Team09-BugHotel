from fastapi import FastAPI
from BugClass import *
from HotelClass import Hotel
from RoomClass import Room
from BugQueue import generate_queue

MAX_BUGS = 35

app = FastAPI(title="Bug Hotel")

def game():
    
    @app("/queue")
    def get_queue():    
        queue_list = []
        fn_current_bug = currentBug #don't want to screw over main loop's iteration
        queue_list.append(fn_current_bug)
        index = 0
        while (fn_current_bug := fn_current_bug.next and i <= MAX_BUGS):
            queue_list.append(currentBug.species)
        return {"queue" : queue_list}

    hotel = Hotel()
    bugs = generate_queue(MAX_BUGS)

    hotel.print_grid_numbers()

    currentBug=bugs.head
    while currentBug:
        print(f"\nNext bug: {currentBug.value.species}")
        print(f"    Budget: {currentBug.value.budget}")
        print(f"    Prefers: {currentBug.value.prefferedEnvironment.name}")
        print(f"    Can fly?: {currentBug.value.canFly}")
        print(f"    Is Predator or Prey: {currentBug.value.preyOrPredator.name}")
        print(f"    Size: {currentBug.value.size}")

        while True:
            try:
                room_num = int(input("Enter a room number to assign this bug: "))
                room_coords = hotel.find_room_coords(room_num)
                if hotel.add_bug_to_room(currentBug.value, room_coords[0], room_coords[1]):
                    break
            except ValueError:
                print("Please enter a room number between 1 and 35, that is not occupied")
        currentBug=currentBug.next

    final = hotel.FinalAverage()
    print(f"\n Your final score is {final}")
    

game()
