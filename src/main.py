from fastapi import FastAPI
from src.routers import message_router

app = FastAPI()

# entrypoint
@app.get("/")
def main():
    return "nothing to see here"

# routers
app.include_router(message_router.router)