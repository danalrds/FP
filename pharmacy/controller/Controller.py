import unittest
from domain.medicineclass import Medicine
from domain.medicineclass import Receipe
from repository.MedicineRepository import Repository
class Controller():
    def __init__(self,repo):
        self._repo=repo
    def lookup(self,name):
        res=self._repo.findbyname(name)
        return res 
    def findbyname(self,name):
        for t in self._repo.getAll():
            if t.getName()==name:
                return t
        return None
    def createreceipe(self,list):
        res=[]
        for i in list:
            obj=self.findbyname(i)
            if obj!=None: 
                res.append(obj)
        reteta=Receipe(res) 
        price=reteta.getTotalPrice()
        return res
        
    def createreceipe2(self,list):
        res=[]
        for i in list:
            obj=self.findbyname(i)
            if obj!=None: 
                res.append(obj)
        reteta=Receipe(res) 
        price=reteta.getTotalPrice()
        
        return price
class ControllerException(Exception):
    def __init__(self,mes):
        self._mes=mes
    def getMessage(self):
        return self._mes
    def __str__(self):
        return str(self._mes)
   
class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("pharmacy.txt")
        self._control=Controller(self._repo)
    def testul(self):
        m=Medicine("Nurofen 500",60)
        self._repo.store(m)
        list=self._repo.getAll()
        self.assertEqual(list,[m])
        m2=Medicine("Paracetamol 500",60)
        self._repo.store(m2)
        list=self._repo.getAll()
        self.assertEqual(list,[m,m2])
        list=self._repo.findbyname("rof")
        self.assertEqual(list,[m])