# Run with:
#   pytest bubble-sort.py

import pytest
from dllist import DoubleLinkedList
import sorting
from random import randint

max_numbers = 20

def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.shift(randint(0,10000))
    return numbers

def is_sorted(numbers):
    node = numbers.begin.next
    while node and node.next and node != numbers.end.prev:
        if node.value > node.next.value:
            return False
        else:
            node = node.next
    return True

def test_bubble_sort():
    assert 'a' == 'a'
    numbers = random_list(max_numbers)
    sorting.bubble_sort(numbers)
    assert is_sorted(numbers)

if __name__ == '__main__':
    test_bubble_sort()
