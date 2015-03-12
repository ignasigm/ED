#EXERCICI 1


class Time:
    def __init__(self, hour=0, minute=0, second=0): #coincidencia de los nombres
        self.hour = hour # define los atributos de la clase
        self.minute = minute
        self.second = second
    #getters i setters (hour minute second)
    def getHour(self):
        return self.hour
    
    def setHour(self,hour):
        self.hour=hour  
        
    def getMinute(self):
        return self.minute
            
    def setMinute(self,minute):
        self.minute=minute 
            
    def getSecond(self):
        return self.second
            
    def setSecond(self,second):
        self.second=second        
        
    def print_time(time): # funcion global
        print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)
        
    def int_to_time(self,second):
        #funcio que converteix els segons a hores,minuts,segons
        self.hour = second/3600
        self.minute = (second-3600*self.hour)/60
        self.second =  second-3600*self.hour-60*self.minute        
        
    def increment(self, seconds): #metodo de la clase
        #suma l'hora (passada a segons) i els segons entrats per paramentre
        seconds += self.time_to_int()
        #llamamos los metodos de la clase con self
        #retorna l'hora de la suma anterior
        return self.int_to_time(seconds)        
                   
    def time_to_int(self):
        #passa hores,segons i minuts a un int segons
        self.minutes = self.hour * 60 + self.minute
        self.seconds = self.minutes * 60 + self.second
        # recuperamos los datos del objeto con self
        return self.seconds
            
    def is_after(self, other):
        #compara dos temps
        return self.time_to_int() > other.time_to_int()
    
    def add_time(t1, t2): #t1, t2 objetos de tipo Time
        #suma dos hores
        sum = Time()
        sum.hour = t1.hour + t2.hour
        sum.minute = t1.minute + t2.minute
        sum.second = t1.second + t2.second
        if sum.second >= 60:
            sum.second -= 60
            sum.minute += 1
        if sum.minute >= 60:
            sum.minute -= 60
            sum.hour += 1
        return sum
    
def ej1():
    print "Exercici 1:"
    #creacio de t1 i t2 i imprimir
    t1=Time(22,15,55)
    t1.print_time()
    t2=Time(1,22,34)
    t2.print_time()
    #imprimir l'hora que resulta de sumar t1 i t2
    t1.add_time(t2).print_time()
    #incrementar t1 1000segons
    t1.increment(1000)
    t1.print_time()
    print ""
    


#EXERCICI 2

def estadisticaFormulaUno(lista,h,m,s):
    #contador es el iterador
    contador = 0
    #numero es el nombre de pilots de compleixen les condicions
    numero = 0 
    #creacio del temps limits a partir dels parametres entrats
    limit = Time(h,m,s)
    #per cada elements de la llista si limit.is_after(lista[contador]) es True aleshores el pilot ho compleix
    while contador<len(lista):
        if limit.is_after(lista[contador]):
            numero+=1 
        contador+=1
    return numero
    

def ej2(h=1,m=40,s=0):
    #llista dels temps
    lista=[Time(1,38,26),Time(1,39,16),Time(1,39,7),Time(1,39,55), Time(1,39,54),Time(1,40,9),Time(1,40,11), Time(1,40,51), Time(1,40,05), Time(1,40,38), Time(1,40,55), Time(1,40,56),Time(1,40,55), Time(1,41,46), Time(1,41,52), Time(1,41,15), Time(1,42,36), Time(1,43, 9), Time(1,43,5),Time(1,44,37)]
    print "Exercici 2:"
    #aplicat la funcio estadisticaFormulaUno a la llista de temps
    print "El numero de deportistas con tiempo menor es: " + str(estadisticaFormulaUno (lista, h,m,s))
    
    
"""TESTS"""
    
    
ej1()
    
ej2(1,41)
