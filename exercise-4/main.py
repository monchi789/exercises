from fastapi import FastAPI


app = FastAPI()

@app.get("/api/weather/all")
def get_weathers():
    return {"Hello": "World"}