import unittest
from bubblesort import list
class Medicine():
    def __init__(self,name,price):
        self._name=name
        self._price=price

    def getName(self):
        return self._name


    def getPrice(self):
        return self._price
    def __str__(self):
        return str(self.getName())+","+str(self.getPrice())

class Receipe():
    def __init__(self,list):
        self._list=list
    def getList(self):
        return self._list
    def getTotalPrice(self):
        sum=0
        for l in self._list:           
            sum+=l.getPrice()
        return sum
    
class Test(unittest.TestCase):


    def testMedicine(self):
        m=Medicine("Nurofen 500",60)
        self.assertEqual(m.getName(),"Nurofen 500")
        self.assertEqual(m.getPrice(),60)
        m=Medicine("Paracetamol 500",100)
        self.assertEqual(m.getName(),"Paracetamol 500")
        self.assertEqual(m.getPrice(),100)
