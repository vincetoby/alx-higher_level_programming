#!/usr/bin/python3
"""class square that inherits from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info abt the square'''
        return '[{}] ({}) {}/{} - {}'.format(type(self).__name__,\
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets value to size"""
        self.width = value
        self.height = value

    def __ups(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates instance attr via * or**args'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates instance attributes via no-keyword & keyword args"""
        if args:
            self.__ups(*args)
        elif kwargs:
            self.__ups(**kwargs)

    def to_dictionary(self):
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
