class QueueNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        return "[{}:{}]".format(self.value, repr(nval))

class Queue(object):

    def __init__(self):
        self.head = None
        self.tail = None
        Queue.node_count = 0

    def enqueue(self, obj):
        """Adds a new node to the tail of the queue"""
        # Create a node
        node = QueueNode(obj, None, None)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        Queue.node_count += 1

    def dequeue(self):
        """Removes a node from the head of the queue. Returns it's value"""
        if self.head == None:
            return None
        elif self.head == self.tail:
            # One item in list
            return_node = self.head
            self.head = self.tail = None
            Queue.node_count -= 1
            return return_node.value
        else:
            return_node = self.head
            self.head = self.head.next
            Queue.node_count -= 1
            return return_node.value

    def first(self):
        """Returns a reference to the head of the queue DOES NOT remove"""
        if self.head == None:
            return None
        else:
            return self.head.value

    def last(self):
        """Returns a reference to the tail of the queue DOES NOT remove"""
        if self.tail == None:
            return None

        return self.tail.value

    def count(self):
        """Returns a count of the number of nodes in the queue"""
        return Queue.node_count

    def dump(self, note='----'):
        """Debugging function that dumps the contents of the list."""
        index = 0
        print("Note: {}".format(note))
        curr_node = self.head
        if curr_node == None:
            print("Empty list")
        print("List: ", end =' ')
        while curr_node != None:
            print("{}: {}".format(index, curr_node.value), end=' -> ')
            curr_node = curr_node.next
            if curr_node == None:
                print("None")
            index += 1


"""Tests"""
def test_enqueue():
    """Each new value should be added to the 'top' of the stack"""
    print("----------Testing Enqueue----------")
    colors = Queue()
    assert colors.count() == 0
    
    colors.enqueue("Red")
    assert colors.count() == 1
    
    colors.dump()
    colors.enqueue("Yellow")
    
    assert colors.count() == 2
    colors.dump()

    colors.enqueue("Blue")
    assert colors.count() == 3
    colors.dump()

def test_dequeue():
    """Each new value should be added to the 'top' of the stack"""
    print("----------Testing Dequeue----------")
    colors = Queue()
    assert colors.count() == 0
    assert colors.dequeue() == None

    colors.enqueue("Red")
    assert colors.dequeue() == "Red"
    colors.enqueue("Yellow")
    colors.enqueue("Blue")
    colors.enqueue("Green")
    colors.dump("before dequing yellow")
    assert colors.dequeue() == "Yellow"
    colors.dump("after dequing yellow")

def test_first():
    print("----------Testing First----------")
    colors = Queue()
    assert colors.first() == None

    colors.enqueue("Red")
    assert colors.first() == "Red"

    colors.enqueue("Yellow")
    assert colors.first() == "Red"

    colors.dequeue()
    colors.dequeue()

    assert colors.first() == None

def test_last():
    print("----------Testing Last----------")
    colors = Queue()
    assert colors.last() == None

    colors.enqueue("Red")
    assert colors.last() == "Red"

    colors.enqueue("Yellow")
    assert colors.last() == "Yellow"

    colors.enqueue("Green")
    assert colors.last() == "Green"

    colors.enqueue("Blue")
    assert colors.last() == "Blue"
    colors.dump("Before emptying queue")

    colors.dequeue()
    colors.dump("After dequeuing Red")
    colors.dequeue()
    colors.dump("After dequeuing Yellow")
    colors.dequeue()
    colors.dump("After dequeuing Green")
    colors.dequeue()
    colors.dump("After emptying queue")
    assert colors.last() == None    


""" Run Tests"""
if __name__ == '__main__':
    test_enqueue()
    test_dequeue()
    test_first()
    test_last()