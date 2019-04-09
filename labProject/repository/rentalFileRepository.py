'''
Created on Dec 11, 2016

@author: Imi
'''
from repository.repositoryClass import Repository
from domain.movieClass import Movie
from domain.rentalClass import Rental
from datetime import *
from repository.clientFileRepository import FileRepoException
class RentalFileREpository(Repository):
    def __init__(self,movierepo,clientrepo,filename):
        Repository.__init__(self)
        self._movieRepo=movierepo
        self._clientRepo=clientrepo
        self.__fileName=filename
        self.__loadFromFile()
    def store(self, obj):
        Repository.store(self, obj)
        self.__storeToFile()
    def delete(self, objId):
        Repository.delete(self, objId)
        self.__storeToFile()
    def update(self, object):
        Repository.update(self, object)
        self.__storeToFile()
    def __loadFromFile(self):
        try:
            f=open(self.__fileName,"r")
            line=f.readline().strip()
            while line!="":
                lineData=line.split(';')
                movie=self._movieRepo.find(int(lineData[1]))
                client=self._clientRepo.find(int(lineData[2]))
                if movie==None or client ==None:
                    raise FileRepoException('smoething went wrong')
                if len(lineData)==4:
                    rental=Rental(int(lineData[0]),movie,client,datetime.strptime(lineData[3],'%Y, %m, %d'),datetime.strptime(lineData[4],'%Y, %m, %d'),None)
                elif len(lineData)==5:
                    rental=Rental(int(lineData[0]),movie,client,datetime.strptime(lineData[3],'%Y, %m, %d'),datetime.strptime(lineData[4],'%Y, %m, %d'),datetime.strptime(lineData[5],'%Y, %m, %d'))
                Repository.store(self,rental)
                line=f.readline().strip()
        except IOError:
            raise FileRepoException('cant open file')
        finally:
            f.close()
    def __storeToFile(self):
        f=open(self.__fileName,"w")
        rentalList=Repository.getAll(self)
        for rental in rentalList:
            rentalString=str(rental.getId())+';'+str(rental.getMovie().getId())+';'+str(rental.getClient().getId())+';'+str(rental.getRentDate())+';'+str(rental.getDueDate())
            if rental.getReturnDate()!=None:
                rentalString+=';'+str(rental.getReturnDate())
            rentalString+='\n'
            f.write(rentalString)
        f.close()
        