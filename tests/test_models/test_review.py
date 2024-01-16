#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

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
