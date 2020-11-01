"""
Tests for Stack Data Structure

Operations to Test:
    Push
    Pop
    Top
    is_empty
    length
"""

from data_structure_and_algorithms import Stack
import pytest
from random import shuffle

class TestStack:
    TEST_VALUES = [
        "alpha",
        "bravo",
        "charlie",
        "delta",
        "echo",
        "foxtrot",
        "golf",
        "hotel",
        "india",
        "juliet",
        "kilo",
        "lima"
    ]

    def test_push(self):
        """
        Test Push functionality
        """

        # Randomize test values
        test_list = self.TEST_VALUES[0:3]
        shuffle(test_list)

        # Create a new Stack
        stack = Stack()

        # Push each value from the random test values to stack
        for elem in test_list:
            stack.push(elem)

        assert stack.length == len(test_list)
        #assert stack.top() == test_list[-1]
        #assert stack.pop() == test_list[-1]

    def test_pop(self):
        # Create a new stack
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.top() == 3

    def test_top(self):
        # Create a new stack
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.top() == 3

    def test_is_empty(self):
        # Create a new stack
        stack = Stack()

        assert stack.is_empty() == True
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.top() == 3
        assert stack.is_empty() == False


    def test_length(self):
        """
        Test the length of a list.
        """
        # Create a new stack
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        # Test Length
        assert stack.length == 3
