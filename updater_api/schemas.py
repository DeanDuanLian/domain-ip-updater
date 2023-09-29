from typing import Any, Optional
from pydantic import BaseModel, constr

# class Model(BaseModel):
#     __root__: Any

class UpdateInfo(BaseModel):
    username:str
    password:str