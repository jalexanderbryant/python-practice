
    def reverse(self):
        llist = self.__reverse_recursive(self.begin)
        llist.next = None
        self.begin, self.tail = self.tail, llist

    def __reverse_recursive(self, curr):
        if curr.next == None:
            return curr
        else:
            node = self.__reverse_recursive(curr.next)
            node.next = curr
            return curr
