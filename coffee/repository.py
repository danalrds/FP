import unittest
from classes import Coffee
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
                d=line.split(";")
                coffee=Coffee(d[0],d[1],float(d[2]))
                self.store(coffee)
                line=f.readline().strip()
        except EOFError:
            raise RepoException("Wrong!")
        f.close()
    def store(self,object):
        self._objects.append(object)
        self.__storetofile()
    def __storetofile(self):
        f=open(self._fname,"w")
        for t in self._objects:
            f.write(str(t))
            f.write("\n")
        f.close()
    def getAll(self):
        return self._objects
class RepoException(Exception):
    def __init__(self,mes):
        self._mes=mes
    def __str__(self):
        return str(self._mes)
class Test(unittest.TestCase):


    def testName(self):
        pass
