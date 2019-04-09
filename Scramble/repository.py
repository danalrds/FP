import unittest
from sentclass import Sentence
class Repository():
    def __init__(self,fname):
        self._objects=[]
        self._fname=fname
        self.__loadfromfile
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
    def getAll(self):           
        return self._objects
       
    def store(self,obj):
        self._objects.append(obj)
        self.__storetofile()
    def __storetofile(self):
        f=open(self._fname,"w")
        for s in self._objects:
            f.write(str(s))
            f.write("\n")
        f.close()    
    
class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("sent.txt")

    def testName(self):
        
        list=[]
        list=self._repo.getAll()        
        print(len(list))
        
