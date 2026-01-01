from fastapi import FastAPI
from pydantic import BaseModel
from utils import forecast

class RequestBody(BaseModel):
    n_days: int
    last_values: list   # last 3 days of sales

app = FastAPI(title="Demand Forecasting API")

@app.post("/forecast")
def get_forecast(data: RequestBody):
    result = forecast(data.n_days, data.last_values)
    return {"forecast": result}
