import unittest
from teamclass import Team
import pickle
class Repository():
    def __init__(self,fname):
        self._objects=[]
        
        self.__fname=fname
        self.__loadfromfile()
    def __loadfromfile(self):
        f=open(self.__fname,"rb")
        try:
            self._objects=pickle.load(f)
        except EOFError:
            self._objects=[]
        except Exception as exc:
            raise RepositoryException(str(exc))
        finally:
            f.close()
    def store(self,object):
        self._objects.append(object)
        self.__storetofile()
    def __storetofile(self):
        f=open(self.__fname,"wb")
        pickle.dump(self.getAll(),f)
        f.close()     
    
    def getAll(self):
        return self._objects
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
        self._repo=Repository("teams.txt")
    def testRepo(self):
        t=Team("Romania","A",4,6)
        self._repo.store(t)
        list=self._repo.getAll()
        self.assertEqual(list,[t])
        t2=Team("Spania","A",3,3)
        self._repo.update(t,t2)
        list=self._repo.getAll()
        self.assertEqual(list,[t2])
        
        t=Team("Norvegia","A",3,5)
        self._repo.store(t)
        t=Team("Romania","A",4,6)
        self._repo.store(t)
