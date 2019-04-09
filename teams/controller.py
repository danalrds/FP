from copy import deepcopy
import unittest
from repository import Repository
from teamclass import Team

class Controller():
    def __init__(self,repo):
        self._repo=repo
    def filterbygroup(self,group):
        res=[]
        for t in self.getAll():
            if t.getGroup()==group:                
                res.append(t)
        if len(res)>0:
            return res
        else :
            raise ControllerException("Inexistent group!")
    
    def sorter(self):        
        list=self.getAll()
        temp=deepcopy(list)
        temp.sort(key=lambda x:x.getPoints(), reverse=True)
        
        return temp
    def solvematch(self,str):
        d=str.split(" ")
        cou1=d[0]
        cou2=d[1]            
        p1=int(d[2])
        p2=int(d[3])
        find1=self.findbycountry(cou1)
        find2=self.findbycountry(cou2)        
        if (find1!=None) and (find2!=None):
            old1=find1
            old2=find2
            
            if p1==p2:
                new1=Team(old1.getCountry(),old1.getGroup(),old1.getNumber()+1,old1.getPoints()+1)
                new2=Team(old2.getCountry(),old2.getGroup(),old2.getNumber()+1,old2.getPoints()+1)
            elif p1<p2:
                new1=Team(old1.getCountry(),old1.getGroup(),old1.getNumber()+1,old1.getPoints())
                new2=Team(old2.getCountry(),old2.getGroup(),old2.getNumber()+1,old2.getPoints()+2)
            else:
                new1=Team(old1.getCountry(),old1.getGroup(),old1.getNumber()+1,old1.getPoints()+2)
                new2=Team(old2.getCountry(),old2.getGroup(),old2.getNumber()+1,old2.getPoints())
            self._repo.update(old1,new1)
            self._repo.update(old2,new2)
                
        else:
            raise ControllerException("One of the countries is not in the groups!")
    def getAll(self):
        return self._repo.getAll()
    def findbycountry(self,country):
        for t in self._repo.getAll():
            if t.getCountry()==country:
                return t                
        return None      

class ControllerException(Exception):
    def __init__(self,mes):
        self._mes=mes
    def getMessage(self):
        return self._mes
    def __str__(self):
        return str(self._mes)

class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("teams.txt")
        self._control=Controller(self._repo)

    def testName(self):
        list=self._control.getAll()
        res=self._control.filterbygroup("A")
        t2=Team("Spania","A",3,3)
        t=Team("Norvegia","A",3,5)
        t3=Team("Romania","A",4,6)
        
        self.assertEqual(len(res),3)
