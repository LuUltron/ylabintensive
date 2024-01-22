import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from models import schemas
from controllers import items
from models.database import get_db


router = APIRouter()

@router.get("/", response_model=List[schemas.Menu])
def read_menus(db: Session = Depends(get_db)):
    menus = items.get_menus(db)
    return menus

@router.get("/{menu_id}", response_model=schemas.Menu)
def read_menu(menu_id: uuid.UUID, db: Session = Depends(get_db)):
    menu = items.get_menu(menu_id, db)
    return {
        "title": menu.title,
        "description": menu.description
        }

@router.post("/", response_model=schemas.Menu)
def post_menu(db: Session = Depends(get_db)):
    title = "new menu title"
    description = "new menu descr"
    menu = items.create_menu(db, title, description)
    print('HHHHHHHEEEEEEEEERRRRRRRRRTTTTTTTT', menu)
    return menu

@router.patch("/{menu_id}", response_model=schemas.Menu)
def patch_menu(menu_id: uuid.UUID, db: Session = Depends(get_db)):
    title = "upd menu title"
    description = "upd menu descr"
    menu = items.update_menu(menu_id, db, title, description)
    return menu

@router.delete("/{menu_id}", response_model=schemas.Menu)
def del_menu(menu_id: uuid.UUID, db: Session = Depends(get_db)):
    menu = items.delete_menu(menu_id, db)
    return {
        "status":menu,
        "message":"The menu has been deleted"
        }
