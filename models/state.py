#!/usr/bin/python3
"""
    Implementation of the State class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """
    Implementation for the State.
    """

    __tablename__ = "states"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """
            Getter attribute in case of file storage.
            """
            from models import storage

            cities = storage.all(City)
            cities_list = []
            for city in cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
