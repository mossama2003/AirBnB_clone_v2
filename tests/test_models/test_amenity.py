#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
from time import sleep
from os import getenv
import pycodestyle
import inspect
import os
import unittest

storage_t = getenv("HBNB_TYPE_STORAGE")


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_name3(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(new.name, "")

    def test_to_dict(self):
        """ """
        new = self.value()
        new_dict = new.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue("to_dict" in dir(new))

    def test_str(self):
        """ """
        new = self.value()
        string = "[{}] ({}) {}".format(
            new.__class__.__name__,
            new.id,
            new.__dict__,
        )
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


class Test_PEP8(unittest.TestCase):
    """test User"""

    def test_pep8_user(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/amenity.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )


class test_inherit_basemodel(unittest.TestCase):
    """Test if user inherit from BaseModel"""

    def test_instance(self):
        """check if user is an instance of BaseModel"""
        user = Amenity()
        self.assertIsInstance(user, Amenity)
        self.assertTrue(issubclass(type(user), BaseModel))
        self.assertEqual(str(type(user)), "<class 'models.amenity.Amenity'>")

    def test_permissions(self):
        """Test the permissions of the file"""
        read = os.access("models/amenity.py", os.R_OK)
        self.assertTrue(read)
        write = os.access("models/amenity.py", os.W_OK)
        self.assertTrue(write)
        exe = os.access("models/amenity.py", os.X_OK)
        self.assertTrue(exe)

    def test_correct_module_doc(self):
        """Test if there is a module doc"""
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_correct_class_doc(self):
        """Test if there is a class doc"""
        self.assertTrue(len(Amenity.__doc__) >= 1)


class test_Amenity_BaseModel(unittest.TestCase):
    """Testing user class"""

    def test_instances(self):
        with patch("models.amenity"):
            instance = Amenity()
            self.assertEqual(type(instance), Amenity)
            instance.name = "Barbie"
            expectec_attrs_types = {
                "id": str,
                "created_at": datetime,
                "updated_at": datetime,
                "name": str,
            }
            inst_dict = instance.to_dict()
            expected_dict_attrs = [
                "id",
                "created_at",
                "updated_at",
                "name",
                "__class__",
            ]
            self.assertCountEqual(inst_dict.keys(), expected_dict_attrs)
            self.assertEqual(inst_dict["name"], "Barbie")
            self.assertEqual(inst_dict["__class__"], "Amenity")

            for attr, types in expectec_attrs_types.items():
                with self.subTest(attr=attr, typ=types):
                    self.assertIn(attr, instance.__dict__)
                    self.assertIs(type(instance.__dict__[attr]), types)
            self.assertEqual(instance.name, "Barbie")

    def test_user_id_and_createat(self):
        """testing id for every user"""
        user_1 = Amenity()
        sleep(2)
        user_2 = Amenity()
        sleep(2)
        user_3 = Amenity()
        sleep(2)
        list_users = [user_1, user_2, user_3]
        for instance in list_users:
            user_id = instance.id
            with self.subTest(user_id=user_id):
                self.assertIs(type(user_id), str)
        self.assertNotEqual(user_1.id, user_2.id)
        self.assertNotEqual(user_1.id, user_3.id)
        self.assertNotEqual(user_2.id, user_3.id)
        self.assertTrue(user_1.created_at <= user_2.created_at)
        self.assertTrue(user_2.created_at <= user_3.created_at)
        self.assertNotEqual(user_1.created_at, user_2.created_at)
        self.assertNotEqual(user_1.created_at, user_3.created_at)
        self.assertNotEqual(user_3.created_at, user_2.created_at)

    def test_str_method(self):
        """
        Testin str magic method
        """
        inst = Amenity()
        str_output = "[Amenity] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(str_output, str(inst))

    @patch("models.storage")
    def test_save_method(self, mock_storage):
        """Testing save method and if it update"""
        instance5 = Amenity()
        created_at = instance5.created_at
        sleep(2)
        updated_at = instance5.updated_at
        instance5.save()
        new_created_at = instance5.created_at
        sleep(2)
        new_updated_at = instance5.updated_at
        self.assertNotEqual(updated_at, new_updated_at)
        self.assertEqual(created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)

    def test_to_dict_method(self):
        """Testing to_dict method"""
        instance6 = Amenity()
        dict_returned = instance6.to_dict()
        self.assertEqual(type(dict_returned), dict)
        self.assertEqual(dict_returned["__class__"], "Amenity")
        self.assertEqual(type(dict_returned["created_at"]), str)
        self.assertEqual(type(dict_returned["updated_at"]), str)

    def test_kwargs(self):
        """Testing kwargs"""
        instance7 = Amenity()
        instance7.name = "Holberton"
        instance7.my_number = 89
        instance7.save()
        dict_rep = instance7.to_dict()
        instance8 = Amenity(**dict_rep)
        self.assertEqual(instance8.to_dict(), instance7.to_dict())
        self.assertFalse(instance8 is instance7)

    def test_permissions(self):
        """Test the permissions of the file"""
        read = os.access("models/amenity.py", os.R_OK)
        self.assertTrue(read)
        write = os.access("models/amenity.py", os.W_OK)
        self.assertTrue(write)
        exe = os.access("models/amenity.py", os.X_OK)
        self.assertTrue(exe)

    def test_correct_module_doc(self):
        """Test if there is a module doc"""
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_correct_class_doc(self):
        """Test if there is a class doc"""
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_init_doc(self):
        """Test if init method is documented"""
        self.assertTrue(len(Amenity.__init__.__doc__) >= 1)

    def test_str_doc(self):
        """Test if str method is documented"""
        self.assertTrue(len(Amenity.__str__.__doc__) >= 1)

    def test_save_doc(self):
        """Test if save method is documented"""
        self.assertTrue(len(Amenity.save.__doc__) >= 1)

    def test_to_dict_doc(self):
        """Test if to_dict method is documented"""
        self.assertTrue(len(Amenity.to_dict.__doc__) >= 1)

    def test_has_methods(self):
        """Test if instance of BaseModel has the methods"""
        self.assertTrue(inspect.ismethod(Amenity.__init__))
        self.assertTrue(inspect.ismethod(Amenity.__str__))
        self.assertTrue(inspect.ismethod(Amenity.save))
        self.assertTrue(inspect.ismethod(Amenity.to_dict))

    def test_has_class_attrs(self):
        """Test if instance of BaseModel has the methods"""
        self.assertTrue(hasattr(Amenity, "__init__"))
        self.assertTrue(hasattr(Amenity, "__str__"))
        self.assertTrue(hasattr(Amenity, "save"))
        self.assertTrue(hasattr(Amenity, "to_dict"))

    def test_inheritance(self):
        """Test if Amenity class inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_is_instance(self):
        """Test if my_model is an instance of BaseModel"""
        my_model = Amenity()
        self.assertIsInstance(my_model, BaseModel)

    def test_attribute_types(self):
        """Test if instance of BaseModel has attributes"""
        my_model = Amenity()
        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_attributes(self):
        """Test if instance of BaseModel has attributes"""
        my_model = Amenity()
        self.assertTrue(hasattr(my_model, "__class__"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_unique_id(self):
        """Test if the id of two instances are different"""
        my_model = Amenity()
        my_model_2 = Amenity()
        self.assertNotEqual(my_model.id, my_model_2.id)

    def test_save(self):
        """Test if the attribute updated_at (date) is updated for
        the same object with the current date"""
        my_model = Amenity()
        first_updated = my_model.updated_at
        sleep(0.5)
        my_model.save()
        second_updated = my_model.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        """Test if to_dict method returns a dictionary with the proper
        attributes"""
        my_model = Amenity()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        self.assertEqual(d["__class__"], "Amenity")
        self.assertEqual(type(d["created_at"]), str)
        self.assertEqual(type(d["updated_at"]), str)
        self.assertEqual(d["name"], "Holberton")
        self.assertEqual(d["my_number"], 89)

    def test_to_dict_noargs(self):
        """Test if to_dict method has no arguments"""
        my_model = Amenity()
        with self.assertRaises(TypeError):
            my_model.to_dict(1)

    def test_to_dict_excess_args(self):
        """Test if to_dict method has excess arguments"""
        my_model = Amenity()
        with self.assertRaises(TypeError):
            my_model.to_dict(1, 2)


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attribute name, and it's as an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if storage_t == "db":
            self.assertEqual(amenity.name, None)
        else:
            self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        am = Amenity()
        print(am.__dict__)
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in am.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
