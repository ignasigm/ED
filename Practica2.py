import random
#class Stack
CONSTANT_CARTES = 7
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
	def pop(self, num):
		return self.__data.pop(num)
	def getIndex(self, el):
		return self.__data.index(el)

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

'''PLAYER'''
class Player(PriorityQueue):
    def __init__(self, nom, deck, maxcartes):
    	PriorityQueue.__init__(self)
        self.__name = nom
        i = 0
        while i < maxcartes:
            self.enqueue(deck.dequeue)
            i+=1
    def getName(self):
	#retorna el nom del jugador
	return self.__name
    def __str__(self):
	#funcio que imprimeix la informacio del player(nom i cartes)
	resultat = "Nom: "+self.getName()+"\nCartes: "+str(self)
	return resultat
	
    	
    def select_card(self,number):
	#funcio que selecciona la carta amb un numero corresponent introduit
	i=0
	possible = False
	#mentre l'index sigui menor que la longitud i True
	while i<self.len() and not possible:
	    possible = number == self.getitem(i).getNumber()		    
	    i+=1
	#si possible es True aleshores es que es pot i retorna la carta de la posicio que ho ha trobat
	if possible:
	    return self.getitem(i)
	else:
		return None
    def can_play_card(self,card):
	#funcio que retorna true si els jugador te una carta que pot jugar i false si no te cap carta bona segons les normes
	i=0
	possible = False
	while i<self.len() and not possible:
	    possible = self.getitem(i).check_card(card)		    
	    i+=1
	#si surt del while abans es que ho ha trobat i per tant True
	return possible
    def play_a_card(self,card, discard_pile):
	#funcio que retorna la carta i elimina de la llista de cartes del jugador
	#afegeix a discard_pile
	discard_pile.append(self.pop(self.getIndex(card)))

	
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
            

'''DECK'''            
class Deck(Queue):
    def __init__(self):
        cards = []            
        Queue.__init__(self)
        for i in range(10):
            for j in range(4):
                cards.append(Card(j, i))
        random.shuffle(cards)
        for i in cards:
            self.enqueue(i)
        
def testDeck():
    print "\n\nTestDeck"
    deck = Deck()
    card1 = deck.dequeue()
    card2 = deck.dequeue()
    print "La carta numero 5 es: ",card1
    print "Una carta a l'atzar es: ",card2
    print "Son compatibles: ",card1.check_card(card2)
    for i in range(5):
        print "Reparteixo ",
        print deck.dequeue()


class Discard_Pile(Stack):
    def __init__(self, deck):
        Stack.__init__(self)
        #afegir una carta aleatoria de deck
        self.append(deck.dequeue())
    def append(self, card):
		#funcio que afegeix al final de la discard_pile la carta card
		self.push(card)

        
def testDiscard_Pile():
    deck = Deck()
    print "\nTest Discard Pile"
    print "Creacio de la Discard Pile:"
    llista = Discard_Pile(deck)
    print "Veure si la llista esta buida:"
    print llista.isEmpty()
    print "Quants elements te?"
    print len(llista)
    print "Mostrar Discard Pile:",llista
    print "Afegim unes quantes cartes"
    llista.append(Card(1,5))
    llista.append(Card(0,9))
    llista.append(Card(3,2))
    print "Ara te",len(llista),"elements"
    print "Es la seguent llista:",llista
    print "Mostrar la carta visible, que es exactament la ultima que s'ha afegit"
    print llista.peek()
    print "Eliminem la carta visible"
    print "Carta borrada:",llista.pop()
    print "Veure de nou la llista:",llista	
	




class One:      
      __jugadors = []
      __baralla = []
      __pila = []
      __moment = 0
      __numplayer = 0
      def __init__(self):
		self.prepare_game()
		self.run_game()
		
      def prepare_game(self):
		self.__baralla = Deck()
		self.__num_player = input("Introdueix el nombre de jugadors_\n")
		for i in range(self.__numplayer):
			nom = raw_input("\nIntrodueix nom del jugador"+str(i+1)+"\n") 
			self.__jugadors.append(Player(nom,self.__baralla,CONSTANT_CARTES))
		self.__pila = Discard_Pile(self.__baralla)
		self.__moment = random.randint(0, self.__num_player)
      def stop_criterion(self):
		i=0
		while i<len(self.__jugadors) and self.__jugadors[i]!=0:
			i=i+1
		if i<len(self.__jugadors):
			return True
		else:
			return False
		
      def announce_champion(self):
	 	i=0
		while self.__jugadors[i]!=0:
			i+=1
		print self.__jugadors[i]
		
      def visualize_state(self,pila,jugadors):
		return "Pila:"+str(pila.peek())+"\nCartes jugador actual:"+str(self.__jugadors[self.__moment])
      def getJugador(self):
		return self.__jugadors[self.__moment]
      def change_turn(self):
          if self.__moment<self.__numplayer:
              self.__moment+=1
          else:
              self.__moment-=self.__numplayer
      def run_game(self):
            while not self.stop_criterion():
                print self.visualize_state(self.__pila, self.__jugadors)
            while not self.getJugador().can_play_card():
                self.getJugador().enqueue(self.__baralla.dequeue())
            while self.getJugador().can_play_card():
                
                carta_sel = self.getJugador().select_card(input("Introdueix el numero de la carta que vols tirar:\n"))
                if carta_sel.check_card(self.__pila.peek()):
                    self.getJugador.pop(carta_sel)
                    self.__pila.enqueue(carta_sel)
                else:
                    print "Incorrecte"
                    self.change_turn()
	
one = One()
one.run_game()
