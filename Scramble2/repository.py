import unittest
from sentclass import Sentence
class Repository():
    def __init__(self,fname):
        self._objects=[]
        self._fname=fname
        self.__loadfromfile()
    ''' load from file procedure takes data fom input.txt and store it in the list objects'''
    def __loadfromfile(self):
        try:
            f=open(self._fname,"r")
            line=f.readline().strip()
            while line!='':
                sent=Sentence(line)
                self.store(sent)
                line=f.readline().strip()
        except EOFError:
            raise Exception("Wrong!")
        f.close()
    ''' store procedure adds an element to the list '''
    def store(self,obj):
        self._objects.append(obj)   
        self.__storetofile()
    ''''store to file takes the list self._objects and prints it in the file '''
    def __storetofile(self):
        f=open(self._fname,"w")
        for t in self._objects:
            f.write(str(t))
            f.write("\n")
        f.close()
    '''returns all the sentences in the list '''
    def getAll(self):
        return self._objects
class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("input.txt")

    def testName(self):
        list=self._repo.getAll()
        self.assertEqual(len(list),3)
        sent=Sentence("Dana is here")
        self._repo.store(sent)
        list=self._repo.getAll()
        self.assertEqual(len(list),4)