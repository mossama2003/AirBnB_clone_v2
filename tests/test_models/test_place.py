#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_to_dict(self):
        """ """
        new = self.value()
        new_dict = new.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue("to_dict" in dir(new))

    def test_str(self):
        """ """
        new = self.value()
        string = "[{}] ({}) {}".format(new.__class__.__name__, new.id, new.__dict__)
        self.assertEqual(string, str(new))

    def test_kwargs(self):
        """ """
        new = self.value()
        json_dict = new.to_dict()
        new2 = self.value(**json_dict)
        self.assertFalse(new is new2)
        self.assertEqual(new.id, new2.id)
        self.assertEqual(new.created_at, new2.created_at)
        self.assertEqual(new.updated_at, new2.updated_at)
