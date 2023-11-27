#!/usr/bin/python3
"""defines an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """a class, rectangle definition that takes two private instance
        attributes

        Args:
            width: an int, horizontal dimension
            height: integer, vertical dimension
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter

            Returns:
                it returns the private instance of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width to a value

            Args:
                value: value to initial width

            Raises:
                TypeError: If `value` is not an int.
                ValueError: If `value` is less than 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter

            Returns:
                it returns the private instance of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets height to a value

            Args:
                value: value to initial height

            Raises:
                TypeError: If `value` is not an int.
                ValueError: If `value` is less than 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
