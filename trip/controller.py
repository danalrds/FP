from repository import Repository
from tripclass import Trip
import unittest
from datetime import datetime,timedelta
class Controller():
    def __init__(self,repo):
        self._repo=repo
    def listall(self):
        return self._repo.getAll()
    def amana(self,value):
        res=self.filterbynumber(value)
        for t in res:
            old=t
            date=t.getDep()
            date += timedelta(days=1)           
            new=Trip(t.getLoc(),date,t.getNumber())
            self._repo.update(old,new)
    def filterbynumber(self,number):
        res=[]
        for t in self._repo.getAll():
            if t.getNumber()<number:
                res.append(t)
        return res
class ControllerException(Exception):
    def __init__(self,mes):
        self._mes==mes
    def getMessage(self):
        return self._mes
    def __str__(self):
        return str(self.mes)
class Test(unittest.TestCase):


    def testName(self):
        pass

