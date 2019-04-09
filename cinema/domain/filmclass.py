import unittest
class Film():
    def __init__(self,id,name,price,places):
        self._id=id
        self._name=name
        self._price=price
        self._places=places

    def getId(self):
        return self._id


    def getName(self):
        return self._name


    def getPrice(self):
        return self._price


    def getPlaces(self):
        return self._places

    def __str__(self):
        return str(self.getId())+";"+str(self.getName())+";"+str(self.getPrice())+";"+str(self.getPlaces())
class Test(unittest.TestCase):

    def testFilm(self):
       f=Film(2,"Bolonia",20,91)
       self.assertEqual(f.getId(),2)
       self.assertEqual(f.getName(),"Bolonia")
       self.assertEqual(f.getPrice(),20)
       self.assertEqual(f.getPlaces(),91)
       