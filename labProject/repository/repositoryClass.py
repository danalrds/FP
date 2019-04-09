'''
Created on Nov 19, 2016

@author: Imi
'''
from repository.iterable import Iterable
from domain.clientClass import Client
class Repository():
    def __init__(self):
        '''
        repository class is specified such that it can be used for storing multiple type of data
        obviously,in one repository instance we will store one type of data
        '''
        self._objects=Iterable()
    def find(self,objId):
        '''
        (find object in repository by id)-method
        returns instance found, if found, none otherwise
        '''
        for o in self._objects:
            if objId == o.getId():
                return o
        return None
    def delete(self,objId):
        '''
        remove object method
        input-objId-the id of object that will be deleted
        output-
        we chwck first if the object with the given id is or not in the repository
        '''
        object = self.find(objId)
        if object == None:
            raise RepositoryException("Element not in repository!")
        self._objects.remove(object)
        return object
    def store(self,obj):
        if self.find(obj.getId())==None:
            self._objects.append(obj)
        else:
            raise RepositoryException("Id already in use")
    def update(self,object):
        '''
        update instance fields, finding it first by id
        input-object, that will take the place of the old object
        output-
        '''
        element=self.find(object.getId())
        if element ==None:
            raise RepositoryException('no element found')
        else:
            #idx = self._objects.index(element)
            #self._objects.remove(element)
            self._objects.replace(element, object)
    def getAll(self):
        return self._objects
    def __len__(self):
        return len(self._objects)
    def __str__(self):
        if len(self._objects)==0:
            return 'repository is empty'
        res = "Repository:\n"
        for e in self._objects:
            res += str(e)
            res += "\n"
        return res
    def clearAll(self):
        self._objects.clear()
            
class RepositoryException(Exception):
    '''
    class for excptions that are related for repsitory, for example
    not found-, id used-type exceptions
    '''
    def __init__(self, message):
        self._message = message

    def getMessage(self):
        return self._message

    def __str__(self):
        return self._message






            
    

#lis=Iterable()
#lis.add(5)
#bob=Client(1,'bob')
#lis.add(bob)
#print(str(lis))




