#!/usr/bin/python3
class LockedClass:
    __slot__ = ["first_name"]

    def __int__(self):
        self.first_name = None
