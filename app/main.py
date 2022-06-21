import datetime
import os
from typing import Union

import boto3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health():
    return "ok"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/echo")
def echo(msg: str):
    s3 = boto3.resource("s3", region_name=os.environ["AWS_REGION"])
    bucket = s3.Bucket(os.environ["S3_BUCKET"])
    key = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    obj = bucket.Object(key)
    obj.put(Body=bytes(msg))

    return {
        "msg": msg,
        "key": key,
    }
