#!/usr/bin/python3
'''smt'''


class Rectangle:
    '''a class that defines the a rectangle
        properties: getter and setter methods for width and height
        methods: __init__ method -for creating a class
        area method - for calculating the area of the rectangle
        perimeter method -for calculating the perimeter of rectangle
        __str__ methods - that returns the string representation of
        Rectangle instance(s)
        _repr__ method - returns the formal strig representation of
                an object that can be evaluated
        _del_ method - performs clean up operation before an object
                is deleted'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2*(self.__height + self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for _ in range(self.__height):
            rectangle += "#" * self.__width + "\n"
        return rectangle.rstrip()

    def __repr__(self):
        return f"Rectangle ({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
