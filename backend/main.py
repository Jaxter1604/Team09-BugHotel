from fastapi import FastAPI

app = FastAPI(title="Bug Hotel")

def root():
    return {"message": "bug hotel"}