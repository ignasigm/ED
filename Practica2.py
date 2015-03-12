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
		

def testStack():
	llista_s = Stack()
	print "Esta buida: ",llista_s.isEmpty()
	llista_s.push(1)
	llista_s.push(2)
	llista_s.push(3)
	print "Esta buida: ", llista_s.isEmpty()
	print "Mida: ",len(llista_s)
	print "Tota la llista: ",llista_s
	llista_s.peek()
	print "Mida: ",len(llista_s)
	print "Element tret: ",llista_s.pop()
	print "Tota la llista: ",llista_s
	

		
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
		
def testQueue():
	llista_q = Queue()
	print "Esta buida: ",llista_q.isEmpty()
	llista_q.enqueue(1)
	llista_q.enqueue(2)
	llista_q.enqueue(3)
	print "Esta buida: ", llista_q.isEmpty()
	print "Mida: ",len(llista_q)
	print "Tota la llista: ",llista_q
	llista_q.peek()
	print "Mida: ",len(llista_q)
	print "Element tret: ",llista_q.dequeue()
	print "Tota la llista: ",llista_q
	

class PriorityQueue(Queue):
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
def testPriorityQueue():
	llista_qr = PriorityQueue()
	print "Esta buida: ",llista_qr.isEmpty()
	llista_qr.enqueue(3)
	llista_qr.enqueue(1)
	llista_qr.enqueue(2)
	print "Esta buida: ", llista_qr.isEmpty()
	print "Mida: ",len(llista_qr)
	print "Tota la llista: ",llista_qr
	llista_qr.peek()
	print "Mida: ",len(llista_qr)
	print "Element tret: ",llista_qr.dequeue()
	print "Tota la llista: ",llista_qr
testStack()
testQueue()
testPriorityQueue()
