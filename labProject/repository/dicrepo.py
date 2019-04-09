from domain.clientClass import Client
class DicRepository():
    def __init__(self):
        '''
        repository class is specified such that it can be used for storing multiple type of data
        obviously,in one repository instance we will store one type of data
        '''
        self._objects={}
    def find(self,objId):
        '''
        (find object in repository by id)-method
        returns instance found, if found, none otherwise
        '''
        if objId not in self._objects.keys():
            return None
        else:
            return self._objects[objId]
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
            self._objects[obj.getId()]=obj
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
            self._objects[object.getId()]=object
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
    
    
    
    
    
    
repo=DicRepository()
bob=Client(1,'bob')
bob2=Client(1,'updatedBob')
repo.store(bob)
repo.update(bob2)
o=repo.find(1)
print(str(repo._objects[1 ])) 
print(o.getName())
