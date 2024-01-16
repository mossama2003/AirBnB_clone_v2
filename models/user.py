#!/usr/bin/python3
"""
    Implementation of the User class which inherits from BaseModel
"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """
    Definition of the User class
    """

    __tablename__ = "users"
    if storage_type == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user", cascade="all, delete")
        reviews = relationship("Review", backref="user", cascade="all, delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

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
                if place.user_id == self.id:
                    places_list.append(place)
            return places_list

        @property
        def reviews(self):
            """
            Getter attribute in case of file storage.
            """
            from models import storage
            from models.review import Review

            reviews = storage.all(Review)
            reviews_list = []
            for review in reviews.values():
                if review.user_id == self.id:
                    reviews_list.append(review)
            return reviews_list
