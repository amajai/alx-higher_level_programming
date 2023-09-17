import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id_assignment(self):
        """
        Test that the 'id' attribute is assigned correctly.
        """
        obj1 = Base()
        obj2 = Base()
        obj3 = Base(10)
        obj4 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 10)
        self.assertEqual(obj4.id, 3)

    def test_id_uniqueness(self):
        """
        Test that 'id' values are unique.
        """
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()

        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj2.id, obj3.id)
        self.assertNotEqual(obj1.id, obj3.id)

    def setUp(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Base.csv"):
            os.remove("Base.csv")

    def test_to_json_string(self):
        """
        Test that the Base method 'to_json_string' works correctly at
        converting object to string.
        """
        obj1 = Square(5, 0, 0, 1)
        obj2 = Square(2, 0, 1, 2)

        json_str = Base.to_json_string([obj1.to_dictionary(), obj2.to_dictionary()])
        obj1_str = '{"id": 1, "x": 0, "size": 5, "y": 0}'
        obj2_str = '{"id": 2, "x": 0, "size": 2, "y": 1}'
        expected_json_str = f'[{obj1_str}, {obj2_str}]'
        self.assertEqual(json_str, expected_json_str)

    def test_from_json_string(self):
        """
        Test that the Base method 'from_json_string' works correctly at
        converting string to object.
        """
        json_str = '[{"id": 1}, {"id": 2}]'
        obj_list = Base.from_json_string(json_str)
        self.assertEqual(len(obj_list), 2)
        self.assertEqual(obj_list[0]["id"], 1)
        self.assertEqual(obj_list[1]["id"], 2)

    def test_save_to_file(self):
        """
        Test that the dictionary from an instance is saved to a file.
        """
        obj1 = Square(5, 0, 0, 1)
        obj2 = Square(2, 0, 1, 2)

        Base.save_to_file([obj1, obj2])

        self.assertTrue(os.path.exists("Base.json"))

        with open("Base.json", "r") as file:
            json_str = file.read()
            obj1_str = '{"id": 1, "x": 0, "size": 5, "y": 0}'
            obj2_str = '{"id": 2, "x": 0, "size": 2, "y": 1}'
            expected_json_str = f'[{obj1_str}, {obj2_str}]'
            self.assertEqual(json_str, expected_json_str)

    def test_load_from_file(self):
        """
        Test that a dictionary is loaded from a file.
        """
        obj1 = Square(5, 0, 0, 1)
        obj2 = Square(2, 0, 1, 2)

        Square.save_to_file([obj1, obj2])
        self.assertTrue(os.path.exists("Square.json"))
        loaded_objs = Square.load_from_file()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].to_dictionary()["id"], 1)
        self.assertEqual(loaded_objs[0].to_dictionary()["size"], 5)
        self.assertEqual(loaded_objs[0].to_dictionary()["x"], 0)
        self.assertEqual(loaded_objs[0].to_dictionary()["y"], 0)

        self.assertEqual(loaded_objs[1].to_dictionary()["id"], 2)
        self.assertEqual(loaded_objs[1].to_dictionary()["size"], 2)
        self.assertEqual(loaded_objs[1].to_dictionary()["x"], 0)
        self.assertEqual(loaded_objs[1].to_dictionary()["y"], 1)

        obj3 = Rectangle(5, 12, 0, 0, 1)
        obj4 = Rectangle(2, 6, 0, 1, 2)

        Rectangle.save_to_file([obj3, obj4])
        self.assertTrue(os.path.exists("Rectangle.json"))
        loaded_objs = Rectangle.load_from_file()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].to_dictionary()["id"], 1)
        self.assertEqual(loaded_objs[0].to_dictionary()["width"], 5)
        self.assertEqual(loaded_objs[0].to_dictionary()["height"], 12)
        self.assertEqual(loaded_objs[0].to_dictionary()["x"], 0)
        self.assertEqual(loaded_objs[0].to_dictionary()["y"], 0)

        self.assertEqual(loaded_objs[1].to_dictionary()["id"], 2)
        self.assertEqual(loaded_objs[1].to_dictionary()["width"], 2)
        self.assertEqual(loaded_objs[1].to_dictionary()["height"], 6)
        self.assertEqual(loaded_objs[1].to_dictionary()["x"], 0)
        self.assertEqual(loaded_objs[1].to_dictionary()["y"], 1)

    def test_save_to_file_csv(self):
        """
        Test that the dictionary from an instance is saved to a csv file.
        """
        obj1 = Square(5, 0, 0, 1)
        obj2 = Square(2, 0, 1, 2)

        Square.save_to_file_csv([obj1, obj2])

        self.assertTrue(os.path.exists("Square.csv"))

        with open("Square.csv", "r") as file:
            csv_data = file.read()
            expected_csv_data = "id,size,x,y\n1,5,0,0\n2,2,0,1"
            self.assertEqual(csv_data, expected_csv_data)

    def test_load_from_file_csv(self):
        """
        Test that a dictionary is loaded from a csv file.
        """
        obj1 = Square(5, 0, 0, 1)
        obj2 = Square(2, 0, 1, 2)

        Square.save_to_file_csv([obj1, obj2])

        loaded_objs = Square.load_from_file_csv()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].to_dictionary()["id"], 1)
        self.assertEqual(loaded_objs[0].to_dictionary()["size"], 5)
        self.assertEqual(loaded_objs[0].to_dictionary()["x"], 0)
        self.assertEqual(loaded_objs[0].to_dictionary()["y"], 0)

        self.assertEqual(loaded_objs[1].to_dictionary()["id"], 2)
        self.assertEqual(loaded_objs[1].to_dictionary()["size"], 2)
        self.assertEqual(loaded_objs[1].to_dictionary()["x"], 0)
        self.assertEqual(loaded_objs[1].to_dictionary()["y"], 1)

        obj3 = Rectangle(5, 12, 0, 0, 1)
        obj4 = Rectangle(2, 6, 0, 1, 2)

        Rectangle.save_to_file_csv([obj3, obj4])

        loaded_objs = Rectangle.load_from_file_csv()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].to_dictionary()["id"], 1)
        self.assertEqual(loaded_objs[0].to_dictionary()["width"], 5)
        self.assertEqual(loaded_objs[0].to_dictionary()["height"], 12)
        self.assertEqual(loaded_objs[0].to_dictionary()["x"], 0)
        self.assertEqual(loaded_objs[0].to_dictionary()["y"], 0)

        self.assertEqual(loaded_objs[1].to_dictionary()["id"], 2)
        self.assertEqual(loaded_objs[1].to_dictionary()["width"], 2)
        self.assertEqual(loaded_objs[1].to_dictionary()["height"], 6)
        self.assertEqual(loaded_objs[1].to_dictionary()["x"], 0)
        self.assertEqual(loaded_objs[1].to_dictionary()["y"], 1)

if __name__ == '__main__':
    unittest.main()