from dynamic_array import DynamicArray
import sys
def test_dynamic_array():
    new_array = DynamicArray()

    assert new_array._capacity == 1     # should be equal to 1
    assert new_array._n == 0        # should be empty

    new_array.append(None)
    assert new_array._capacity == 1

    new_array.append(None)
    assert new_array._capacity == 2

    new_array.append(None)
    assert new_array._capacity == 4

    new_array.append(None)
    assert new_array._capacity == 4
    assert new_array.__len__() == 4
    
    new_array.append(None)
    assert new_array.__len__() == 5
    assert new_array._capacity == 8


def test_print():
    data = DynamicArray()
    for i in range(27):
        print("Count: {0:2d}; Capacity: {1:2d}".format( data._n, data._capacity))
        data.append(None)



