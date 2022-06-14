# -*- coding: utf-8 -*-
"""
Description
"""

__version__ = '0.1'
__author__ = 'Utkarsh Srivastava'

import traceback
import logging
import uvicorn
from fastapi import FastAPI, Request, Body
from app.dtos.items import Item
import json

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# variables
@app.get("/")
async def sample_get():
    try:
        return "hi"
    except Exception as e:
        print(e)
        return "Exception occured in parsing response"

@app.post("/thanks")
async def read_item(item: Item):
    try:
        return item
    except Exception as e:
        print(e)
        return "Exception occured in parsing response"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port={{cookiecutter.project_server_port}})