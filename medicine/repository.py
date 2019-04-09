import unittest
from medicineclass import Medicine

class Repository():
    def __init__(self,fname):
        self._objects=[]
        self._fname=fname
        self.__loadfromfile()
    
    def __loadfromfile(self):
        try:
            f=open(self._fname,'r')
            line=f.readline().strip()
            while line!='':
                d=line.split(';')
                object=Medicine(int(d[0]),d[1],int(d[2]))
                self.store(object)
                line=f.readline().strip()
        except EOFError:
            raise RepositoryException("Something went wrong!")
        finally:
            f.close()
    def store(self,object):
        self._objects.append(object)
        self.__storetofile()
    def remove(self,id):
        if self.find(id)!=None:
            self._objects.remove(self.find(id))
            self.__storetofile()
        else:
            raise RepositoryException("Element not in repository!")
    def __storetofile(self):
        f=open(self._fname,'w')
        for m in self.getAll():
            f.write(str(m))
            f.write("\n")
        f.close()
    def getAll(self):
        return self._objects
    def update(self,old,new):
        index=self._objects.index(old)
        self._objects[index]=new 
    def find(self,id):        
        for m in self.getAll():
            if m.getId()==id:
                return m 
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
        self._repo=Repository("medicine.txt")
    def testRepo(self):
        m=Medicine(12,"Paracetamol",452)
        self._repo.store(m)
        list=self._repo.getAll()
        self.assertEqual(list,[m])
        m2=Medicine(13,"Reuprofen",30)
        self._repo.store(m2)
        list=self._repo.getAll()
        self.assertEqual(list,[m,m2])
        self._repo.remove(12)
        list=self._repo.getAll()
        self.assertEqual(list,[m2])
        m3=Medicine(13,"Reuprofen",35)
        self._repo.update(m2,m3)
        list=self._repo.getAll()
        self.assertEqual(list,[m3])
         