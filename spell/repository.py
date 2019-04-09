from dictionary import Dictionary
import unittest
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
                d=line.split(';')
                dict=Dictionary(int(d[0]),d[1],d[2])
                self.store(dict)
                line=f.readline().strip()
        except EOFError:
            raise RepositoryException("Wrong!")
        f.close()
    def store(self,object):
        self._objects.append(object)
        self.__storetofile()
    def getAll(self):
        return self._objects
    def __storetofile(self):
        f=open(self._fname,'w')
        for s in self._objects:
            f.write(str(s))
            f.write('\n')
        f.close()
class RepositoryException(Exception):
    def __init__(self,mes):
        self._mes=mes
    def __str__(self):
        return str(self._mes)
class Test(unittest.TestCase):


    def testName(self):
        pass

