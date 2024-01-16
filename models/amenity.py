#!/usr/bin/python3
"""
    Implementation of the Amenity class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """
    Implementation for the Amenities.
    """

    __tablename__ = "amenities"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary="place_amenity", viewonly=False
        )
    else:
        name = ""

    if storage_type != "db":

        @property
        def place_amenities(self):
            """
            Getter attribute in case of file storage.
            """
            from models import storage
            from models.place import Place

            place_amenities = storage.all(Place)
            place_amenities_list = []
            for place in place_amenities.values():
                if place.amenity_ids == self.id:
                    place_amenities_list.append(place)
            return place_amenities_list
