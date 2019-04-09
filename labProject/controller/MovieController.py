'''
Created on Nov 25, 2016

@author: Imi
'''
from repository.repositoryClass import RepositoryException
from controller.undoController import UndoController, Operation
from controller.undoController import Function
class MovieController:
    def __init__(self,repo,undoController):
        self._repo=repo
        self._undoController=undoController
        #self._rentalRepo=rentalRepo
    def addMovie(self,movie):
        '''
        method that adds a movie to the repository of itself
        '''
        self._repo.store(movie)
        redo=Function(self.addMovie,movie)
        undo=Function(self.removeMovie, movie.getId())
        operation=Operation(redo, undo)
        self._undoController.saveOperation(operation)
       # print(self._undoController._operations)
    def removeMovie(self,id):
        '''
        mainstream  remove method
        recieves as input the id of the movie that will be deleted
        '''
        if self._repo.find(id)!=None:
            movie=self._repo.find(id)
            self._repo.delete(id)
            redo=Function(self.removeMovie, id)
            undo=Function(self.addMovie, movie)
            operation=Operation(redo, undo)
            #operation.redo()
            self._undoController.saveOperation(operation)
        else:
            raise RepositoryException('movie not found')
    def updateMovie(self,movie):
        '''
        update method
        recieves as input the whole movie object
        '''
        old=self._repo.find(movie.getId())
        self._repo.update(movie)
        #print(old.getTitle())
        redo=Function(self.updateMovie,movie)
        undo=Function(self.updateMovie,old)
        operation=Operation(redo, undo)
        #operation.undo()
        self._undoController.saveOperation(operation)
    def getAllMovies(self):
        '''
        returns the string representation of all movies from repository
        '''
        return str(self._repo)
    def filterMovies(self,id, title, description, genre):
        '''
        this method allows us to filter the content of the movie repository by certain criteria
        as input we pass as parameters some attributes of a movie object, based on wich we will filter the repo
        in case we wnat to filter by one criteria, we pass as parameters None for the other attributes
        as an output we get a list of filtered rentals
        '''
        result=[]
        for movie in self._repo.getAll():
            if id!=None and movie.getId()==id:
                result.append(movie)
            if title!=None and title.upper() in movie.getTitle().upper():
                result.append(movie)
            if description!=None and description.upper() in movie.getDescription().upper():
                result.append(movie)
            if genre!=None and genre.upper() in movie.getGenre().upper():
                result.append(movie)
    
        return result
    def movieListToString(self,list):
        '''
        this method basically exist just for the filtetMOvies method's sake
        '''
        res=''
        for movie in list:
            res+=str(movie)+'\n'
        return res

            
            
            
            
            
            
            
            
