import unittest
import sys
import io
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_contructor(self):
        """
        Test that the constuctor values are assigned correctly.
        """
        sq1 = Square(5)
        sq2 = Square(2, 2, 2)
        sq3 = Square(7, 2, 2, 19)

        self.assertEqual(sq1.size, 5)
        self.assertIsNotNone(sq1.id)

        self.assertEqual(sq2.size, 2)
        self.assertEqual(sq2.x, 2)
        self.assertEqual(sq2.y, 2)

        self.assertEqual(sq3.size, 7)
        self.assertEqual(sq3.x, 2)
        self.assertEqual(sq3.y, 2)
        self.assertEqual(sq3.id, 19)   

    def test_attributes_validation(self):
        """
        Test that the module is handling attribute errors.
        """
        with self.assertRaises(TypeError) as context:
            Square("5")
        self.assertEqual(
            str(context.exception),
            "width must be an integer"
        )
        with self.assertRaises(TypeError) as context:
            Square(5.6)
        self.assertEqual(
            str(context.exception),
            "width must be an integer"
        )

        with self.assertRaises(ValueError) as context:
            Square(0)
        self.assertEqual(
            str(context.exception),
            "width must be > 0"
        )

        with self.assertRaises(ValueError) as context:
            Square(2, -2, 9)
        self.assertEqual(
            str(context.exception),
            "x must be >= 0"
        )
        with self.assertRaises(ValueError) as context:
            Square(2, 2, -9)
        self.assertEqual(
            str(context.exception),
            "y must be >= 0"
        )    

    def test_area(self):
        """
        Test the area method output the correct value
        """
        rec = Square(5)
        self.assertEqual(rec.area(), 25)
        
    def test_display(self):
        """
        Test the printed out shape is displayed correctly
        """
        output = "###\n###\n###\n"
        rec = Square(3)
        capturedOutput = io.StringIO() 
        sys.stdout = capturedOutput 
        rec.display()
        sys.stdout = sys.__stdout__  
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_with_x_and_y(self):
        """
        Test the printed out shape is displayed correctly with respect to
        x and y values
        """
        output = "\n\n #####\n #####\n #####\n #####\n #####\n"
        rec = Square(5, 1, 2)
        capturedOutput = io.StringIO() 
        sys.stdout = capturedOutput 
        rec.display()
        sys.stdout = sys.__stdout__  
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_string_representation(self):
        """
        Test that the string respresentation of rectangle displayed correctly
        """
        rec = Square(5, 2, 3, 1)
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(rec), expected_str)

    def test_update(self):
        """
        Test that the new atrributes added is set correctly
        """
        rec = Square(5)
        rec.update(1, 3, 2, 1)
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.size, 3)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, 1)

    def test_update_kwargs_only(self):
        """
        Test that the new atrributes added is set correctly with kwargs
        """
        rec = Square(2)
        rec.update(x=1, size=3, y=3, id=5)
        self.assertEqual(rec.id, 5)
        self.assertEqual(rec.size, 3)
        self.assertEqual(rec.x, 1)
        self.assertEqual(rec.y, 3)

    def test_to_dictionary(self):
        """
        Test that the dictionary is displayed correctly
        """
        r = Square(5, 2, 3, 1)
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertDictEqual(r.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()