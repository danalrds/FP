import unittest
from classes import Film
class Repository():
    def __init__(self,fname):
        self._fname=fname
        self._objects=[]
        self.__loadfromfile()
    def __loadfromfile(self):
        try:
            f=open(self._fname,"r")
            line=f.readline().strip()
            while line!='':
                d=line.split(";")
                film=Film(int(d[0]),d[1],float(d[2]),int(d[3]))
                self.store(film)
                line=f.readline().strip()
        except EOFError:
            raise RepoException("Wrong!")
        f.close()
    def __storetofile(self):
        f=open(self._fname,"w")
        for t in self._objects:
            f.write(str(t))
            f.write("\n")
        f.close()
    def store(self,object):
        self._objects.append(object)
        self.__storetofile()
    def getAll(self):
        return self._objects
    def update(self,old,new):
        idx=self._objects.index(old)
        self._objects[idx]=new
        self.__storetofile()
class RepoException(Exception):
    def __init__(self,mes):
        self._mes=mes
    def __str__(self):
        return str(self._mes)
class Test(unittest.TestCase):


    def testName(self):
        pass
