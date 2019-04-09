from classes import Coffee
from repository import Repository
from copy import deepcopy
class Controller():
    def __init__(self,repo):
        self._repo=repo
    def getAll(self):
        return self._repo.getAll()
    def filterbycountry(self,country,price):
        rezults=[]
        for t in self.getAll():
            if t.getCountry()==country:
                if t.getPrice()<price:
                    rezults.append(t)
        for r in rezults:
            print(str(r)) 
    def sort(self):
        list=self.getAll()
        cafele=deepcopy(list)
        cafele.sort(key=lambda x:(x.getCountry(),-x.getPrice()))
        for c in cafele:
            print(str(c))
    
            