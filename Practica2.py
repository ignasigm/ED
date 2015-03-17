#class Stack
class Stack:
	def __init__(self):
		self.__items = []
	def __str__(self):
		return ''.join(str(elem)+', '
		               for elem in self.__items)
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
	print "\ntestStack"
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
	
	def __init__(self):        
		self.__data=[]      
	def __str__(self):        
		return ''.join(str(elem)+','
		               for elem in self.__data)                
	def enqueue(self,el):        
		self.__data.append(el)    
	def dequeue(self):      
		return self.__data.pop(0)    
	def isEmpty(self):      
		return self.__data==[]       
	def __len__(self):   
		return len(self.__data)
	def insert(self, num, el):
		self.__data.insert(num, el)
	def __getitem__(self, num):
		return self.__data[num]
def testQueue():
	print "\ntestQueue"
	llista_q = Queue()
	print "Esta buida: ",llista_q.isEmpty()
	llista_q.enqueue(1)
	llista_q.enqueue(2)
	llista_q.enqueue(3)
	print "Esta buida: ", llista_q.isEmpty()
	print "Mida: ",len(llista_q)
	print "Tota la llista: ",llista_q
	llista_q.dequeue()
	print "Mida: ",len(llista_q)
	print "Element tret: ",llista_q.dequeue()
	print "Tota la llista: ",llista_q
	

class PriorityQueue(Queue):
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
	print "\ntestPQueue"
	llista_qr = PriorityQueue()
	print "Esta buida: ",llista_qr.isEmpty()
	llista_qr.enqueue(3)
	llista_qr.enqueue(1)
	llista_qr.enqueue(2)
	print "Esta buida: ", llista_qr.isEmpty()
	print "Mida: ",len(llista_qr)
	print "Tota la llista: ",llista_qr
	llista_qr.dequeue()
	print "Mida: ",len(llista_qr)
	print "Element tret: ",llista_qr.dequeue()
	print "Tota la llista: ",llista_qr
	
	
'''CARD'''
class Card:
    def __init__(self, color, number):
        #constructor on iniciem els dos atributs(privats)
        self.__color = color
        self.__number = number
    def getColor(self):
        #canvia el color
        return self.__color
    def getNumber(self):
        #retorna el nombre
        return self.__number
    def setColor(self, color):
        #defineix color
        self.__color = color
    def setNumber(self, number):
        #defineix nombre
        self.__number = number
    def tellMeColor(self):
        #converteix l'int del nombre en color escrit
        dic = {0: "blue", 1: "green", 2: "red", 3: "yellow"}
        return dic[self.getColor()]        
    def __str__(self):
        #sobrecarrega del print (imprimeix una carta de la forma: nombre-color)
        #retorna un string on s'hi especifica nombre i color
        return str(self.getNumber())+"-"+str(self.tellMeColor())
    def check_card(self, other):
        #comprova si dos cartes son compatibles
        if self.getColor() == other.getColor() or self.getNumber()== other.getNumber():
            return True
        else:
            return False
            

'''falta acabar'''            
class Deck(Queue):
    def __init__(self):            
        Queue.__init__(self)
        for i in range(10):
            for j in range(4):
                self.enqueue(Card(j, i)) 
    def __getitem__(self,i):
        return self[i]
    def remove(self,i):
        self.remove(i)
    def deal_one_card(self,card):
        i = random.randint(0,len(self)-1)
        card = self.__getitem__(i)
        self.remove(i)
        return card
        
def testDeck():
    print "\nTest Deck"
    llista = Deck()
    print llista
    llista.deal_one_card(Card(2,3))
'''fins aqui'''


class Discard_Pile(Stack):
    def __init__(self):
        Stack.__init__(self)
        #afegir una carta aleatoria de deck, per emntrestant me l'invento
        self.push(Card(2,5))
        
def testDiscard_Pile():
    print "\nTest Discard Pile"
    print "Creacio de la Discard Pile:"
    llista = Discard_Pile()
    print "Veure si la llista esta buida:"
    print llista.isEmpty()
    print "Quants elements te?"
    print len(llista)
    print "Mostrar Discard Pile:",llista.__str__()
    print "Afegim unes quantes cartes"
    llista.push(Card(1,5))
    llista.push(Card(0,9))
    llista.push(Card(3,2))
    print "Ara te",len(llista),"elements"
    print "Es la seguent llista:",llista
    print "Mostrar la carta visible, que es exactament la ultima que s'ha afegit"
    print llista.peek()
    print "Eliminem la carta visible"
    print "Carta borrada:",llista.pop()
    print "Veure de nou la llista:",llista	
	
	
testStack()
testQueue()
testPriorityQueue()
testDeck()   
testDiscard_Pile()
