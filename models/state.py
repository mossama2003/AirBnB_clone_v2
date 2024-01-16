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
    name = Column(String(128), nullable=False)
    if storage_type == "db":
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete-orphan",
        )
    else:

        @property
        def cities(self):
            """
            Returns the list of City instances with state_id equals
            to the current State.id
            """
            cities = models.storage.all(City)
            list_cities = []
            for city in cities.values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
