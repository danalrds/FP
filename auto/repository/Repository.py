from domain.carclass import Car
import unittest

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
                d=line.split(";")
                c=Car(int(d[0]),d[1],float(d[2]))
                self.store(c)
                line=f.readline().strip()
        except EOFError:
            raise RepositoryException("Something went wrong!")
    def store(self,object):
        self._objects.append(object)
        self.__storetofile()
    def getAll(self):
        return self._objects
    def __storetofile(self):
        f=open(self._fname,'w')
        for obj in self.getAll():
            f.write(str(obj))
            f.write("\n")
    def findbyid(self,id):
        for z in self.getAll():
            if z.getId()==id:
                return z
        return None
    def delete(self,id):
        gasit=self.findbyid(id)
        if self.findbyid(id)!=None:
            self._objects.remove(gasit)
            self.__storetofile()
        else:
            raise RepositoryException("Inexistent id!")
    def update(self,old,new):
        index=self._objects.index(old)
        self._objects[index]=new
        self.__storetofile()
class RepositoryException(Exception):
    def __init__(self,mes):
        self._mes=mes
    def getMessage(self):
        return self._mes
    def __str__(self):
        return str(self._mes)

class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("cars.txt")
    def testRepo(self):
       c=Car(1,"Audi",1000)
       self._repo.store(c)
       list=self._repo.getAll()
       self.assertEqual(list,[c])
       c2=Car(1,"Mercedes",1000)
       self._repo.update(c,c2)       
       list=self._repo.getAll()
       self.assertEqual(list,[c2])