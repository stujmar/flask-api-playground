from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"user": "smarsh"}

@app.post("/login")
def login():
    return {"user": "smarsh"}

