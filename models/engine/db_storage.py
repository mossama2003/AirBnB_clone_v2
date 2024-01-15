#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """create tables in environmental"""

    __engine = None
    __session = None

    def __init__(self):
        """creates engine"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, db),
            pool_pre_ping=True,
        )
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        else:
            Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            all_obj = self.__session.query(State).all()
            all_obj += self.__session.query(City).all()
            all_obj += self.__session.query(User).all()
            all_obj += self.__session.query(Place).all()
            all_obj += self.__session.query(Review).all()
            all_obj += self.__session.query(Amenity).all()
        else:
            all_obj = self.__session.query(cls).all()
        return {obj.id: obj for obj in all_obj}

    def new(self, obj):
        """add a new element in the table"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """save changes"""
        return self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """configuration"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """calls remove()"""
        self.__session.close()
