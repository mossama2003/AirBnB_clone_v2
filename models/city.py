#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import os
from models.amenity import Amenity


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="cities", cascade="delete")
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False,
            backref="cities",
            cascade="delete",
        )
    else:

        @property
        def reviews(self):
            """getter attribute for list of review instances"""
            from models import storage

            review_list = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.city_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """getter attribute for list of amenity instances"""
            from models import storage

            amenity_list = []
            all_amenities = storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.city_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list
