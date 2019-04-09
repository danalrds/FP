import unittest
class Bycicle():
    def __init__(self,id,type,price):
        self._id=id
        self._type=type
        self._price=price

    def getId(self):
        return self._id


    def getType(self):
        return self._type


    def getPrice(self):
        return self._price  


    def setPrice(self, value):
        self._price = value  

    def __str__(self):
        return str(self.getId())+';'+str(self.getType())+';'+str(self.getPrice())
class Test(unittest.TestCase):
    def testbycicle(self):
        b=Bycicle(34,"Pegas",199)
        self.assertEqual(b.getId(),34)
        self.assertEqual(b.getType(),"Pegas")
        self.assertEqual(b.getPrice(),199)
        b.setPrice(700)
        self.assertEqual(b.getPrice(),700)
        self.assertEqual(b.__str__(),"34;Pegas;700")
