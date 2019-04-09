'''
Created on Dec 14, 2016

@author: Imi
'''
import pickle
from repository.repositoryClass import Repository
from repository.clientFileRepository import FileRepoException
from domain.clientClass import Client
class PickleRepo(Repository):
    def __init__(self,fname):
        Repository.__init__(self)
        self.__fileName=fname
        self.__loadFromFile()
    def __loadFromFile(self):
        f=open(self.__fileName,"rb")
        try:
            self._objects=pickle.load(f)
        except EOFError:
            self._objects=[]
        except Exception as exc:
            raise FileRepoException(str(exc))
        finally:
            f.close()
    def __storeToFile(self):
        f=open(self.__fileName,"wb")
        pickle.dump(Repository.getAll(self),f)
        f.close()
    def store(self, obj):
        Repository.store(self, obj)
        self.__storeToFile()
    def delete(self, objId):
        Repository.delete(self, objId)
        self.__storeToFile()
    def update(self, object):
        Repository.update(self, object)
        self.__storeToFile()
    def clearAll(self):
        Repository.clearAll(self)
        self.__storeToFile()
#c=Client(1,'sssspp')
#rep=PickleRepo('C:/Users/Imi/Desktop/pTextFiles/pick.pickle.txt')
#rep.clearAll()
#rep.store(c)
#o=rep.find(1)
#print(str(o))