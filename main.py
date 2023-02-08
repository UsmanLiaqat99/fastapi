from fastapi import FastAPI # This is a class

app = FastAPI() # This is an instance of the class

@app.get("/") # This is a decorator
def index():
    return {"message": "Hello World"} # This is a dictionary