from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from EC2!"}

@app.get("/square/{num}")
def square(num: int):
    return {"number": num, "square": num ** 2}
