#!/usr/bin/python3
"""defines a class Rectangle that defines a rectangle
"""


class Rectangle:
    """a class, rectangle definition that takes two private instance
        attributes

        Args:
            width: an int, horizontal dimension
            height: integer, vertical dimension

        Attributes:
            number_of_instances: increments each time and instance is added
                decrements when it is deleted
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):

        type(self).number_of_instances += 1
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

    def print_rectangle(self):
        """prints the rectangle with #

            Attributes:
                __width: horizontal dimension
                __height: vertical dimension
                str: string of # chars

            Returns: str containing printed rectangle
        """
        str = ""
        for i in range(self.__height):
            for j in range(self.width):
                str = str + '#'

            if self.__width != 0 and i < self.__height - 1:
                str = str + '\n'
        return str

    def __str__(self):
        """permits direct printing of str
        """
        return self.print_rectangle()

    def __repr__(self):
        """allows the use of eval

            Returns: the string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(self):
        """detects and prints a message whenever an instance is deleted
            and decrements the number_of_instances values in the process

        """
        self.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two instances and returns the larger of the two.

             Args:
                rect_1 (Rectangle object): first instnce
                rect_2 (Rectangle object): second instance

            Raises:
                TypeError: if rect_1 or rect_2 isnt an instance of class

            Returns:
                the larger instance or rect_1 if they are equal

        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() <= rect_1.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns an instance with equal sides.

        Args:
            size: int representing length of sides

        Returns:
            new instance of class with equal sides (square)

        """
        return cls(size, size)
