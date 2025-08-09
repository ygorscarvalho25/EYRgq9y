from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Version": "0.0-0"}
