import unittest
class Team():
    def __init__(self,cou,gr,nr,points):
        self._cou=cou
        self._gr=gr
        self._nr=nr
        self._points=points

    def getCountry(self):
        return self._cou


    def getGroup(self):
        return self._gr


    def getNumber(self):
        return self._nr


    def getPoints(self):
        return self._points   
    def __str__(self):
        return str(self.getCountry())+" "+str(self.getGroup())+" "+str(self.getNumber())+" "+str(self.getPoints()) 
class Test(unittest.TestCase):
    def testTeam(self):
        t=Team("Romania","A",4,6)
        self.assertEqual(t.getCountry(),"Romania")
        self.assertEqual(t.getGroup(),"A")
        self.assertEqual(t.getNumber(),4)
        self.assertEqual(t.getPoints(),6)