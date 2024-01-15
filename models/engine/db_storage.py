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
        """constructor"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(User).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(Review).all()
            objs += self.__session.query(Amenity).all()
        else:
            objs = self.__session.query(cls).all()
        return {obj.id: obj for obj in objs}

    def new(self, obj):
        """add a new element in the table"""
        if obj:
            self.__session.add(obj)
            self.__session.flush()
            self.__session.refresh(obj)

    def save(self):
        """save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """configuration"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """calls remove()"""
        self.__session.close()
