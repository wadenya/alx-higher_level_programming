#!/usr/bin/python3
"""
class student
"""


class Student:
    """Rep of student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Get a dictionary rep of students"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for y in attrs:
            try:
                new_dict[y] = self.__dict__[y]
            except FileNotFoundError:
                pass
        return new_dict
