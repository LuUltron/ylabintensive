from sqlalchemy.orm import Session

from models.core import Menu, Submenu, Dish

def get_dishes(submenu_id: str, db: Session) -> list[Dish]:
    return db.query(Dish).filter(Dish.submenu_id == submenu_id).all()

def get_dish(dish_id: str, db: Session) -> Dish:
    return db.query(Dish).filter(Dish.id == dish_id).first()

def create_dish(dish_id: str, submenu_id: str, db: Session, 
                title: str, description: str, price: int) -> Dish:
    submenu = db.query(Submenu).filter(Submenu.id == submenu_id).first()
    new_dish = Dish(
        id=dish_id,
        title=title,
        description=description,
        submenu_id=submenu.id,
        price=price
        )
    db.add(new_dish)
    submenu.dishes_count += 1
    menu = db.query(Menu).filter(Menu.id == submenu.menu_id).first()
    menu.dishes_count += 1
    db.commit()
    return new_dish

def update_dish(dish_id: str, db: Session, title: str, description: str, price: int) -> Dish:
    dish = db.query(Dish).filter(Dish.id == dish_id).first()
    dish.title = title
    dish.description = description
    dish.price = price
    db.commit()
    return dish

def delete_dish(dish_id: str, db: Session) -> bool:
    dish = db.query(Dish).filter(Dish.id == dish_id).first()
    submenu = db.query(Submenu).filter(Submenu.id == dish.submenu_id).first()
    submenu.dishes_count -= 1
    menu = db.query(Menu).filter(Menu.id == submenu.menu_id).first()
    menu.submenus_count -= 1
    menu.dishes_count -= 1
    db.delete(dish)
    db.commit()
    return True


def get_submenus(menu_id: str, db: Session):
    return db.query(Submenu).filter(Submenu.menu_id == menu_id).all()

def get_submenu(submenu_id: str, db: Session):
    return db.query(Submenu).filter(Submenu.id == submenu_id).first()

def create_submenu(submenu_id: str, menu_id: str, db: Session, title: str, description: str):
    menu = db.query(Menu).filter(Menu.id == menu_id).first()
    new_submenu = Submenu(
        id=submenu_id,
        title=title,
        description=description,
        menu_id=menu.id
        )
    db.add(new_submenu)
    menu.submenus_count += 1
    db.commit()
    return new_submenu

def update_submenu(submenu_id: str, db: Session, title: str, description: str):
    submenu = db.query(Submenu).filter(Submenu.id == submenu_id).first()
    submenu.title = title
    submenu.description = description
    db.commit()
    return submenu

def delete_submenu(submenu_id: str, db: Session):
    submenu = db.query(Submenu).filter(Submenu.id == submenu_id).first()
    for dish in submenu.dishes:
        delete_dish(dish.id, db)
    menu = db.query(Menu).filter(Menu.id == submenu.menu_id).first()
    menu.submenus_count -= 1
    menu.dishes_count -= submenu.dishes_count
    db.delete(submenu)
    db.commit()
    return True


def get_menus(db: Session):
    return db.query(Menu).all()

def get_menu(menu_id: str, db: Session):
    return db.query(Menu).filter(Menu.id == menu_id).first()

def create_menu(db: Session, title: str, description: str):
    new_menu = Menu(
        title=title,
        description=description
        )
    db.add(new_menu)
    db.commit()
    print('controllerHHHHHHHEEEEEEEEERRRRRRRRRTTTTTTTT', new_menu, new_menu.id, type(new_menu.id))
    return new_menu

def update_menu(menu_id: str, db: Session, title: str, description: str):
    menu = db.query(Menu).filter(Menu.id == menu_id).first()
    menu.title = title
    menu.description = description
    db.commit()
    return menu

def delete_menu(menu_id: str, db: Session):
    menu = db.query(Menu).filter(Menu.id == menu_id).first()
    for submenu in menu.submenus:
        delete_submenu(submenu.id, db)
    db.delete(menu)
    db.commit()
    return True