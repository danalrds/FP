from classes import Film
from repository import Repository


class Controller():
    def __init__(self,repo):
        self._repo=repo
    def getAll(self):
        return self._repo.getAll()
    def actualizeaza(self,old,new):
        self._repo.update(old,new)
    def findbyid(self,id):
        for t in self.getAll():
            if t.getId()==id:
                return t
        return None
        
class ControlException(Exception):
    def __init__(self,mes):
        self._mes=mes
    def __str__(self):
        return str(self._mes)