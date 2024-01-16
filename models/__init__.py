#!/usr/bin/python3
"""
    Package initializer
"""
from os import getenv

from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()

classes = {
    "State": State,
    "City": City,
    "User": User,
    "Review": Review,
    "BaseModel": BaseModel,
    "Amenity": Amenity,
    "Place": Place,
}
