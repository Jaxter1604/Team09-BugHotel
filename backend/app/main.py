from fastapi import FastAPI, Request
import asyncio
import json
from BugClass import *
from HotelClass import Hotel
from RoomClass import Room
from BugQueue import generate_queue
from fastapi.middleware.cors import CORSMiddleware
import threading

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



async def get_room_num():
    room_num = input("Enter room number:\n")
    return room_num

bugs = generate_queue(MAX_BUGS)
currentBug = bugs.head

@app.get("/queue")
def get_queue():    
    queue_list = []
    global currentBug #don't want to screw over main loop's iteration
    fn_current_bug = currentBug 
    while (fn_current_bug != None):
        queue_list.append({
            "species" : fn_current_bug.value.species,
            "budget" : fn_current_bug.value.budget,
            "canFly" : fn_current_bug.value.canFly,
            "preyOrPredator" : fn_current_bug.value.preyOrPredator,
            "prefferedEnvironment" : fn_current_bug.value.prefferedEnvironment,
            "agression" : fn_current_bug.value.aggression,
            "size" : fn_current_bug.value.size,
            "roomNo" : fn_current_bug.value.roomNo
            })
        fn_current_bug = fn_current_bug.next

    return {"queue" : queue_list}

def get_console_input():
    return input("Enter room number \n")

@app.on_event("startup")
async def start_game():
    thread = threading.Thread(target=game, daemon=True)
    thread.start()
    

def game():

    hotel = Hotel()

    hotel.print_grid_numbers()

    global currentBug 
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

                room_num = get_console_input()

                room_coords = hotel.find_room_coords(int(room_num))

                if hotel.add_bug_to_room(currentBug.value, room_coords[0], room_coords[1]):
                    currentBug.roomNo = room_num
                    break
            except ValueError:
                print("Please enter a room number between 1 and 35, that is not occupied")
        currentBug=currentBug.next

    final = hotel.FinalAverage()
    print(f"\n Your final score is {final}")
    