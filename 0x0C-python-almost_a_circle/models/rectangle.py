#!/usr/bin/python3
"""Class method that inherits from Bae
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle  inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets value to width"""
        self.check_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.check_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x getter of the rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.vcheck_int("x", value)
        self.__x = value

    @property
    def y(self):
        '''y getter of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        self.check_int("y", value)
        self.__y = value

    def check_int(self, name, value, fg=True):
        """func for validating value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 and fg:
            raise ValueError("{} must be >= 0".format(name))
        elif not fg and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """function that displays the rect with '#'"""
        print("('#' * self.__width) * self.__height)
