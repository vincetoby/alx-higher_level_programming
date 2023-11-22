#!/usr/bin/python3
"""Defines a class 'Node' for a linked list"""


class Node:
    """Definition of class"""
    def __init__(self, data, next_node=None):
        """Init Node with data and next_node"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not (next_node is None or isinstance(next_node, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Gets data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets data to a value.

        Args:
            value: value to be assigned to data.
        Raises:
            TypeError: value is not an integer.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next_node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node of the node.

        Args:
            value: value to set the next_node
        """
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """Init linked List with a head."""
        self.__head = None

    def __str__(self):
        """func that returns a str with all data in the list"""
        temp = self.__head
        datar = []
        while (temp is not None):
            datar.append("{:d}".format(temp.data))
            temp = temp.next_node
        return "\n".join(datar)

    def sorted_insert(self, value):
        """Inserts a new node in a sorted order"""
        temp = self.__head
        new_n = Node(value)
        if temp is None:
            self.__head = new_n
            return
        if value < temp.data:
            new_n.next_node = temp
            self.__head = new_n
            return
        while (temp.next_node is not None and value > temp.next_node.data):
            temp = temp.next_node
        new_n.next_node = temp.next_node
        temp.next_node = new_n
