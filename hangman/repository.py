import unittest
from sentclass import Sentence
class Repository():
    def __init__(self,fname):
        self._objects=[]
        self._fname=fname
        self.__loadfromfile()
    '''load from file procedure reads all the lines from sentences.txt and creates a list with all of them '''
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
    '''store procedure 
    input data: an object of type sentence
    it is addes in the list self._objetcs'''
    def store(self,obj):
        self._objects.append(obj)        
        self.__storetofile()
    ''' returns all the sentences from the file'''
    def getAll(self):
        return self._objects
    '''store to file procedure takes all the sentences from self._objects and writes them into the file '''
    def __storetofile(self):
        f=open(self._fname,"w")
        for t in self._objects:
            f.write(str(t))
            f.write("\n")
        f.close()
class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("sentences.txt")

    def testName(self):
        list=self._repo.getAll()
        self.assertEqual(len(list),6)
        sent=Sentence("patricia has apples")
        self._repo.store(sent)
        self.assertEqual(len(list),2)