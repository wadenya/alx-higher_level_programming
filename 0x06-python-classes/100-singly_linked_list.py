#!/usr/bin/python3
"""Defines classes for a singly linked list"""

class  Node:
    """Represent a node in a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initializes a new node.
        Arguments: data (int): The data of the new Node.
        next_node (Node): The next node of the new Node."""
        salf.data = data
        self.next_node = next_node

