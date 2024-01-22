from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from models import schemas
from controllers import items
from models.database import get_db


router = APIRouter()

@router.get("/dishes", response_model=List[schemas.Dish])
def read_dishes(submenu_id: str, db: Session = Depends(get_db)):
    dishes = items.get_dishes(submenu_id, db)
    return dishes

@router.get("/dishes/{dish_id}", response_model=schemas.Dish)
def read_dish(dish_id: str, db: Session = Depends(get_db)):
    dish = items.get_dish(dish_id, db)
    return dish

@router.post("/", response_model=schemas.Dish)
def post_dish(submenu_id: str, db: Session = Depends(get_db)):
    title = "new title"
    description = "new descr"
    price = 100
    dish = items.create_dish(submenu_id, db, title, description, price)
    return dish

@router.patch("/dishes/{dish_id}", response_model=schemas.Dish)
def patch_dish(dish_id: str, db: Session = Depends(get_db)):
    title = "upd title"
    description = "upd descr"
    price = 123
    dish = items.update_dish(dish_id, db, title, description, price)
    return dish

@router.delete("/dishes/{dish_id}", response_model=schemas.Dish)
def del_dish(dish_id: str, db: Session = Depends(get_db)):
    dish = items.delete_dish(dish_id, db)
    return {
        "status":dish,
        "message":"The dish has been deleted"
        }
