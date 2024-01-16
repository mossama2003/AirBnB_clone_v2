#!/usr/bin/python3
"""create class DBStorage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


database = getenv("HBNB_MYSQL_DB")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
password = getenv("HBNB_MYSQL_PWD")
hbnb_env = getenv("HBNB_ENV")

classes = {
    "State": State,
    "City": City,
    "User": User,
    "Place": Place,
    "Review": Review,
    "Amenity": Amenity,
}


class DBStorage:
    """class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """init method"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                user,
                password,
                host,
                database,
            ),
            pool_pre_ping=True,
        )
        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all method"""
        new_dict = {}
        if cls is None:
            for key, value in classes.items():
                if key != "BaseModel":
                    for row in self.__session.query(value):
                        key = row.__class__.__name__ + "." + row.id
                        new_dict[key] = row
        else:
            for row in self.__session.query(classes[cls]):
                key = row.__class__.__name__ + "." + row.id
                new_dict[key] = row
        return new_dict

    def new(self, obj):
        """new method"""
        self.__session.add(obj)

    def save(self):
        """save method"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete method"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload method"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False,
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close method"""
        self.__session.close()
