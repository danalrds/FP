from datetime import datetime
from domain.clientclass import Client
from domain.bookclass import Book
import unittest
class Rental:
    def __init__(self,id,book,client,rentdate,duedate,returndate):
        self._id=id
        self._book=book
        self._client=client
        self._rentdate=rentdate
        self._duedate=duedate
        self._returndate=returndate
    def getId(self):
        return self._id
    def getBook(self):
        return self._book
    def getClient(self):
        return self._client
    def getRentdate(self):
        return self._rentdate
    def getDuedate(self):
        return self._duedate
    def getReturndate(self):
        return self._returndate
    
    def setBook(self,book):
        self._book=book
    def setClient(self,client):
        self._client=client
    def setRentdate(self,rentdate):
        self._rentdate=rentdate
    def setDuedate(self,duedate):
        self._duedate=duedate
    def setReturndate(self,returndate):
        self._returndate=returndate
    
    def __str__(self):
        s=''        
        s+="rental: "+str(self.getId())+"book: "+str(self.getBook())+"\n client: "+str(self.getClient())+"\n rentdate: "+str(self.getRentdate())+" duedate: "+str(self.getDuedate())
        if self.getReturndate()!=None:
             s+="\n returned on: "+str(self.getReturndate())
             
    def __len__(self): 
        l=(self._duedate-self._rentdate).days+1
        if l<0:
            l=0
        return l
class testRental(unittest.TestCase):
    def testrental(self):
        c=Client(1,"Yanna")
        b=Book(1,"Avangarde","Robinson")
        d1 = datetime.strptime('2017, 12, 7', '%Y, %m, %d')
        d2 = datetime.strptime('2017, 12, 30', '%Y, %m, %d')
        r=Rental(1,b,c,d1,d2,None)
        self.assertEqual(r.getId(),1)
        self.assertEqual(r.getBook(),b)
        b=Book(1,"Avangarde2","Robinson2")
        r.setBook(b)
        self.assertEqual(r.getBook(),b)
        