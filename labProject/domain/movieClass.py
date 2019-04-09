'''
Created on Nov 19, 2016

@author: Imi
'''
from domain.idObjcen import IdObject
class Movie(IdObject):
    def __init__(self,objId,title,description,genre):
        '''
        every movie will have a unique id, a title, a description, a genre
        '''
        IdObject.__init__(self,objId)
        self._title=title
        self._description=description
        self._genre=genre
    def getTitle(self):
        return self._title
    def setTitle(self,title):
        self._title=title
    def getDescription(self):
        return self._description
    def setDescription(self,description):
        self._description=description
    def getGenre(self):
        return self._genre
    def setGenre(self,genre):
        self._genre=genre
    def __eq__(self, movie):
        if isinstance(movie, Movie)==False:
            return False
        return movie.getId()==self.getId()
    def __str__(self):
        '''
        override str function so that a movie instance will be more readable as a string
        '''
        return 'id: '+str(self.getId())+' ,title: '+str(self.getTitle())+' ,description: '+str(self.getDescription())+' ,genre: '+str(self.getGenre())
    
            