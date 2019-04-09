'''
Created on Nov 19, 2016

@author: Imi
'''
from datetime import *
from domain.idObjcen import IdObject
from domain.validatorEXception import ValidatorException
class Rental(IdObject):
    def __init__(self,objId,movie,client,rentDate,dueDate,returnDate):
        '''
        every rental object will have a unique id, but will also contain the
        id of client who has rented the movie, whose id is also contained, the following
        fields are for storing the date of rental and the due date
        '''
        IdObject.__init__(self, objId)
        self._movie=movie
        self._client=client
        self._rentDate=rentDate
        self._dueDate=dueDate
        self._returnDate=returnDate
    '''
    getters and setters for specified fields
    '''
    def getMovie(self):
        return self._movie
    
    def setMovie(self,movie):
        self._movie=movie
    
    def getClient(self):
        return self._client
    
    def setClient(self,client):
        self._client=client
    
    def getRentDate(self):
        return self._rentDate
    
    def setRentDate(self,rentDate):
        self._rentDate=rentDate
    
    def getDueDate(self):
        return self._dueDate
    
    def setDueDate(self,dueDate):
        self._dueDate=dueDate
    
    def getReturnDate(self):
        return self._returnDate
    
    def setReturnDate(self,returnDate):
        self._returnDate=returnDate
    def __len__(self): 
        l=(self._dueDate-self._rentDate).days+1
        if l<0:
            l=0
        return l
    def __str__(self):
        '''
        override str method
        the string representation will contain if the movie is returned or it passed the de date
        '''
        s=''
        s+='rental:'+str(self.getId())+'\n movie: '+str(self.getMovie())+'\n client:'+str(self.getClient())+"\n Period: " + self._rentDate.strftime("%Y-%m-%d") + " to " + self._dueDate.strftime("%Y-%m-%d")
        if self.getReturnDate()!=None:
            s+='\n returned on '+str(self.getReturnDate())
        return s
    def __lt__(self,o):
        return len(self)>len(o)
    def __repr__(self):
        return str(self)
class RentalValidator():
    '''
    validator class for rental objects
    this allows us to check if a rental's data is or not correct
    '''
    
    def validate(self, rental):
        if isinstance(rental, Rental) == False:
            raise TypeError("Not a Rental")
        _errorList = []
        now = datetime.now()
        if rental.getRentDate() < now:
            _errorList.append("Rental can't start in past \n")
        if len(rental) <= 1:
            _errorList.append("Rental must be at least 1 day\n")
        if len(_errorList) > 0:
            raise ValidatorException(_errorList)
#id=int(input('enter id'))
#id2=int(input('enter movie id'))
#id3=int(input('enter client id'))
#date1=input('enter rent date')
#date2=input('enter due date')
#d1=datetime.strptime(date1, '%Y, %m, %d')
#d2=datetime.strptime(date2, '%Y, %m, %d')
#rent=Rental(id,id2,id3,d1,d2,None)
#print(rent.getReturnDate())