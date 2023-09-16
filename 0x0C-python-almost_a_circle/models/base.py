#!/usr/bin/python3
"""
This module is for class Base

"""
import json
import os
import turtle


class Base:
    """
    base class

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initial function
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list[dict,...]): list of dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            from_json_string (str): string representing a list of dictionaries
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits from Base
        """
        path = "{}.json".format(cls.__name__)
        if list_objs:
            dict_list = [obj.to_dictionary() for obj in list_objs]
        else:
            dict_list = []
        with open(path, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dict_list))

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        path = "{}.json".format(cls.__name__)
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            json_dict_list = f.read()
        dict_list = cls.from_json_string(json_dict_list)
        instance_list = []
        for obj in dict_list:
            instance = cls.create(**obj)
            instance_list.append(instance)
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the csv string representation of list_objs to a csv

        Args:
            list_objs (list): list of instances who inherits from Base
        """
        path = "{}.csv".format(cls.__name__)
        if list_objs:
            dict_list = [obj.to_dictionary() for obj in list_objs]
        else:
            dict_list = []
        csv_list = []
        if cls.__name__ == "Square":
            for obj in dict_list:
                _id = obj['id']
                _size = obj['size']
                _x = obj['x']
                _y = obj['y']
                csv_line = f"{_id},{_size},{_x},{_y}"
                csv_list.append(csv_line)
        else:
            for obj in dict_list:
                _id = obj['id']
                _width = obj['width']
                _height = obj['height']
                _x = obj['x']
                _y = obj['y']
                csv_line = f"{_id},{_width},{_height},{_x},{_y}"
                csv_list.append(csv_line)
        with open(path, "w", encoding="utf-8") as f:
            if cls.__name__ == "Square":
                f.write("id,size,x,y\n")
            else:
                f.write("id,width,height,x,y\n")
            f.write('\n'.join(csv_list))

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances from csv
        """
        path = "{}.csv".format(cls.__name__)
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            csv_data = f.read().split('\n')
        dict_list = []
        if 'size' in csv_data[0]:
            for csv_line in csv_data[1:]:
                csv_values = csv_line.split(',')
                dict_list.append(
                    {
                        "id": int(csv_values[0]),
                        "size": int(csv_values[1]),
                        "x": int(csv_values[2]),
                        "y": int(csv_values[3]),
                    }
                )
        else:
            for csv_line in csv_data[1:]:
                csv_values = csv_line.split(',')
                dict_list.append(
                    {
                        "id": int(csv_values[0]),
                        "width": int(csv_values[1]),
                        "height": int(csv_values[2]),
                        "x": int(csv_values[3]),
                        "y": int(csv_values[4]),
                    }
                )
        instance_list = []
        for obj in dict_list:
            instance = cls.create(**obj)
            instance_list.append(instance)
        return instance_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Args:
            dictionary (dict): dictionary with key/value
        """
        if cls.__name__ == "Square":
            instance = cls(1)
        else:
            instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares

        Args:
            list_rectangles (dict): dictionary with key/value
            list_squares (dict): dictionary with key/value
        """
        screen = turtle.Screen()
        screen.title("ALX: Let's draw it")
        screen.bgcolor("white")

        for sq in list_squares:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.setpos(sq.x, sq.y)
            t.pendown()
            t.color("red")
            t.forward(sq.size)
            t.right(90)
            t.forward(sq.size)
            t.right(90)
            t.forward(sq.size)
            t.right(90)
            t.forward(sq.size)
            t.penup()

        for rec in list_rectangles:
            t2 = turtle.Turtle()
            t2.hideturtle()
            t2.penup()
            t2.setpos(rec.x, rec.y)
            t2.pendown()
            t2.color("blue")
            t2.forward(rec.width)
            t2.right(90)
            t2.forward(rec.height)
            t2.right(90)
            t2.forward(rec.width)
            t2.right(90)
            t2.forward(rec.height)
            t2.penup()

        screen.exitonclick()
