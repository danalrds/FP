'''
Created on Nov 20, 2016

@author: Imi
'''
from domain.clientClass import Client
from repository.repositoryClass import Repository, RepositoryException
from clientRepository import ClientRepository
from controller.undoController import Function,UndoController, Operation
class ClientController:
    def __init__(self,repos,undoController):
        self._repos=repos
        self._undoController=undoController
    def addClient(self,client):
        '''
        mainstream add method
        input-client, that will be stored in controller's repository
        output-
        '''
        self._repos.store(client)
        redo=Function(self.addClient,client)
        undo=Function(self.removeClient,client.getId())
        operation=Operation(redo, undo)
        #operation.undo()
        self._undoController.saveOperation(operation)
    def removeClient(self,id):
        '''
        mainstream remove method
        input:-id of client that will be deleted
        output-
        '''
        client=self._repos.find(id)
        self._repos.delete(id)
        redo=Function(self.removeClient,id)
        undo=Function(self.addClient,client)
        operation=Operation(redo, undo)
        self._undoController.saveOperation(operation)
    def updateClient(self,client):
        '''
        updates client, recieved as input
        '''
        old=self._repos.find(client.getId())
        self._repos.update(client)
        redo=Function(self.updateClient,client)
        undo=Function(self.updateClient,old)
        operation=Operation(redo, undo)
        self._undoController.saveOperation(operation)
    def getAllClients(self):
        '''
        returns the string representation of  client's data from repository
        '''
        return str(self._repos)
        #########################################################################################   reference to line160 of interaface 
    def findClient(self,name):
        result=[]
        for client in self._repos.getAll():
            if name.upper() in client.getName().upper():
                result.append(client)
        return result  
    ##############################################################################################
    def clientListToString(self,list):
        '''
        do I really need this method?
        '''
        res=''
        for client in list:
            res+=str(client)+'\n'
        return res
    def filterClients(self,id, name):
        '''
        filter clients either by name or by id
        id filter works with equality checking, while
        name filter works with case-insensitive, parial string mathcing
        '''
        result=[]
        for client in self._repos.getAll():
            if name!=None and name.upper() in client.getName().upper():
                result.append(client)
            if id!=None and client.getId()==id:
                result.append(client)
        return result
    
    
    
#tingo=Client(1,'dingo')
#dingo=Client(2,'dingo')
#repoting=Repository()
#contri=ClientController(repoting) o
#contri.addClient(tingo)
#contri.addClient(dingo)
#print(contri.getAll())
#print("this")