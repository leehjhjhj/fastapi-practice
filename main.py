from fastapi import FastAPI
from enum import Enum
from typing import Union

app = FastAPI()

#Enum example
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/")
async def root(page: int = 1, q: Union[str, None] = None, needy = str):
    '''
    Union: Union은 여러 가능한 타입 중 하나를 나타내기 위한 타입 힌트입니다.
    여기서는 str 또는 None 타입이 될 수 있음을 나타냅니다.
    {
        "message": "Hello World",
        "page": 1,
        "needy": "안녕",
        "q": "23"
    }
    여기서 needy는 필수 쿼리 파라미터이다. q는 None 설정을 해놨음으로 필수가 아니다.
    '''
    res = {"message": "Hello World", "page": page, "needy": needy}

    if q:
        res.update({"q": q}) #update로 딕셔너리에 추가
    return res
#매개변수
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

#선언형 매개변수
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
