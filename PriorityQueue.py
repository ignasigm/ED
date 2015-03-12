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
