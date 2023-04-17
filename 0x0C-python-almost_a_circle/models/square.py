#!/usr/bin/python3
"""
A Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ReP a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args(int):
            size(width, height): The size of the new Square.
            x: The x coordinate of the new Square.
            y: The y coordinate of the new Square.
            id: The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set/get size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args: *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd // // size attribute
                - 3rd // // x attribute
                - 4th // // y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for c, h in kwargs.items():
                if c == "id":
                    if h is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = h
                elif c == "size":
                    self.size = h
                elif c == "x":
                    self.x = h
                elif c == "y":
                    self.y = h

    def to_dictionary(self):
        """Return the dictionary rep of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() rep of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
