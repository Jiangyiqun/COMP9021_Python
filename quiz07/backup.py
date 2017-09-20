# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        index = self.duplicate()
        i = 0   # index of self
        o = 0   # index of odd number
        while index.value_at(i):
            self.delete_value(index.value_at(i))
            if index.value_at(i) % 2:   # if it is odd
                self.insert_value_at(index.value_at(i), o)
                o += 1
            else:                       # if it is even, append on self
                self.append(index.value_at(i))
            i += 1