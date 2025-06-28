from fastapi import FastAPI

app = FastAPI()

# entrypoint
@app.get("/")
def main():
    return "Nothing to see here"