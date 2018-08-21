class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return "[{}:{}]".format(self.value,repr(nval))

class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None
        self.node_count = 0

    def push(self, obj):
        """Appends a new value on the end of the list."""
        # create new node
        new_node = SingleLinkedListNode(obj, None)
        # Empty list
        if self.node_count == 0: 
            self.begin = self.end = new_node
        else:
            self.end.next = new_node
            self.end = self.end.next
        self.node_count +=1

    def pop(self):
        """Removes the last item and returns it."""
        if self.node_count == 0:
            return None
        elif self.node_count == 1:
            return_node = self.begin
            self.begin = self.end = None
            self.node_count -= 1

            return return_node.value
        else:
            iter_node = self.begin
            while iter_node.next != self.end:
                iter_node = iter_node.next

            return_node = iter_node.next
            iter_node.next = None
            self.end = iter_node
            self.node_count -= 1

            return return_node.value

    def shift(self, obj):
        """Another name for push."""
        self.push(obj)

    def unshift(self):
        """Removes the first item and returns it."""
        if self.node_count == 0: 
            return None
        elif self.node_count == 1:
            return_node = self.begin
            self.begin = self.end = None
            self.node_count -= 1
            return return_node.value
        else:
            return_node = self.begin
            self.begin = self.begin.next
            self.node_count -= 1
            return return_node.value

    def remove(self, obj):
        """Finds a matching item and removes it from the list. Returns index"""
        if self.node_count==0:
            return None
        elif self.node_count == 1 and self.begin.value != obj:
            return None
        else:
            index = 0
            # Case 1 - Obj is at start of list...
            if self.begin.value == obj:
                node = self.unshift()
                return index
            # Case 2 - Obj is AT LEAST the second element in list
            iter_node = self.begin
            while iter_node.next != None:
                index += 1
                if iter_node.next.value == obj:
                    return_node = iter_node.next
                    iter_node.next = iter_node.next.next
                    return_node.next = None # no longer a pointer to this
                    return index
                iter_node = iter_node.next

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        if self.begin is None:
            return None
        else:
            return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        if self.begin is None:
            return None
        else:
            return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        return self.node_count

    def get(self, index):
        """Get the value at index."""
        if self.begin is None:
            return None
        else:
            internal_index = 0
            # Case 1 - Obj is at start of list...
            if index == 0:
                return self.begin.value

            # Case 2 - Obj is AT LEAST the second element in list
            iter_node = self.begin
            while iter_node != None:
                if internal_index == index:
                    return iter_node.value
                internal_index += 1
                iter_node = iter_node.next

    def reverse(self):
        pass

    def dump(self, mark=None):
        """Debugging function that dumps the contents of the list."""
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


# Test methods

def test_push():
    colors = SingleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2

def test_pop():
    colors = SingleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None

def test_unshift():
    colors = SingleLinkedList()
    colors.push("Viridian")
    colors.push("Sap Green")
    colors.push("Van Dyke")
    assert colors.unshift() == "Viridian"
    assert colors.unshift() == "Sap Green"
    assert colors.unshift() == "Van Dyke"
    assert colors.unshift() == None

def test_shift():
    colors = SingleLinkedList()
    colors.shift("Cadmium Orange")
    assert colors.count() == 1
    colors.shift("Carbazole Violet")
    assert colors.count() == 2
    assert colors.pop() == "Carbazole Violet"
    assert colors.count() == 1
    assert colors.pop() == "Cadmium Orange"
    assert colors.count() == 0

def test_remove():
    colors = SingleLinkedList()
    colors.push("Cobalt")
    colors.push("Zinc White")
    colors.push("Nickle Yellow")
    colors.push("Perinone")
    colors.dump()
    assert colors.remove("Cobalt") == 0
    colors.dump("before perinone")
    assert colors.remove("Perinone") == 2
    colors.dump("after perinone")
    assert colors.remove("Nickle Yellow") == 1
    assert colors.remove("Zinc White") == 0

def test_first():
    colors = SingleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.first() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Pthalo Green")
    assert colors.first() == "Cadmium Red Light"

def test_last():
    colors = SingleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.last() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.last() == "Hansa Yellow"
    colors.shift("Pthalo Green")
    assert colors.last() == "Pthalo Green"

def test_get():
    colors = SingleLinkedList()
    colors.push("Vermillion")
    assert colors.get(0) == "Vermillion"
    colors.push("Sap Green")
    colors.dump()
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    colors.push("Cadmium Yellow Light")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == "Cadmium Yellow Light"
    assert colors.pop() == "Cadmium Yellow Light"
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == None
    colors.pop()
    assert colors.get(0) == "Vermillion"
    colors.pop()
    assert colors.get(0) == None

def test_reverse():
    print("Testing Reverse")
    colors = SingleLinkedList()
    colors.push("Vermillion")
    colors.push("Sap Green")
    colors.push("Cadmium Yellow Light")
    colors.push("Hansa Yellow")
    assert colors.get(0) is "Vermillion"
    assert colors.get(1) is "Sap Green"
    assert colors.get(2) is "Cadmium Yellow Light" 
    assert colors.get(3) is "Hansa Yellow"
    colors.dump()
    colors.reverse()
    # colors.dump()
    # assert colors.get(0) is "Hansa Yellow"
    # assert colors.get(1) is "Cadmium Yellow Light" 
    # assert colors.get(2) is "Sap Green"
    # assert colors.get(3) is "Vermillion"

    
# Run Tests
if __name__ == '__main__':
    # test_push()
    # test_pop()
    # test_shift()
    # test_unshift()
    # test_remove()
    # test_first()
    # test_last()
    # test_get()
    test_reverse()