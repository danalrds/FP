import unittest
from repository.OrderRepository import OrderRepository
from repository.DriverRepository import DriverRepository
from domain.classes import Orders
from domain.classes import Driver
class Controller():
    def __init__(self,repo,repod):
        self._repo=repo
        self._repod=repod
    def getAll(self):
        return self._repo.getAll()
    def add(self,id,distance):
        if distance<1:
            raise ControllerException("Distance must be >=1!")
        else:
            if self.find_id(id)!=None:
                order= Orders(id,distance)
                self._repo.store(order)
            else:
                raise ControllerException("Id not found!")
    def find_id(self,id):
        list=self._repod.getAll()
        for l in list:
            if l.getId()==id:
                return l
        return None
    def filterbyid(self,id):
        res=[]
        list=self._repo.getAll()
        for l in list:
            if int(l.getIdDriver())==id:
                res.append(l)
        return res
    def compute(self,id):        
        sum=0
        list=self.filterbyid(id)        
        for l in list:           
            sum=sum+int(l.getKm())
        print(sum)
class ControllerException(Exception):
    def __init__(self,mes):
        self._mes=mes
    def getMessage(self):
        return self._mes
    def __str__(self):
        return str(self._mes)

