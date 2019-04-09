from domain.classes import Orders
from domain.classes import Driver
import unittest

class OrderRepository():
    def __init__(self,fname):
        self._objects=[]
        self._fname=fname
        self.__loadfromfile()
    def __loadfromfile(self):
        try:
            f=open(self._fname,'r')
            line=f.readline().strip()
            while line!='':
                d=line.split(";")
                order=Orders(d[0],d[1])
                self.store(order)
                line=f.readline().strip()
        except EOFError:
            raise RepositoryException("Something went wrong!")
    def store(self,object):
        self._objects.append(object)
        self.__storetofile()
    def getAll(self):
        return self._objects
    def __storetofile(self):
        f=open(self._fname,'w')
        for obj in self.getAll():
            f.write(str(obj))
            f.write("\n")
    
class RepositoryException(Exception):
    def __init__(self,mes):
        self._mes=mes
    def getMessage(self):
        return self._mes
    def __str__(self):
        return str(self._mes)

class Test(unittest.TestCase):
    def setUp(self):
        self._repo=OrderRepository("orders.txt")
    def testRepo(self):
     
       order=Orders(1,18) 
       self._repo.store(order)
       list=self._repo.getAll()
       self.assertEqual(list,[order])
       