import unittest
class Client:
    def __init__(self,id,name):
        self._id=id
        self._name=name
    def getId(self):
        return self._id
    def getName(self):
        return self._name
    def setName(self,name):
        self._name=name
    def __str__(self):
        return "id: "+str(self.getId())+" "+"name: "+str(self.getName()) 
class testClient(unittest.TestCase):
    def testclient(self):
        c=Client(4,"Naomi")
        self.assertEqual(c.getId(),4)
        self.assertEqual(c.getName(),"Naomi")
        c.setName("Riccina")
        self.assertEqual(c.getName(),"Riccina")
        self.assertEqual(c.__str__(),"id: 4 name: Riccina")