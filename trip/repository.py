from datetime import datetime
from tripclass import Trip
import unittest

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
                date=datetime.strptime(str(d[1]),'%Y-%m-%d %H:%M:%S')
                t=Trip(d[0],date,int(d[2]))
                self.store(t)
                line=f.readline().strip()
        except EOFError:
            raise RepositoryException("Something went wrong!")
        finally:
            f.close()
    
    def store(self,object):
        self._objects.append(object)
        self.__storetofile()
        
    def update(self,old,new):
        index=self._objects.index(old)
        self._objects[index]=new
        self.__storetofile()
        
    def __storetofile(self):
        f=open(self._filename,'w')
        for t in self.getAll():
            f.write(str(t))
            f.write('\n')
        f.close()
    def getAll(self):
        return self._objects
class RepositoryException(Exception):
    def __init__(self,msg):
        self._msg=msg
    def getMessage(self):
        return self._msg
    def __str__(self):
        return str(self._msg)

class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("trip.txt")
    def testRepo(self):        
        d1 = datetime.strptime('2017, 12, 7', '%Y-%m-%d %H:%M:%S')
        d2 = datetime.strptime('2017, 12, 30', '%Y-%m-%d %H:%M:%S')
        t=Trip("Shanghai",d1,800)
        self._repo.store(t)
        list=self._repo.getAll()
        self.assertEqual(list,[t])
        t2=Trip("Beyjing",d2,900)
        self._repo.store(t2)
        list=self._repo.getAll()
        self.assertEqual(list,[t,t2])
        
