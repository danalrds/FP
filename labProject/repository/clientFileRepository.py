'''
Created on Dec 11, 2016

@author: Imi
'''
from repository.repositoryClass import Repository
from domain.clientClass import Client
from repository.generalFileRepo import FileRepository
class ClientFileRepository(Repository):
    def __init__(self,filename):
        Repository.__init__(self)
        self.__fileName=filename
        self.__loadFromFile()
    def store(self, obj):
        Repository.store(self, obj)
        self.__storeToFile()
    def delete(self, objId):
        client=Repository.delete(self, objId)
        self.__storeToFile()
    #def clearAll(self):
    #    Repository._objects.clear()
   #     self.__storeToFile()
    def update(self, object):
        Repository.update(self, object)
        self.__storeToFile()
            
        
    def __loadFromFile(self):
        try:
            f=open(self.__fileName, "r")
            line=f.readline().strip()
            while line!="":
                lineData=line.split(';')
                client=Client(int(lineData[0]),lineData[1])
                Repository.store(self,client)
                line=f.readline().strip()
        except IOError:
            raise FileRepoException("can't open file")
        finally:
            f.close()
    def __storeToFile(self):
        f=open(self.__fileName,"w")
        clientList=Repository.getAll(self)
        for client in clientList:
            clientString=str(client.getId())+';'+client.getName()+'\n'
            f.write(clientString)
        f.close()
            
                    
            
        
        
        
        
class FileRepoException(Exception):
    def __init__(self, message):
        self._message = message

    def getMessage(self):
        return self._message

    def __str__(self):
        return self._message
#repo=Repository()
#fileRepo=ClientFileRepository('C:/Users/Imi/Desktop/try.txt')
#bob=Client(2,'gareth bobby fergusson')
#fileRepo.store(bob)
#print(fileRepo.getAll())
#fileRepo.update(bob)
#fileRepo.delete(2)
#print(str(fileRepo.find(2)))













