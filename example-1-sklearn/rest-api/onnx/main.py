import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from estimate import estimate_price
import time

class EstimationParams(BaseModel):
    param_1:    int


class EstimationOutput(BaseModel):
    param_1:    int
    price:      int

app = FastAPI()

@app.get('/echo')
async def echo():
    return {"msg": "Hello World"}

@app.post('/estimate', response_model=EstimationOutput)
def estimate(input: EstimationParams):
    input_values = input.dict()
    now = time.time()
    result = estimate_price(input_values)
    print('Inference runtime (ONNX): {} s '.format(time.time() - now))
    return result

# run from console with "uvicorn main:app --host 0.0.0.0 --port 8001 --reload"