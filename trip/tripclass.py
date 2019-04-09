import unittest
from datetime import datetime
class Trip():
    def __init__(self,loc,dep,number):
        self._loc=loc
        self._dep=dep
        self._number=number

    def getLoc(self):
        return self._loc

    def getDep(self):
        return self._dep


    def getNumber(self):
        return self._number


    def setLoc(self, value):
        self._loc = value


    def setDep(self, value):
        self._dep = value


    def setNumber(self, value):
        self._number = value
    def __str__(self):
        return str(self.getLoc())+';'+str(self.getDep())+';'+str(self.getNumber())

class Test(unittest.TestCase):


    def testTrip(self):
        d=datetime.strptime('2017, 12, 3','%Y-%m-%d %H:%M:%S')
        t=Trip("Shanghai",d,800)
        self.assertEqual(t.getLoc(),"Shanghai")
        self.assertEqual(t.getDep(),d)
        self.assertEqual(t.getNumber(),800)
        d=datetime.strptime('2018, 12, 3','%Y-%m-%d %H:%M:%S')
        t.setDep(d)
        t.setLoc("Beyjing")
        t.setNumber(500)
        self.assertEqual(t.getLoc(),"Beyjing")
        self.assertEqual(t.getDep(),d)
        self.assertEqual(t.getNumber(),500)


