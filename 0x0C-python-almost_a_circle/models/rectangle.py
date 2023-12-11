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
        self.check_int("x", value)
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
        return self.height * self.width

    def display(self):
        """function that displays the rect with '#'"""
        print('\n' * self.y + (' ' * self.x + '#' * self.width + '\n')\
                * self.height, end="")

    def __str__(self):
        """recturns info of rect"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,\
                self.x, self.y, self.width, self.height)

     def __ups(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method that updates instance attr via * or**args'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates instance attributes via no-keyword & keyword args"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        elif kwargs:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]
