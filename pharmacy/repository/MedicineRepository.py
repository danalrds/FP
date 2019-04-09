import unittest
from domain.medicineclass import Medicine
class Repository():
    def __init__(self,fname):
        self._objects=[]
        self._fname=fname
        self.__loadfromfile()
    def __loadfromfile(self):
        try:
            f=open(self._fname,"r")
            line=f.readline().strip()
            while line!='':
                d=line.split(',')
                object=Medicine(d[0],int(d[1]))
                self.store(object)
                line=f.readline().strip()
        except EOFError:
            raise RepositoryException("Something went wrong!") 
        finally:
            f.close()
    def store(self,object):
        if self.find(object)==None:
            self._objects.append(object)
        self.__storetofile()
    def getAll(self):
        return self._objects
    def __storetofile(self):
        f=open(self._fname,'w')
        for t in self.getAll():
            f.write(str(t))
            f.write("\n")
        f.close()
    def findbyname(self,name):
        res=[]
        name=name.lower()       
        for t in self.getAll():
            if name in str(t.getName()):
                res.append(t)
        return res
    def find(self,obj):
        res=None
        for e in self.getAll():
            if e==obj:
                res=obj
        return res    
class RepositoryException(Exception):
    def __init__(self,mes):
        self._mes=mes
    def getMessage(self):
        return self._mes
    def __str__(self):
        return str(self._mes)
class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("pharmacy.txt")

    def testRepo(self):        
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