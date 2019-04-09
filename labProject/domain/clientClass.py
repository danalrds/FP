'''
Created on Nov 19, 2016

@author: Imi
'''
from domain.idObjcen import IdObject
class Client(IdObject):
    '''
    client class
    every client has an id, and a name
    '''
    def __init__(self,objectId,name):
        IdObject.__init__(self, objectId)
        self._name=name
    def getName(self):
        return self._name
    def setName(self,name):
        self._name=name
    
    def __str__(self):
        return 'id:'+str(self.getId())+' name:'+self.getName()
    def __eq__(self, client):
        '''
        equality relation override method
        wecheck if the other object is or not an element of the client class
        because at some point we will compare a client to None
        '''
        if isinstance(client, Client)==False:
            return False
        return self.getId()==client.getId()