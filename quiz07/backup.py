# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
       super().__init__(L)

    def rearrange(self):
        index = self.duplicate()
        even = LinkedList()
        odd = LinkedList()
        i = 0   # index of self
        while index.value_at(i) is not None:
            self.delete_value(index.value_at(i))
            if index.value_at(i) % 2:   # if it is odd
               odd.append(index.value_at(i))
            else:                       # if it is even
               even.append(index.value_at(i))
            i += 1
        self.extend(odd)
        self.extend(even)