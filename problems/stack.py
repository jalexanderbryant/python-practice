
# node object
#   data,
#   next
class node():
  data = None
  next_node = None

  def __init__(self, data, next_node):
    self.data = data
    self.next_node = next_node

# stack interface
  # attr => head (front node object)
  # method => push
  # method => pop
class stack():
  head = None

  def __init__(self):
    pass

  def push(self, data):
    # no items in stack
    if self.head == None:
      self.head = node(data, None)
    # items already in stack
    else: 
      print("adding new node")
      new_node = node(data, self.head)
      self.head = new_node

  def pop(self):
    if self.head == None:
      return None
    # remove head and return value from node
    data = self.head.data
    self.head = self.head.next_node
    return data


  def print(self):
    curr_node = self.head
    while(curr_node != None):
      print(curr_node.data, end=' ')
      curr_node = curr_node.next_node



if __name__ == '__main__':
  new_stack = stack()
  new_stack.push(1)
  new_stack.push(2)
  new_stack.push(3)
  new_stack.push(4)
  new_stack.print()
  new_stack.pop
  new_stack.print()