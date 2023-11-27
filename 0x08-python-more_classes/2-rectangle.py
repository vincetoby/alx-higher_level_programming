#!/usr/bin/python3
"""defines a class Rectangle that defines a rectangle
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

    def area(self):
        """returns area of rectangle

             Attributes:
                 __width: horizontal dimension
                __height: vertical dimension

            Returns:
                area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """returns aperimeter of rectangle

            Attributes:
                __width: horizontal dimension
                __height: vertical dimension

            Returns:
                0 if any attribute = 0, or the perimeter: (__width * 2) +
            (__height * 2).

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
