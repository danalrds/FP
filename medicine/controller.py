import unittest
from medicineclass import Medicine
from repository import Repository
class Controller():
    def __init__(self,repo):
        self._repo=repo
    def listall(self):
        return self._repo.getAll()
    def delete(self,name):
        res=self.filterbyname(name)
        if len(res)>0:
            for m in res:
                self._repo.remove(m.getId())                
        else:
            raise ControllerException("There are no elements with this in name!S")
    def filterbyname(self,name):
        res=[]
        for t in self._repo.getAll():
            if name in str(t.getName()):
                res.append(t)
        return res
    
    def increase(self,value,cant):
        res=self.filterbycant(value)
        if len(res)>0:            
            for m in res:
                old=m
                quant=m.getCant()+cant
                new =Medicine(m.getId(),m.getName(),quant)  
                self._repo.update(old,new)  
        else:
            raise ControllerException("There are no medicines with quantity < then the given value!")
    def filterbycant(self,value):
        res=[]
        for t in self._repo.getAll():
            if t.getCant()<value:
                res.append(t)
        return res
class ControllerException(Exception):
    def __init__(self,mesaj):
        self._mesaj=mesaj
    def getMessage(self):
        return self._mesaj
    def __str__(self):
        return str(self._mesaj)


class Test(unittest.TestCase):


    def testName(self):
        pass

