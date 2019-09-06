class SingleLinkedListNode(object):

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList(object):
    """
    Single Linked List definition
    """

    def __init__(self):
        self.begin = None
        self.end = None
        self.__count = 0

    def __create_new_node(self, value):
        self.__count += 1
        return SingleLinkedListNode(value, None)

    def push(self, obj):
        """Appends new value on the end of the list"""
        new_node = self.__create_new_node(obj)
        if self.begin == None: # Empty list
            self.begin = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        #self.dump()

    def pop(self):
        """ Removes and returns the last item"""
        self.dump()
        value = None

        if self.begin == None: # Empty list
            return None
        elif self.begin == self.tail: # Only one element
            value = self.tail.value
            self.begin = self.end = None
            self.__count -= 1
        else:
            self.__count -= 1
            value = self.tail.value
            curr = self.begin
            while curr.next != self.tail:
                curr = curr.next
            self.tail = curr
            curr.next = None
        self.dump()
        return value


    def shift(self, obj):
        """Another name for push."""
        self.push( obj )

    def unshift(self):
        """Removes and returns the first item."""
        if self.begin == None: # empty list
            return None
        else:
            self.__count -= 1
            value = self.begin.value
            self.begin = self.begin.next
            return value

    def remove(self, obj):
        """Finds a matching item and removes it from the list. Returns
            the index. """
        # No nodes in list
        if self.begin == None:
            return None
        index = 0

        # At at least one node in list AND match occurs at head of list
        if self.begin.value == obj:
            self.begin = self.begin.next
            return index

        # If match occurs after first elemetn
        ptr = self.begin
        while ptr != self.tail:
            index += 1
            if ptr.next.value == obj:
                ptr.next = ptr.next.next
                return index
            ptr = ptr.next

        return None


    def first(self):
        """Returns a *reference* to the first item, does not remove"""
        if self.begin == None:
            return None
        else:
            return self.begin.value

    def last(self):
        """ Returns a reference to the last ite, does not remove."""
        if self.tail == None:
            return None
        else:
            return self.tail.value

    def count(self):
        """Count the number of elements in the list."""
        return self.__count

    def get(self, index):
        """ Get the value at index."""
        if self.begin == None or index > self.__count - 1:
            return None
        # start count at 0
        count = 0
        # init a node for traversal, point it at the head of list
        curr_node = self.begin

        # Iterate over the list with the traversal node
        while curr_node != None:
            # For each node encountered
            # Check if the count matches the index
            # If a match 
            if count == index:
                # Return the value
                return curr_node.value
            # traverse nodes
            curr_node = curr_node.next
            # increment count by 1
            count += 1

        # End of traversal without returing a value? Return None
        return None

    def reverse(self):
        self.__reverse_recursive(self.begin)

    def __reverse_recursive(self, curr):
        if curr.next == None:
            self.begin = curr
            return
        else:
            self.__reverse_recursive(curr.next)
            node = curr.next
            node.next = curr
            curr.next = None

    def dump(self, mark=None):
        """ Debugging Tool: Dump the contents of the list."""
        index = 0
        print("Mark: {}".format(mark))
        curr_node = self.begin
        if curr_node == None:
            print("Empty list")
        print("List: ", end =' ')
        while curr_node != None:
            print("{}: {}".format(index, curr_node.value), end=' -> ')
            curr_node = curr_node.next
            if curr_node == None:
                print("None")
            index += 1
