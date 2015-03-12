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
		
class Queue:
	“””Define un TDA Cola”””
	def __init__(self):        
		self.__data=[]      
	def __str__(self):        
		return ''.join(str(elem)+','+for elem in self._data)                
	def enqueue(self,el):        
		self.__data.append(el)    
	def dequeue(self):      
		return self.__data.pop(0)    
	def isEmpty(self):      
		return self.__data==[]       
	def __len__():        
		return len(self.__data)
		
class PriorityQueue:
  """ Cola de prioridad, hereda de una cola pero inserta los elementos en orden, por defecto ascendiente"""        

	def __init__(self):        
		Queue.__init__(self)          
  
	def enqueue(self,el):        
		if self.isEmpty(): self.insert(0,el)        
		elif el<=self.__getitem__(0): self.insert(0,el)        
		else:               
			inserted,i=False,0              
		  	while i< (len(self)-1) and not(inserted):                
		    		if self.__getitem__(i)<el and el<=self.__getitem__(i+1): 
			    		self.insert(i+1,el)
			    		inserted=True  
		    		i=i+1              
		  	if not(inserted):  self.insert(len(self),el)
