'''
Created on Nov 25, 2016

@author: Imi
'''
from repository.iterable import filterList
from repository.iterable import gnomeSort
from repository.repositoryClass import RepositoryException
from domain.rentalClass import Rental, RentalValidator
from datetime import *
from domain.clientClass import Client
from repository.iterable import Iterable
from controller.undoController import UndoController, Function, Operation
class RentalController:
    def __init__(self,Rentalrepo, MovieRepo, ClientRepo, RValidator,undoController):
        self._RentalRepo=Rentalrepo
        self._MovieRepo=MovieRepo
        self._ClientRepo=ClientRepo
        self.__RValidator=RValidator
        self._undoController=undoController
    def addRental(self,id, mId, cId, rentDate, dueDate):
        '''
        (add rental)-method that checks before adding rental to repository that 
        the involved client has no rented movies that is not returned in time, 
        and if the involved movie is available or not
        input-id, movie, client, rentDate, dueDate-fields of a rental object to build
        output-none
         
        '''
        client=self._ClientRepo.find(cId) 
        movie=self._MovieRepo.find(mId) 
        if movie==None or client==None:
            raise RepositoryException('pls enter a valid movie and client id')
        rental=Rental(id, movie, client,rentDate,dueDate, None)
        self.__RValidator.validate(rental)
        #print(self.checkMovieAvailability(movie, rentDate, dueDate))
        if self.checkMovieAvailability(movie, rentDate, dueDate)==False:
            raise RepositoryException('movie is not available in that period')
        #print(len(rental))
        self._RentalRepo.store(rental)
        redo=Function(self.addRental,id, mId, cId, rentDate, dueDate)
        undo=Function(self.removeRental, id)
        operation=Operation(redo, undo)
        self._undoController.saveOperation(operation)
        
    def removeRental(self,id):
        rental=self._RentalRepo.find(id)
        self._RentalRepo.delete(id)
        redo=Function(self.removeRental,id)
        undo=Function(self.addRental, rental.getId(),rental.getMovie().getId(),rental.getClient().getId(),rental.getRentDate(),rental.getDueDate())
        operation=Operation(redo,undo)
        self._undoController.saveOperation(operation)
    def returnMovie(self,id,date):
        '''
        (return movie)-method
        input-id of rental involved
        we search fCor the involved rental by it's id, anr raise repositoryException if
        it is not found, otherwise we set it's return date to the date parameter of this method
        '''
        ndate=datetime.now()
        o=self._RentalRepo.find(id)
        if o==None:
            raise RepositoryException('no rental found')
        elif o.getReturnDate()!=None:
            raise RepositoryException('movie is already returned')
        o.setReturnDate(ndate)
        redo=Function(self.returnMovie,id,date)
        undo=Function(o.setReturnDate, None)
        operation=Operation(redo,undo)
        self._undoController.saveOperation(operation)
    def getAllRentals(self):
        '''
        we specified this mehtod so many tiiiimes
        '''
        return str(self._RentalRepo)
            
    def filterRentals(self, client,movie):   
        '''
        filter rentals method
        we pass as parameters both client and movie, so we don't have to
        write two methods to filter once by movies, and again by clients
        if we wish to filter by one, then we pass None for the other
         '''
             
        filtered=[]
        #for rental in self._RentalRepo.getAll():
            #if client!=None :
             #   if rental.getClient()==client:
             #       filtered.append(rental)
            #if movie!=None:
                #if rental.getMovie()==movie:
                #print(rental.getMovie()==movie)
                    #filtered.append(rental)
        return filtered
    def checkMovieAvailability(self, movie, rentDate, dueDate):
        '''
        check availability of movie in the period rentDate-dueDate
        for this we check if the movie is not already rented or it will not be in the given period
        '''
        rentalList=self.filterRentals(None, movie)
        #print(rentalList)
        for rental in rentalList:
            if rentDate> rental.getDueDate() or  dueDate<rental.getRentDate():
                continue
            return False
        return True
    def mostTimesRentedMovies(self):
        '''
        we calculate for each movie how many times it was rented
        for this we will use a dictionary, where the key is the movie title
        and value is the number it was rented
        then we transform the dictionary into a data transfer object list
        and output the new list of objects
        '''
        result={}
        for movie in self._MovieRepo.getAll():
            if movie.getTitle() not in result.keys():
                result[movie.getTitle()]=0
            countList=self.filterRentals(None, movie)
            result[movie.getTitle()]=len(countList)
        statList=[]
        for movieTitle in result.keys():
            movieCount=MovieCountTransfer(movieTitle, result[movieTitle])
            statList.append(movieCount)
        statList.sort(reverse=True)
        return statList
    def longestPeriodRentedMovie(self):
        '''
        calculate for every movie the number of days it was rented for
        this method requires no specific input
        as an output we get a list of data trnasfer objects, where
        one filed is the movie name, the other is the number of days it was rented
        '''
        
        resultList=[]
        for movie in self._MovieRepo.getAll():
            statList=self.filterRentals(None, movie)
            length=0
            for rental in statList:
                length+=len(rental)
            movieTrans=MovieCountTransfer(movie.getTitle(), length)
            resultList.append(movieTrans)  
        resultList.sort(reverse=True)
        #print(resultList)
        return resultList
    def mostActiveClients(self):
        '''
        calculate for every client the number of movie rental days they have
        for this we will create a dto-list
        '''
        resList=Iterable()
        for client in self._ClientRepo.getAll():
            #print(client.getName())
            statList=self.filterRentals(client, None)
            #print(statList)
            length=0
            for rental in statList:
                length+=len(rental)
            clientTrans=ClientTransfer(client.getName(), length)
            resList.append(clientTrans)
        resList.gnome()
        return resList
    def lateRentals(self):
        '''
        return the list of rentals for which the due date passed, together with the list of delayed rentals
        '''
        resList=[]
        n=datetime.now()
        for rental in self._RentalRepo.getAll():
            if rental.getReturnDate()==None and rental.getDueDate()< n:
                day=abs(n-rental.getDueDate()).days
                rentalTrans=RentalTransfer(rental, day)
                resList.append(rentalTrans)
        resList.sort(reverse=True)
        return resList
    def rentalIdLister(self,movieId,clientId):
        result=[]
        for rental in self._RentalRepo.getAll():
            if movieId!=None and movieId==rental.getMovie().getId():
                result.append(rental.getId())
            if clientId!=None and clientId==rental.getClient().getId():
                result.append(rental.getId())
        return result
    def removeById(self,movieId, clientId):
        '''
        this method is used when a client or movie is removed and
        the rentals related to them have to be deleted too 
        we build the list of rentalId-s from Ids of rentals having a given client/movie,
        then we remove each rental by their idsfrom the list
        '''
        deathList=[]
        for rental in self._RentalRepo.getAll():
            if movieId!=None and movieId==rental.getMovie().getId():
                deathList.append(rental.getId())
            if clientId!=None and clientId==rental.getClient().getId():
                deathList.append(rental.getId())
        for id in deathList:
            rental=self._RentalRepo.find(id)
            undo=Function(self._RentalRepo.store,rental)
            redo=Function(self._RentalRepo.delete,id)
            operation=Operation(redo,undo)
            self._undoController.saveOperation(operation)
            self._RentalRepo.delete(id)
        
    def acceptFilter(self,rental,):
        if 
        
               
                               
    
    
class MovieCountTransfer():
    '''
    data trnasfer object-class for statistics
    name filed is not specified because we use this class
    to transfer movies and clients as well
    '''
    def __init__(self,name, times):
        self._name=name
        self._times=times
    def getName(self):
        return self._name
    def getTimes(self):
        return self._times
    def __lt__(self,obj):
        return self.getTimes() < obj.getTimes()
    def __str__(self):
        text=''
        text+=str(self.getName())+' was rented for '+str(self.getTimes())###uptade it such that it can be used for both ststcs
        return text
    
class ClientTransfer(MovieCountTransfer):
    '''
    child class of the above dto class
    the only difference between the two classes is the overridden str method, which has to be
    specific for clients and movies
    '''
    def __str__(self):
        return str(self.getName())+' has a total rental days of '+str(self.getTimes())
    
class RentalTransfer():
    '''
    data transfer object for rentals
    '''
    def __init__(self, rental, lateDays):
        self._rental=rental
        self._lateDays=lateDays
    def getRental(self):
        return self._rental
    def getLateDays(self):
        return self._lateDays
    def __str__(self):
        return str(self.getRental().getClient().getName())+'('+str(self.getRental().getId())+')s rental of '+str(self.getRental().getMovie().getTitle())+' has a delay of '+str(self.getLateDays())+' days'
        
    
    
    
    