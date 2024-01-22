from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from models import schemas
from controllers import items
from models.database import get_db


router = APIRouter()

@router.get("/submenus/", response_model=List[schemas.Submenu])
def read_submenus(db: Session = Depends(get_db)):
    submenus = items.get_submenus(db)
    return submenus

@router.get("/submenus/{submenu_id}", response_model=schemas.Submenu)
def read_submenu(submenu_id: str, db: Session = Depends(get_db)):
    submenu = items.get_submenu(submenu_id, db)
    return submenu

@router.post("/", response_model=schemas.Submenu)
def post_submenu(menu_id: str, db: Session = Depends(get_db)):
    title = "new submenu title"
    description = "new submenu descr"
    submenu = items.create_submenu(menu_id, db, title, description)
    return submenu

@router.patch("/submenus/{submenu_id}", response_model=schemas.Submenu)
def patch_submenu(submenu_id: str, db: Session = Depends(get_db)):
    title = "upd submenu title"
    description = "upd submenu descr"
    submenu = items.update_submenu(submenu_id, db, title, description)
    return submenu

@router.delete("/submenus/{submenu_id}", response_model=schemas.Submenu)
def del_submenu(submenu_id: str, db: Session = Depends(get_db)):
    submenu = items.delete_submenu(submenu_id, db)
    return {
        "status":submenu,
        "message":"The subsubmenu has been deleted"
        }