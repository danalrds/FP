import unittest
from classes import Bear
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
                d=line.split(",")
                bere=Bear(d[0],d[1],float(d[2]))
                self.store(bere)
                line=f.readline().strip()   
        except EOFError:
            raise Exception("Wrong!")
        f.close()    
    def store(self,obj):
        self._objects.append(obj)
        self.__storetofile()        
    def getAll(self):
        return self._objects    
    def __storetofile(self):
        f=open(self._fname,"w")
        for t in self._objects:
            f.write(str(t))
            f.write("\n")
        f.close()
    def update(self,old,new):
        idx=self._objects.index(old)
        self._objects[idx]=new
        self.__storetofile()
class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("produse.txt")
    def testRepo(self):
        b=Bear("Ciucas","blonda",3.14)        
        self._repo.store(b)
        '''
        self._repo.store(b2)
        self.assertEqual(self._repo.find(12),b)
        self.assertEqual(self._repo.find(47),b2)
        '''
        
