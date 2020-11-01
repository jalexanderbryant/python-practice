"""
Stack Class
Inherits from SLLIST (Single Linked List)
Supports operations: Push, Pop, Top, Length, Is_Empty
"""

from data_structure_and_algorithms import SingleLinkedList

class Stack:
    def __init__(self):
        """
        """
        self._linked_list = SingleLinkedList()
        self._length = 0

    def push(self, value):
        """
        Adds a new value to the stack.
        """
        self._linked_list.push_to_front(value)
        self._length += 1

    def pop(self):
        """
        Removes the first value from the stack and returns it.
        """
        pass

    def top(self):
        """
        Return the value of the element that was last pushed to the stack but don't remove it.
        """

        if self._linked_list.begin:
            return self._linked_list.begin.value
        else:
            return None

    @property
    def length(self):
        return self._linked_list.count()
