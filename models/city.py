#!/usr/bin/python3
"""
    Define the class City.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """
    Define the class City that inherits from BaseModel.
    """

    __tablename__ = "cities"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        name = ""
        state_id = ""

        @property
        def places(self):
            """
            Getter attribute in case of file storage.
            """
            from models import storage
            from models.place import Place

            places = storage.all(Place)
            places_list = []
            for place in places.values():
                if place.city_id == self.id:
                    places_list.append(place)
            return places_list
