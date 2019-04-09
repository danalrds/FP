import unittest
class Car():
    def __init__(self,id,mark,price):
        self._id=id
        self._mark=mark
        self._price=price

    def getId(self):
        return self._id


    def getMark(self):
        return self._mark


    def getPrice(self):
        return self._price
    
    def setPrice(self, value):
        self._price = value  

    def __str__(self):
        return str(self.getId())+";"+str(self.getMark())+";"+str(self.getPrice())
    

class Test(unittest.TestCase):


    def testCar(self):
       c=Car(1,"Audi",1000)
       self.assertEqual(c.getId(),1)
       self.assertEqual(c.getMark(),"Audi")
       self.assertEqual(c.getPrice(),1000)