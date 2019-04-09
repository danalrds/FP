from classes import Bear
from repository import Repository

class Controller():
    def __init__(self,repo):
        self._repo=repo
    def getAll(self):
        return self._repo.getAll()
    def update(self,old,new):
        self._repo.update(old,new)
    def list(self):
        for t in self.getAll():
            print(str(t))
    def updateprice(self,name,procent):
        
        for t in self.getAll():
            if t.getName()==name:
                old=t
                newprice=t.getPrice()-procent*t.getPrice()
                new=Bear(t.getName(),t.getType(),float(newprice))
                self.update(old, new)
    def minim(self,name):
        min=99999
        for t in self.getAll():
            if t.getName()==name:
                if t.getPrice()<min:
                    min=t.getPrice()
        return min
    def updatebytype(self,tip):
        for t in self.getAll():
            if t.getType()==tip:
                min=self.minim(t.getName())
                old=t
                newprice=float(min)
                new=Bear(t.getName(),t.getType(),float(newprice))
                self.update(old, new)