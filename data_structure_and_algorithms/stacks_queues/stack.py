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

    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False

    def push(self, value):
        """
        Adds a new value to the stack.
        """
        self._linked_list.push_to_front(value)

    def pop(self):
        """
        Removes the first value from the stack and returns it.
        """
        return self._linked_list.pop_front()

    def top(self):
        """
        Get the value of the last element pushed to the stack but don't remove it's node.
        """

        if self._linked_list.begin:
            return self._linked_list.begin.value
        else:
            return None

    @property
    def length(self):
        return self._linked_list.count()
