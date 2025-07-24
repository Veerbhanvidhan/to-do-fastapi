from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles  # ✅ required for static files

app = FastAPI()

# ✅ This line tells FastAPI to serve files from the "static" folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI app!"}


