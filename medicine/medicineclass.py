import unittest
from ctypes.test.test_pickling import name
class Medicine():
    def __init__(self,id,name,cant):
        self._id=id
        self._name=name
        self._cant=cant

    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    def getCant(self):
        return self._cant
    def __str__(self):
        return str(self.getId())+";"+str(self.getName())+";"+str(self.getCant())  

class Test(unittest.TestCase):
    def testMedicine(self):
        m=Medicine(12,"Paracetamol",452)
        self.assertEqual(m.getId(),12)
        self.assertEqual(m.getName(),"Paracetamol")
        self.assertEqual(m.getCant(),452) 
        m=Medicine(13,"Nurofen",30)
        self.assertEqual(m.getId(),13)
        self.assertEqual(m.getName(),"Nurofen")
        self.assertEqual(m.getCant(),30) 