
class Queue:
	“””Define un TDA Cola”””
	def __init__(self):        
		self.__data=[]      
	def __str__(self):        
		return ''.join(str(elem)+', ’ for elem in self.__data)                
	def enqueue(self,el):        
		self.__data.append(el)    
	def dequeue(self):      
		return self.__data.pop(0)    
	def isEmpty(self):      
		return self.__data==[]       
	def __len__():        
		return len(self.__data)
