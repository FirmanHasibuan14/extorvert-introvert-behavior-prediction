from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=['Root'])
def read_root():
    return {"Message": "Welcome to the Personality API. Go to /docs for documentation."}