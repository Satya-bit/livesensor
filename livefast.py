from fastapi import FastAPI

app = FastAPI()

# @app.get("/hello")
# async def hello():
#     return {"message": "hello world"}

@app.get("/hello/{name}")
async def hello(name):
    return f"This is my python class {name}" 