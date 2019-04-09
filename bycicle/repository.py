import unittest
from bycicleclass import Bycicle
class Repository():
    def __init__(self,filename):
        self._objects=[]
        self._filename=filename
        self.__loadfromfile()
    def __loadfromfile(self):
        try:
            f=open(self._filename,'r')
            line=f.readline().strip()
            while line!='':
                d=line.split(';')
                object=Bycicle(int(d[0]),d[1],float(d[2]))
                self.store(object)
                line=f.readline().strip()
        except EOFError:
            raise RepositoryException("Something went wrong!")
        finally:
            f.close()
    def __storetofile(self):
        f=open(self._filename,'w')
        for b in self.getAll():
            f.write(str(b))
            f.write("\n")
        f.close()
    def getAll(self):
        return self._objects
    def store(self,object):
        if self.find(object.getId())!=None:
            raise RepositoryException("Id already in use!")
        else:
            self._objects.append(object)
        self.__storetofile()
    def update(self,old,new):
        index=self._objects.index(old)
        self._objects[index]=new
        self.__storetofile()
        
        
    def delete(self,id):
        if self.find(id)==None:
            raise RepositoryException("Element not in repository!")
        else:
            self._objects.remove(self.find(id))
        self.__storetofile()
    def find(self,id):  
        for b in self.getAll():
            if b.getId()==id:
                return b
        return None
class RepositoryException(Exception):
    def __init__(self,mesaj): 
        self._mesaj=mesaj
    def getMessage(self):
        return self._mesaj
    def __str__(self):
        return str(self._mesaj)      
class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("bycicle.txt")
    def testRepo(self):
        b=Bycicle(12,"Pegas",100.5)
        b2=Bycicle(47,"Pegasssss",589)
        self._repo.store(b)
        self._repo.store(b2)
        self.assertEqual(self._repo.find(12),b)
        self.assertEqual(self._repo.find(47),b2)
        
        


