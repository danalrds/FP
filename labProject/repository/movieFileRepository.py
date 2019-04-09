'''
Created on Dec 11, 2016

@author: Imi
'''
from repository.repositoryClass import Repository
from repository.clientFileRepository import FileRepoException
from domain.movieClass import Movie
class MovieFileRepository(Repository):
    def __init__(self,filename):
        Repository.__init__(self)
        self.__fileName=filename
        self.__loadFromFile()
    def __loadFromFile(self):
        try:
            f=open(self.__fileName, "r")
            line=f.readline().strip()
            while line!="":
                lineData=line.split(';')
                movie=Movie(int(lineData[0]),lineData[1],lineData[2],lineData[3])
                Repository.store(self,movie)
                line=f.readline().strip()
        except IOError:
            raise FileRepoException("can't open file")
        finally:
            f.close()
    def __storeToFile(self):
        f=open(self.__fileName,"w")
        movieList=Repository.getAll(self)
        for movie in movieList:
            mString=str(movie.getId())+';'+movie.getTitle()+';'+movie.getDescription()+';'+movie.getGenre()+'\n'
            f.write(mString)
        f.close()
    def store(self, obj):
        Repository.store(self, obj)
        self.__storeToFile()
    def delete(self, objId):
        client=Repository.delete(self, objId)
        self.__storeToFile()
    #def clearAll(self):
      #  Repository._objects.clear()
     #   self.__storeToFile()
    def update(self, object):
        Repository.update(self, object)
        self.__storeToFile()