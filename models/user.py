#!/usr/bin/python3
"""
    Implementation of the User class which inherits from BaseModel
"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """
    Definition of the User class
    """

    __tablename__ = "users"
    email = Column(
        String(128),
        nullable=False,
    )
    password = Column(
        String(128),
        nullable=False,
    )
    first_name = Column(
        String(128),
        nullable=True,
    )
    last_name = Column(
        String(128),
        nullable=True,
    )
    if storage_type == "db":
        places = relationship(
            "Place",
            backref="user",
            cascade="all, delete-orphan",
        )
        reviews = relationship(
            "Review",
            backref="user",
            cascade="all, delete-orphan",
        )
    else:

        @property
        def places(self):
            """
            Returns the list of Place instances with user_id equals
            to the current User.id
            """
            places = models.storage.all(Place)
            list_places = []
            for place in places.values():
                if place.user_id == self.id:
                    list_places.append(place)
            return list_places

        @property
        def reviews(self):
            """
            Returns the list of Review instances with user_id equals
            to the current User.id
            """
            reviews = models.storage.all(Review)
            list_reviews = []
            for review in reviews.values():
                if review.user_id == self.id:
                    list_reviews.append(review)
            return list_reviews
