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

        place_list = []
        for place in storage.all(Place).values():
            if place.user_id == self.id:
                place_list.append(place)
        return place_list

    @property
    def reviews(self):
        """
        Getter attribute in case of file storage.
        """
        from models import storage
        from models.review import Review

        review_list = []
        for review in storage.all(Review).values():
            if review.user_id == self.id:
                review_list.append(review)
        return review_list
