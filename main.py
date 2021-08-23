from fastapi import FastAPI
from starlette.responses import RedirectResponse
from data import Data

app = FastAPI()

@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse("/docs")

@app.get("/name")
def name():
    data = Data.name()
    return {'data' : data}

@app.get("/member_info")
def member():
    data = Data.member()
    return {'data' : data}
