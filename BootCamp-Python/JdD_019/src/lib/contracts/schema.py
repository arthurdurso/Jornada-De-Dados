from pydantic import BaseModel, PositiveFloat
from typing import Union

class ItemBase(BaseModel):
    name: str
    price: PositiveFloat
    is_offer: Union[bool, None] = None

class ItemCreate(ItemBase):
    pass

class ItemSchema(ItemBase):
    id: int