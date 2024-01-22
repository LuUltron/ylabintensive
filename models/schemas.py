import uuid
from pydantic import BaseModel
from typing import List, Optional

class ItemBase(BaseModel):
    id: uuid.UUID
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Dish(ItemBase):
    price: int
    submenu_id: str

    class Config:
        orm_mode = True

class Submenu(ItemBase):
    dishes_count: int
    dishes: List[Dish] = []

    class Config:
        orm_mode = True

class Menu(ItemBase):
    submenus_count: int
    dishes_count: int
    submenus: List[Submenu] = []

    class Config:
        orm_mode = True