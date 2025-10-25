from fastapi import FastAPI
from routers import bugs, rooms

app = FastAPI(title="Bug Hotel")

app.include_router(bugs.router)
app.include_router(rooms.router)

def root():
    return {"message": "bug hotel"}