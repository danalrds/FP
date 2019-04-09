'''
Created on Nov 23, 2016

@author: Imi
'''
from controller.ClientControl import ClientController
from domain.clientClass import Client
from builtins import ValueError
from repository.repositoryClass import Repository
from domain.movieClass import Movie
from controller.MovieController import MovieController
from controller.rentalController import RentalController
from domain.rentalClass import Rental,RentalValidator
from datetime import *
from domain.validatorEXception import ValidatorException
class Ui:
    def __init__(self,ClientControl,MovieControl,RentalControl,undoControl):
        self._clientControl=ClientControl
        self._movieControl=MovieControl
        self._rentalControl=RentalControl
        self._undoControl=undoControl
    @staticmethod
    def printMenu():
        string='available commands:\n'
        string+='1-add client\n'
        string+='2-add movie\n'
        string+='3-remove client\n'
        string+='4-remove movie\n'
        string+='5-update client\n'
        string+='6-update movie\n'
        string+='7-list all clients\n'
        string+='8-list all movies\n'
        string+='9-rent a movie\n'
        string+='10-return a movie\n'
        string+='11-view all rentals\n'
        string+='12-search client \n'
        string+='13-search movie \n'
        string+='14-most rented movies\n'
        string+='15-most active clients\n'
        string+='16-late rentals\n'
        string+='17-undo\n'
        string+='18-redo\n'
        string+='0-exit \n'
        
        print(string)
    def MainMenu(self):
        self.printMenu()
        stop=False
        while stop==False:
            try:
                command=input('enter command:\n').strip()
                if command=='1':
                    self.addClientSubmenu()  
                elif command=='2':
                    self.addMovieSubmenu()
                elif command=='3':
                    self.deleteClientSubmenu()
                    print('removal succesful')
                elif command=='4':
                    self.deleteMovieSubmenu()
                elif command=='5':
                    self.updateClientSubmenu()
                elif command=='6':
                    self.updateMovieSubmenu()
                elif command=='7':
                    print(self._clientControl.getAllClients())
                elif command=='8':
                    print(self._movieControl.getAllMovies())   
                elif command=='9':
                    self.newRentalSubmenu()
                elif command=='10':
                    self.returnMovieSubmenu()
                elif command=='11':
                    print(self._rentalControl.getAllRentals())
                elif command=='12':
                    #self.findClientByNameSubmenu()
                    self.findCLient()
                elif command=='13':
                    self.findMovie()
                    #self.findMovie()
                elif command=='14':
                    self.topRentedMovies()
                elif command=='15':
                    self.mostActiveClients()
                elif command=='16':
                    self.printLateRentals()
                elif command=='17':
                    self._undoControl.undoOperation()
                    print('undo succesfull')
                    #print(len(self._undoControl._operations))
                elif command=='18':
                    self._undoControl.redoOperation()
                    print('redo success')
                elif command=='0':
                    print('bye!')
                    stop=True
                else:
                    raise ValueError('pls enter a valid command')
            except Exception as exc:
                print(exc)
    @staticmethod
    def readValidId(ms):
        id=None
        while id==None:
            try:
                id=int(input(ms))
                if id<0:
                    id=None
                    raise ValueError
            except ValueError:
                print('pls input valid id')
        return id
    def addClientSubmenu(self):
        id=self.readValidId('enter client id')
        name=input('enter name')
        client=Client(id,name)
        self._undoControl.newOperation()
        self._clientControl.addClient(client)
        print('client succesfully added')
    def addMovieSubmenu(self):
        id=self.readValidId('enter movie id')
        title=input('enter title')
        description=input('enter description')
        genre=input('enter genre')
        movie=Movie(id, title,description,genre)
        self._undoControl.newOperation()
        self._movieControl.addMovie(movie)
        print('movie succesfully added')
    def deleteClientSubmenu(self):
        id=self.readValidId('enter id of client you eant ot delete')
        self._undoControl.newOperation()
        self._clientControl.removeClient(id)
        #self._undoControl.newOperation()
        self._rentalControl.removeById(None,id)
    def deleteMovieSubmenu(self):
        id=self.readValidId('enter id of movie you want to delete')
        self._undoControl.newOperation()
        self._movieControl.removeMovie(id)
        self._undoControl.newOperation()
        self._rentalControl.removeById(id,None)
        print('movie removed')
    def updateClientSubmenu(self):
        id=self.readValidId('which client do you want to update_')
        name=input('name')
        client=Client(id,name)
        self._undoControl.newOperation()
        self._clientControl.updateClient(client)
        print('succesfully updated')
    def updateMovieSubmenu(self):
        id=self.readValidId('enter id of movie you want to update')
        title=input('new title')
        description=input('description')
        genre=input('genre')
        movie=Movie(id,title,description,genre)
        self._undoControl.newOperation()
        self._movieControl.updateMovie(movie)
        print('succesfully updated')
    def newRentalSubmenu(self):
        rId=self.readValidId('enter rental id')
        mId=self.readValidId('enter movie ID')
        cId=self.readValidId('enter id of client')
        rDate=self.readDate('enter rent date')
        dDate=self.readDate('enter due date')
        #client=self._clientControl._repos.find(cId) 
        #movie=self._movieControl._repo.find(mId) 
       
        #if movie==None or client==None:
        #    raise ValidatorException('pls enter a valid movie and client id')
        self._undoControl.newOperation()      
        self._rentalControl.addRental(rId, mId, cId, rDate, dDate)
        print('rental added')
    def returnMovieSubmenu(self):
        id=self.readValidId('enter id of rental')
        rdate=self.readDate('enter returned date')
        n=datetime.now()
        if rdate<n:
            raise ValidatorException('movie cant be returned in past')
        self._undoControl.newOperation()
        self._rentalControl.returnMovie(id, rdate)
        print('movie returned')
    def findClientByNameSubmenu(self):
        name=input('enter name of client you want to find')
        list=self._clientControl.findClient(name)
        print(self._clientControl.clientListToString(list))
    def findCLient(self):
        comm=input('enter the criteria you want to search by(id/name)')
        if comm not in ['id','name']:
            raise ValidatorException('not a valid criteria')
        elif comm=='id':
            id=self.readValidId('enter id')
            list=self._clientControl.filterClients(id,None)
            print(self._clientControl.clientListToString(list))
        elif comm=='name':
            self.findClientByNameSubmenu()
    def findMovie(self):
        comm=input('enter search criteria name(id/title/description/genre)')
        if comm not in['id','title','description','genre']:
            raise ValidatorException('not a valid criteria')
        if comm=='id':
            id=self.readValidId('enter id')
            list=self._movieControl.filterMovies(id,None,None,None)
        if comm=='title':
            title=input('enter title')
            list=self._movieControl.filterMovies(None,title,None,None)
        if comm=='description':
            description=input('enter description')
            list=self._movieControl.filterMovies(None,None,description,None)
        if comm=='genre':
            genre=input('enter genre')
            list=self._movieControl.filterMovies(None,None,None,genre)
        print(self._movieControl.movieListToString(list))  
    def topRentedMovies(self):
        print('movies rented for most times:')
        result=self._rentalControl.mostTimesRentedMovies()
        for entity in result:
            print(str(entity)+' times\n') 
        print('movies rented for longest period:')
        result2=self._rentalControl.longestPeriodRentedMovie()
        for entity in result2:
            print(str(entity)+' days\n')  
    def mostActiveClients(self):
        print('most active clients:')
        res=self._rentalControl.mostActiveClients()
        for entity in res:
            print(str(entity)+'\n')
    def printLateRentals(self):
        res=self._rentalControl.lateRentals()
        if len(res)==0:
            print('no late rentals')
        else:
            print('late rentals:')
            for entity in res:
                print(str(entity)+'\n')
    def readDate(self,ms):
        d=None 
        while d==None:
            try:
                date=input(ms)
                d = datetime.strptime(date, '%Y, %m, %d')
            except ValueError:
                d=None
                print ("Incorrect format")
        return d
            
            
'''        
clientrep=Repository()
movierep=Repository()
rentalrep=Repository()
valid=RentalValidator()
bob=Client(1,'bob')
arthur=Client(2,'arthur')
titanic=Movie(1,'titanic','romantic cliche', 'drama')
lotr=Movie(2,'lordOFTHeRings','long fantasy idk what', 'fantasy')
movierep.store(lotr)
movierep.store(titanic)
clientrep.store(bob)
clientrep.store(arthur)
controll=ClientController(clientrep)
mcont=MovieController(movierep)
rcont=RentalController(rentalrep, movierep, clientrep,valid)
ui=Ui(controll,mcont,rcont)
ui.MainMenu()
   '''     