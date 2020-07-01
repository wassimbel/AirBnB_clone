#!/usr/bin/python3
""" Place Class Unittest """
import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    """ Place class testing """

    def test_place(self):
        """ test """
        a = Place()
        self.assertTrue(hasattr(a, "name"))
        self.assertTrue(hasattr(a, "city_id"))
        self.assertTrue(hasattr(a, "user_id"))
        self.assertTrue(hasattr(a, "description"))
        self.assertTrue(hasattr(a, "number_rooms"))
        self.assertTrue(hasattr(a, "number_bathrooms"))
        self.assertTrue(hasattr(a, "max_guest"))
        self.assertTrue(hasattr(a, "price_by_night"))
        self.assertTrue(hasattr(a, "latitude"))
        self.assertTrue(hasattr(a, "amenity_ids"))
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertIsInstance(a.name, str)
        self.assertIsInstance(a.description, str)
        self.assertIsInstance(a.city_id, str)
        self.assertIsInstance(a.user_id, str)
        self.assertIsInstance(a.number_rooms, int)
        self.assertIsInstance(a.number_bathrooms, int)
        self.assertIsInstance(a.max_guest, int)
        self.assertIsInstance(a.price_by_night, int)
        self.assertIsInstance(a.latitude, float)
        self.assertIsInstance(a.longitude, float)
        self.assertIsInstance(a.amenity_ids, list)
        self.assertTrue(issubclass(Place, models.base_model.BaseModel))


if __name__ == '__main__':
    unittest.main()
