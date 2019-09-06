class DoubleLinkedListNode(object):

    def __init__(self, value, nxt=None, prev=None):
        self.next = nxt
        self.prev = prev
        self.value = value

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{'H' if self.prev==None and self.next != None else repr(pval)},{self.value}, {'T' if self.prev!=None and self.next == None else repr(nval)}] "


class DoubleLinkedList(object):
    """
    DoubleLinkedList definition
    """
    def __init__(self):
        self.__count = 0 # Initialize to negative 2 to account for sentinels
        self.begin = self.__create_new_node(None)
        self.end = self.__create_new_node(None)
        self.begin.next = self.end
        self.end.prev = self.begin

    def __create_new_node(self, value):
        node = DoubleLinkedListNode(value, None, None)
        return node

    def _invariant(self):
        # Sent. nodes should never change their end points
        assert self.begin.prev == None, "Header's previous is not None."
        assert self.end.next == None, "Trailer's next is not None."

    def __is_empty(self):
        return self.begin.next == self.end

    def __increment_count(self):
        self.__count += 1

    def __decrement_count(self):
        self.__count -= 1

    def __insert_node(self, left_node, right_node, insert_node):
        """ Inserts a node between 2 other nodes."""
        left_node.next = insert_node
        insert_node.prev = left_node
        insert_node.next = right_node
        right_node.prev = insert_node
        self.__increment_count()

    def __detach_node(self, node_to_remove):
        value = node_to_remove.value
        node_to_remove.prev.next = node_to_remove.next
        node_to_remove.next.prev = node_to_remove.prev
        self.__decrement_count()
        return value

    def push(self, obj):
        """Appends new value on the end of the list"""
        self.__insert_node(self.end.prev, self.end, self.__create_new_node(obj))
        #self.dump()

    def pop(self):
        """ Removes and returns the last item"""
        if self.__is_empty():
            return None
        else:
            return self.__detach_node(self.end.prev)


    def shift(self, obj):
        """Another name for push"""
        self.push(obj)

    def unshift(self):
        """Removes and returns the first item."""
        if self.__is_empty():
            return None
        else:
            return self.__detach_node(self.begin.next)


    def remove(self, obj):
        """Finds a matching item and removes it from the list. Returns
            the index. """
        if self.__is_empty():
            # Empty list
            return None
        elif self.begin.next.value == obj:
            # Found at first value in list
            self.unshift()
            return 0
        else:
            # set a ptr at the first node (non-sentinel)
            ptr = self.begin.next
            index = 0
            # Traverse node until you reach the trailer
            while ptr != self.end:
                if ptr.value == obj:
                    self.__detach_node(ptr)
                    return index
                ptr = ptr.next
                index += 1
            # If no match found
            return none

    def first(self):
        """Returns a *reference* to the first item, does not remove"""
        if self.__is_empty():
            return None
        else:
             return self.begin.next.value

    def last(self):
        """ Returns a reference to the last ite, does not remove."""
        if self.__is_empty():
            return None
        else:
             return self.end.prev.value

    def count(self):
        """Count the number of elements in the list."""
        return self.__count

    def get(self, index):
        """ Get the value at index."""
        if self.__is_empty():
            return None
        else:
            ptr_index = 0
            ptr = self.begin.next # Initialize to second node

            while ptr != self.end:
                if ptr_index == index:
                    return ptr.value
                ptr_index += 1
                ptr = ptr.next

        return None

    def reverse(self):
        # self.__reverse_recursive(self.begin)
        pass

    def __reverse_recursive(self, curr):
        pass

    def dump(self, mark=None):
        """ Debugging Tool: Dump the contents of the list."""
        index = 0
        print("Mark: {}".format(mark))
        curr_node = self.begin
        if curr_node == None:
            print("Empty list")
        print("List: ", end =' ')
        while curr_node != None:
            if curr_node == self.begin:
                print("Header", end=' -> ')
            elif curr_node == self.end:
                print("Trailer", end=' -> ')
            else:
                print("{}: {}".format(index, curr_node.value), end=' -> ')
                index += 1
            curr_node = curr_node.next
            if curr_node == None:
                print("None")
