import unittest
import sys
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_contructor(self):
        """
        Test that the constuctor values are assigned correctly.
        """
        rec1 = Rectangle(5, 10)
        rec2 = Rectangle(2, 10, 2, 2)
        rec3 = Rectangle(7, 6, 2, 2, 19)

        self.assertEqual(rec1.width, 5)
        self.assertEqual(rec1.height, 10)
        self.assertIsNotNone(rec1.id)

        self.assertEqual(rec2.width, 2)
        self.assertEqual(rec2.height, 10)
        self.assertEqual(rec2.x, 2)
        self.assertEqual(rec2.y, 2)

        self.assertEqual(rec3.width, 7)
        self.assertEqual(rec3.height, 6)
        self.assertEqual(rec3.x, 2)
        self.assertEqual(rec3.y, 2)
        self.assertEqual(rec3.id, 19)   

    def test_attributes_validation(self):
        """
        Test that the module is handling attribute errors.
        """
        with self.assertRaises(TypeError) as context:
            Rectangle("5", 10)
        self.assertEqual(
            str(context.exception),
            "width must be an integer"
        )
        with self.assertRaises(TypeError) as context:
            Rectangle(5.6, 10.4)
        self.assertEqual(
            str(context.exception),
            "width must be an integer"
        )
        with self.assertRaises(TypeError) as context:
            Rectangle(6, "3")
        self.assertEqual(
            str(context.exception),
            "height must be an integer"
        )

        with self.assertRaises(ValueError) as context:
            Rectangle(0, 10)
        self.assertEqual(
            str(context.exception),
            "width must be > 0"
        )
        with self.assertRaises(ValueError) as context:
            Rectangle(4, 0)
        self.assertEqual(
            str(context.exception),
            "height must be > 0"
        )  

        with self.assertRaises(ValueError) as context:
            Rectangle(2, 5, -2, 9)
        self.assertEqual(
            str(context.exception),
            "x must be >= 0"
        )
        with self.assertRaises(ValueError) as context:
            Rectangle(2, 5, 2, -9)
        self.assertEqual(
            str(context.exception),
            "y must be >= 0"
        )    

    def test_area(self):
        """
        Test the area method output the correct value
        """
        rec = Rectangle(5, 10)
        self.assertEqual(rec.area(), 50)
        
    def test_display(self):
        """
        Test the printed out shape is displayed correctly
        """
        output = "###\n###\n"
        rec = Rectangle(3, 2)
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
        output = "\n\n #####\n #####\n #####\n #####\n #####\n #####\n"
        rec = Rectangle(5, 6, 1, 2)
        capturedOutput = io.StringIO() 
        sys.stdout = capturedOutput 
        rec.display()
        sys.stdout = sys.__stdout__  
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_string_representation(self):
        """
        Test that the string respresentation of rectangle displayed correctly
        """
        rec = Rectangle(5, 10, 2, 3, 1)
        expected_str = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(rec), expected_str)

    def test_update(self):
        """
        Test that the new atrributes added is set correctly
        """
        rec = Rectangle(5, 10)
        rec.update(1, 3, 4, 2, 1)
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.width, 3)
        self.assertEqual(rec.height, 4)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, 1)

    def test_update_kwargs_only(self):
        """
        Test that the new atrributes added is set correctly with kwargs
        """
        rec = Rectangle(5, 10)
        rec.update(x=1, height=2, y=3, width=4, id=5)
        self.assertEqual(rec.id, 5)
        self.assertEqual(rec.width, 4)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 1)
        self.assertEqual(rec.y, 3)

    def test_to_dictionary(self):
        """
        Test that the dictionary is displayed correctly
        """
        r = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {
            "id": 1,
            "width": 5,
            "height": 10,
            "x": 2,
            "y": 3
        }
        self.assertDictEqual(r.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()