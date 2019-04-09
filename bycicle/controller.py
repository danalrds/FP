from bycicleclass import Bycicle
from repository import Repository
class Controller():
    def __init__(self,repo):
        self._repo=repo
    def listall(self):
        return self._repo.getAll()
    def reduceprice(self,type,percent):
        res=self.filterbytype(type)
        if len(res)>0:
            for b in res:
                old=b
                new=Bycicle(b.getId(),type,b.getPrice()-percent*b.getPrice())
                self._repo.update(old,new)
                
        else:
            raise ControllerException("Type not found!")
    def filterbytype(self,type):
        res=[]
        for b in self._repo.getAll():
            if b.getType()==type:
                   res.append(b)
        return res
class ControllerException(Exception):
    def __init__(self,mesaj):
        self._mesaj=mesaj
    def getMessage(self):
        return self._mesaj
    def __str__(self):
        return str(self._mesaj)