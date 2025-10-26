from fastapi import FastAPI, Request
import asyncio
import json
from BugClass import *
from HotelClass import Hotel
from RoomClass import Room
from BugQueue import generate_queue

MAX_BUGS = 35

app = FastAPI(title="Bug Hotel")
app.state.room_num = None
app.state.input_event = asyncio.Event()

@app.post("/user_input")
async def get_room_num(request: Request):
    data = await request.json()
    room_num = app.state.room_num = data.get("room_num")
    app.state.input_event.set()
    return {"status": "received", "room_num": room_num}

@app.on_event("startup")
async def start_game():
    asyncio.create_task(game())
    

async def game():

    @app.get("/queue")
    def get_queue():    
        queue_list = []
        fn_current_bug = currentBug #don't want to screw over main loop's iteration
        queue_list.append(fn_current_bug.value.species)
        print(fn_current_bug)
        index = 0
        while (fn_current_bug != None and index <= MAX_BUGS):
            fn_current_bug = fn_current_bug.next
            queue_list.append(currentBug.value.species)
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
                print("getting input")
                await app.state.input_event.wait()
  
                room_num = app.state.room_num
                room_coords = hotel.find_room_coords(room_num)
                app.state.input_event.clear()
                if hotel.add_bug_to_room(currentBug.value, room_coords[0], room_coords[1]):
                    break
            except ValueError:
                print("Please enter a room number between 1 and 35, that is not occupied")
        currentBug=currentBug.next

    final = hotel.FinalAverage()
    print(f"\n Your final score is {final}")
    

game()
