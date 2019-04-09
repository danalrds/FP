import unittest
class Driver():
    def __init__(self,id,name):
        self._id=id
        self._name=name

    def getId(self):
        return self._id


    def getName(self):
        return self._name

   
    def __str__(self):
        return str(self.getId())+";"+str(self.getName())
class Orders():
    def __init__(self,idul,km):
        self._idul=idul
        self._km=km
    def getIdDriver(self):
        return self._idul
    
    def getKm(self):
        return self._km

    def __str__(self):
        return str(self.getIdDriver())+";"+str(self.getKm())
class Test(unittest.TestCase):

    def testDriver(self):
       d=Driver(1,"Alex")
       self.assertEqual(d.getId(),1)
       self.assertEqual(d.getName(),"Alex")
       d=Driver(2,"Max")
       self.assertEqual(d.getId(),2)
       self.assertEqual(d.getName(),"Max")
    
    def testOrder(self):
        
        order=Orders(1,18)
        self.assertEqual(order.getIdDriver(),1)
        
        self.assertEqual(order.getKm(),18)
       
       