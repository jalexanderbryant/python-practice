class DoubleLinkedListNode(object):

	def __init__(self, value, nxt, prev):
		self.value = value
		self.next = nxt
		self.prev = prev

	def __repr__(self):
		nval = self.next and self.next.value or None
		pval = self.prev and self.prev.value or None
		return "[{}, {}, {}]".format(self.value, repr(nval), repr(pval))

class DoubleLinkedList(object):

	def __init__(self):
		self.begin = None
		self.end = None
		DoubleLinkedList.node_count = 0

	def push(self, obj):
		"""Appends a new value on the end of the list."""
		# Create new node
		new_node = DoubleLinkedListNode(obj, None, None)

		if self.begin is None:
			self.begin = self.end = new_node
		else:
			new_node.prev = self.end
			self.end.next = new_node
			self.end = self.end.next

		DoubleLinkedList.node_count += 1


	def pop(self):
		"""Removes the last item and returns it."""
		if self.begin is None: 
			return None
		if DoubleLinkedList.node_count == 1:
			return_node = self.begin
			self.begin = self.end = None
			DoubleLinkedList.node_count -= 1
			return return_node.value
		else:
			return_node = self.end
			self.end = self.end.prev
			self.end.next = None
			DoubleLinkedList.node_count -= 1
			return return_node.value



	def shift(self, obj):
		"""Actually just another name for push."""
		self.push(obj)

	def unshift(self):
		"""Removes the first item (from begin) and returns it."""
		if self.begin is None:
			return None
		elif DoubleLinkedList.node_count == 1:
			return self.pop()
		else:
			return_node = self.begin
			self.begin = self.begin.next
			DoubleLinkedList.node_count -= 1
			return return_node.value

	def detach_node(self, node):
		"""You'll need to use this operation sometimes, but mostly 
		inside remove().  It should take a node, and detach it from
		the list, whether the node is at the front, end, or in the middle."""

		# Cases...
		# 	item at front of list
		if self.begin == node:
			pass
		# 	item at end of list
		# 	item in middle of list


	def remove(self, obj):
		"""Finds a matching item and removes it from the list."""
		# Find the node
		if DoubleLinkedList.node_count == 0:
			return None
		elif DoubleLinkedList.node_count == 1 and self.begin.value != obj:
			return None
		else:
			index = 0
			if self.begin.value == obj:
				self.unshift()
				return index
			else:
				# object at second element
				iter_node = self.begin
				while iter_node.next != None:
					index +=1
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
		if self.begin == self.end:
			return self.begin.value
		else:
			return self.end.value


	def count(self):
		"""Counts the number of elements in the list."""
		return DoubleLinkedList.node_count

	def get(self, index):
		"""Get the value at index."""
		list_index = 0
		if self.begin is None: 
			return None
		if index is 0:
			return self.begin.value

		# Value is at least at the second element
		iter_node = self.begin
		while iter_node != None:
			if list_index is index:
				return iter_node.value
			list_index += 1
			iter_node = iter_node.next

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


def test_push():
    colors = DoubleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2

def test_pop():
    colors = DoubleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None

def test_unshift():
    colors = DoubleLinkedList()
    colors.push("Viridian")
    colors.push("Sap Green")
    colors.push("Van Dyke")
    assert colors.unshift() == "Viridian"
    assert colors.unshift() == "Sap Green"
    assert colors.unshift() == "Van Dyke"
    
    assert colors.unshift() == None

def test_shift():
    colors = DoubleLinkedList()
    colors.shift("Cadmium Orange")
    assert colors.count() == 1
    colors.shift("Carbazole Violet")
    assert colors.count() == 2
    assert colors.pop() == "Carbazole Violet"
    assert colors.count() == 1
    assert colors.pop() == "Cadmium Orange"
    assert colors.count() == 0

def test_remove():
    colors = DoubleLinkedList()
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
    colors = DoubleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.first() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Pthalo Green")
    assert colors.first() == "Cadmium Red Light"

def test_last():
    colors = DoubleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.last() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.last() == "Hansa Yellow"
    colors.shift("Pthalo Green")
    assert colors.last() == "Pthalo Green"

def test_get():
    colors = DoubleLinkedList()
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

if __name__ == '__main__':
	test_push()
	test_pop()
	test_shift()
	test_unshift()
	test_first()
	test_last()
	test_remove()
	test_get()