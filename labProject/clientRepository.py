'''
Created on Nov 19, 2016

@author: Imi
'''
from repository.repositoryClass import Repository
from domain.clientClass import Client
class ClientRepository(Repository):
    def __init__(self):
        self._objects=[]
repo=ClientRepository()
#bob=Client(2,'bob')
#donna=Client(1,'Donna')
#repo.store(bob)
#repo.store(donna)
#print(str(donna))