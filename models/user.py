#!/usr/bin/python3
"""This is the user class"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        places = []
        reviews = []

        @property
        def places(self):
            """Returns the list of Place instances with user_id equals
            to the current User.id"""
            from models import storage

            place_list = []
            for place in storage.all(Place).values():
                if place.user_id == self.id:
                    place_list.append(place)
            return place_list

        @property
        def reviews(self):
            """Returns the list of Review instances with user_id equals
            to the current User.id"""
            from models import storage

            review_list = []
            for review in storage.all(Review).values():
                if review.user_id == self.id:
                    review_list.append(review)
            return review_list
