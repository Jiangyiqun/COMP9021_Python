# Written by Sarika Azad(5172690) for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
	def __init__(self, L = None):
		super().__init__(L)
		
	def rearrange(self):
		value_1 = self.head.value
		value_2 = self.head.next_node.value
		if value_2 % 2 == 1 and value_1 % 2 ==0:
			node = self.head.next_node 
			next_node = node.next_node
			node.next_node = self.head
			self.head = node
			node.next_node.next_node = next_node
		
		try:
			while True:
				node = self.head
				counter=len(self)-1
				for i in range(1,len(self)):
					try:
						n1 = node.next_node
						value_1 = n1.value
						n2 = n1.next_node
						value_2 = n2.value
						n1 = node.next_node
						value_1 = n1.value
					except AttributeError:
						value_2 = None
						value_1 = None
						
					try:
						n3 = n2.next_node
					except AttributeError:	
						value_3 = None
					if value_1 and value_2 and value_2 % 2 == 1 and value_1 % 2 ==0:
						if value_2 != None:
							n2.next_node = None
							n1.next_node = n3
						node.next_node = n2
						n2.next_node = n1
						counter+= -1
					node = node.next_node				
				if counter == len(self)-1:
					raise ValueError
		except ValueError:
			pass
		return self
	