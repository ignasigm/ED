#class Stack
class Stack:
  	“””Define un TDA Pila “””
	def __init__(self):
		self.__items = []
	def __str__(self):
		return ''.join(str(elem)+', '+for elem in self.__items)
	def isEmpty(self):
		return self.__items == []
	def push(self, item): 		
		self.__items.append(item)
	def pop(self):
		return self.__items.pop()
	def peek(self):
	  	if len(self)>0:
	    		return self.__items[len(self)-1]
	  	else: return None
	def __len__(self):
		return len(self.__items)
