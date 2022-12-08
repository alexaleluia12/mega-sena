
from enum import Enum

from fastapi import FastAPI

import randon_generator as rg


class ModelNumbers(str, Enum):
    modelOne = "modelOne"
    modelTwo = "modelTwo"
    modelThree = "modelThree"

app = FastAPI()


@app.get("/numbers/{model}")
async def createNumber(model: ModelNumbers):
    mapNumbesGenerators = {
        "modelOne": rg.GeneratorPureRandom,
        "modelTwo": rg.GeneratorBFLow,
        "modelThree": rg.GeneratorAALow,
    }
    gen = mapNumbesGenerators[model.value]
    seq = rg.SequenceNumber()
    return seq.create(gen())
