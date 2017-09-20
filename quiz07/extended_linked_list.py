# Written by Sarika Azad(5172690) for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        pass
        # Replace pass above with your code

    def remove_duplicates(self):
        if not self.head:
            return
        x_node = self.head
        while x_node:
            node = x_node
            while node.next_node:
                if node.next_node.value == x_node.value:
                    node.next_node = node.next_node.next_node
                else:
                    node = node.next_node
            x_node = x_node.next_node
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()