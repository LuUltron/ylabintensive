import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Menu(Base):
    __tablename__ = "menus"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True, nullable=False)
    title = Column(String, index=True)
    description = Column(String, index=True)
   
    submenus = relationship("Submenu", back_populates="menu")

    def __repr__(self) -> dict:
        return {
            "title": self.title,
            "description": self.description
        }

class Submenu(Base):
    __tablename__ = "submenus"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True, nullable=False)
    title = Column(String, index=True)
    description = Column(String, index=True)
    menu_id = Column(String, ForeignKey("menus.id"))
    dishes_count = Column(Integer, index=True, default=0)

    menu = relationship("Menu", back_populates="submenus")
    dishes = relationship("Dish", back_populates="submenu")

    def __repr__(self) -> dict:
        return {
            "title": self.title,
            "description": self.description
        }


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True, nullable=False)
    title = Column(String, index=True)
    description = Column(String, index=True)
    submenu_id = Column(String, ForeignKey("submenus.id"))
    price = Column(Integer, index=True)

    submenu = relationship("Submenu", back_populates="dishes")