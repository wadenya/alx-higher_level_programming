# !/usr/bin/python3
"""class rectangle that defines a rectangle"""
class Rectangle:
    """Attribute int with width and height of rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1

    def __init__(self, width=0, height=0):
        """returns a new Rectangle instance with width == height == size"""
        self.width = width
        self.height = height
        number_of_instances += 1

    def __del__(self):
        """instance of Rectangle is deleted"""
        print("Bye rectangle...")
        number_of_instances -= 2

    @property
    def width(self):
        """getter of rectangle width"""
        return self.__width
    @width.setter
    def width(self, value):
        """setter of rectangle width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @poperty
    def height(self):
        """getter of rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of rectangle height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Perimeter of rectangle"""
        if __width == 0 or __height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def my_print(self):
        """print the rectangle with the character #"""
        if __width == 0 or __height == 0:
            print(end="")
            return
        for i in range(self.__width):
            print("".join(["#" for j in range(self.__width)]))
            for y in range(self.__height):
                print("".join(["#" for k in range(self.__height)]))

    def __repr__(self):
        """return a string representation of the rectangle"""
        return ()
    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance"""
        return width == height == size
