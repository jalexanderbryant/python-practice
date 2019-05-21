import ctypes

class DynamicArray:
    """A dynamic array class akin to a simplified python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0                                     # count actual elements
        self._capacity = 1                              # default array capacity
        self._A = self._make_array(self._capacity)      # low-level array


    def __len__(self):
        """Return number of actual elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:                        # if k is greater than or equal to 0,
                                                        # and k is less than the count of the elements
            raise IndexError('invalid index')           # Raise index error
        
        return self._A[k]                               # Retreive from array

    def append(self, obj):
        
        """Add object to end of the array."""
        if self._n == self._capacity:                   # not enough room
            self._resize(2 * self._capacity)            # double the capacity
        self._A[self._n] = obj                          # Add obj to array
        self._n += 1                                    # Increment count of elements


    def _resize(self, c):                               # nonpublic utility
        """Resize internal array to capacity c."""
        B = self._make_array(c)                         # create new, bigger array
        for k in range(self._n):                        # For each existing value...
            B[k] = self._A[k]                               # add to the new array
        self._A = B                                     # Point interal array A to B
        self._capacity = c                              # Update the capacity

    def _make_array(self, c):                           # nonpublic utility
        """Return new array with capacity c."""
        return (c* ctypes.py_object)()