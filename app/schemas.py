# schemas.py
from pydantic import BaseModel
from typing import Union

class ItemBase(BaseModel):
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True
