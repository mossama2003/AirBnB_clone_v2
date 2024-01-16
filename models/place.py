#!/usr/bin/python3
"""
    Define the class Place.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            nullable=False,
        ),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            nullable=False,
        ),
    )


class Place(BaseModel, Base):
    """
    Define the class Place that inherits from BaseModel.
    """

    __tablename__ = "places"
    if storage_type == "db":
        city_id = Column(
            String(60),
            ForeignKey("cities.id"),
            nullable=False,
        )
        user_id = Column(
            String(60),
            ForeignKey("users.id"),
            nullable=False,
        )
        name = Column(
            String(128),
            nullable=False,
        )
        description = Column(
            String(1024),
            nullable=True,
        )
        number_rooms = Column(
            Integer,
            default=0,
            nullable=False,
        )
        number_bathrooms = Column(
            Integer,
            default=0,
            nullable=False,
        )
        max_guest = Column(
            Integer,
            default=0,
            nullable=False,
        )
        price_by_night = Column(
            Integer,
            default=0,
            nullable=False,
        )
        latitude = Column(
            Float,
            nullable=True,
        )
        longitude = Column(
            Float,
            nullable=True,
        )
        amenity_ids = []
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete",
        )
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False,
            back_populates="place_amenities",
        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

    if storage_type != "db":

        @property
        def reviews(self):
            """
            Getter attribute in case of file storage.
            """
            from models import storage
            from models.review import Review

            review_list = []
            for key, value in storage.all(Review).items():
                if value.place_id == self.id:
                    review_list.append(value)
            return review_list

        @property
        def amenities(self):
            """
            Getter attribute in case of file storage.
            """
            from models import storage
            from models.amenity import Amenity

            amenity_list = []
            for key, value in storage.all(Amenity).items():
                if value.id in self.amenity_ids:
                    amenity_list.append(value)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """
            Setter attribute in case of file storage.
            """
            from models.amenity import Amenity

            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
