import unittest
from copy import deepcopy
from repository.FilmRepository import Repository
from domain.filmclass import Film
class Controller():
    def __init__(self,repo):
        self._repo=repo
    def add(self,id,name,price,places):
        f=Film(id,name,price,places)
        self._repo.store(f)
    def getAll(self):
        return self._repo.getAll()    
    def reduce(self,pretul):
        res=[]
        for obj in self._repo.getAll():
            if obj.getPrice()>=pretul:
                res.append(obj)
        for t in res:
            old=t
            pret=t.getPrice()-t.getPrice()*25/100
            new=Film(t.getId(),t.getName(),pret,t.getPlaces())
            self._repo.update(old,new)
    def afisaremedia(self):
        res=[]
        s=0
        c=0
        for object in self._repo.getAll():
            s=s+object.getPlaces()
            c=c+1
        media=s/c
        for object in self._repo.getAll():
            if float(object.getPlaces())>media:
                res.append(object)
        return res
    def sorter(self,name,criteriu):
        res=self.filterbyname(name)
        temp=deepcopy(res)
        if criteriu=="1":
            ok=True
            while ok==True:
                ok=False
                for i in range(0,len(temp)-1):
                    if temp[i].getPlaces()* temp[i].getPrice()> temp[i+1].getPlaces()* temp[i+1].getPrice():
                        temp[i],temp[i+1]=temp[i+1],temp[i]
                        ok=True
            return temp
        elif criteriu=="2":
            temp.sort(key=lambda x:x.getPrice()*x.getName(), reverse=False)
            return temp
        else:
            raise ControllerException("This is not a valid criteria!")
        
    def filterbyname(self,name):
        res=[]
        for t in self._repo.getAll():
            if name in t.getName():
                res.append(t)
        return res
class ControllerException(Exception):
    def __init__(self,mes):
        self._mes=mes
    def getMessage(self):
        return self._mes
    def __str__(self):
        return str(self._mes)

class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("filme.txt")
        self._control=Controller(self._repo)

    def testRepo(self):
        f=Film(2,"Bolonia",20,91)
        self._repo.store(f)
        list=self._repo.getAll()
        self.assertEqual(list,[f])
        
