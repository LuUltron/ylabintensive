from fastapi import FastAPI
from models import core
from models.database import engine
from routers.menus import router as menus_router
from routers.submenus import router as submenus_router
from routers.dishes import router as submenus_router

core.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    router=menus_router,
    prefix="/api/v1/menus"
)

app.include_router(
    router=submenus_router,
    prefix="/api/v1/menus/{menu_id}/submenus"

)

app.include_router(
    router=submenus_router,
    prefix="/api/v1/menus/{menu_id}/submenus/{submenu_id}"
)

