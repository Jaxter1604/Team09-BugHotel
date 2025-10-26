from fastapi import FastAPI, Request
import asyncio
import json
from BugClass import *
from HotelClass import Hotel
from RoomClass import Room
from BugQueue import generate_queue
from fastapi.middleware.cors import CORSMiddleware

MAX_BUGS = 35

app = FastAPI(title="Bug Hotel")
app.state.room_num = None
app.state.input_event = asyncio.Event()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



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
        while (fn_current_bug != None):
            queue_list.append({
                "species" : fn_current_bug.value.species,
                "budget" : fn_current_bug.value.budget,
                "canFly" : fn_current_bug.value.canFly,
                "preyOrPredator" : fn_current_bug.value.preyOrPredator,
                "prefferedEnvironment" : fn_current_bug.value.prefferedEnvironment,
                "agression" : fn_current_bug.value.prefferedEnvironment,
                "size" : fn_current_bug.value.size
                })
            fn_current_bug = fn_current_bug.next

        return {"queue" : queue_list}

    @app.get("/hotel")
    def get_hotel_data():
        room_info = []
        for room_no in range(1, hotel.max_room_num+1):
            room_row, room_col = hotel.find_room_coords(room_no)
            currentRoom = hotel.grid[room_row][room_col]
            room_info.append({
                "size" : currentRoom.size,
                "environment" : currentRoom.environment,
                "accessibility" : currentRoom.accessibility,
                "occupiedBy" : currentRoom.occupiedBy,
                "cost" : currentRoom.cost,
                "roomNo" : currentRoom.roomNo
            })
        return {"room_info" : room_info}

    @app.get("/score")
    def get_score():
        return {"score": hotel.FinalAverage()}

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
