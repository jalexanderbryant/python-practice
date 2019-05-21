class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return "[{}:{}]".format(self.value, repr(nval))



class Stack(object):

    def __init__(self):
        self.begin = None
        Stack.node_count = 0

    def push(self, obj):
        """Pushes a new value to the top of the stack."""
        # Create new node
        sn = StackNode(obj, None)
        if self.begin is None:
            self.begin = sn
        else:
            sn.next = self.begin
            self.begin = sn

        Stack.node_count += 1

    def pop(self):
        """Pops the value that is currently on the top of the stack."""
        if self.begin is None:
            return None

        return_node = self.begin
        self.begin = self.begin.next
        Stack.node_count -= 1
        return return_node.value

    def top(self):
        """Returns a *reference* to the first item, does not remove."""
        if self.begin is None:
            return None

        return self.begin.value

    def count(self):
        """Counts the number of elements in the stack."""
        return Stack.node_count

    def dump(self, mark="----"):
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

"""Test Methods"""
def test_create():
    """Should return empty Stack"""
    colors = Stack()
    assert colors.top() is None

def test_push():
    """Each new value should be added to the 'top' of the stack"""
    print("----------Testing Push----------")
    colors = Stack()
    colors.push("Red")
    assert colors.top() is "Red"
    colors.dump()

    colors.push("Yellow")
    assert colors.top() is "Yellow"
    colors.dump()

    colors.push("Blue")
    assert colors.top() is "Blue"
    colors.dump()

def test_pop():
    """Each popped value should come from the 'top' of the stack"""
    print("----------Testing Pop----------")
    colors = Stack()
    assert colors.pop() is None

    colors.push("Red")
    assert colors.pop() is "Red"

    colors.push("Yellow")
    colors.push("Blue")
    colors.push("Green")
    colors.dump()
    
    assert colors.pop() is "Green"
    colors.dump("after Popping Green")

    assert colors.pop() is "Blue"
    colors.dump("after Popping Blue")

    assert colors.pop() is "Yellow"
    colors.dump("After popping yellow")

    assert colors.pop() is None

def test_top():
    """Each returned value should come from the top without altering the list"""
    print("----------Testing Top----------")
    colors = Stack()
    assert colors.top() is None

    colors.push("Red")
    assert colors.top() is "Red"
    colors.dump()

    colors.push("Yellow")
    assert colors.top() is "Yellow"
    colors.dump()

    colors.push("Blue")
    assert colors.top() is "Blue"
    colors.dump()

def test_count():
    """Should return the correct count for number of nodes in the stack"""
    print("----------Testing Count----------")
    colors = Stack()
    assert colors.count() is 0

    colors.push("Red")
    assert colors.count() is 1

    colors.push("Yellow")
    colors.push("Green")
    colors.push("Blue")
    assert colors.count() is 4
    colors.dump("After loading")

    colors.pop()
    colors.pop()
    colors.pop()
    colors.pop()
    assert colors.count() is 0
    

"""Run tests"""
if __name__ == '__main__':
    test_create()
    test_push()
    test_pop()
    test_top()
    test_count()