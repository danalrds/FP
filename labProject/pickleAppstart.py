'''
Created on Dec 14, 2016

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
from controller.undoController import UndoController
from domain.validatorEXception import ValidatorException
from interface import Ui
from repository.clientFileRepository import ClientFileRepository
from repository.movieFileRepository import MovieFileRepository
from repository.rentalFileRepository import RentalFileREpository
from repository.pickleRepo import PickleRepo
clientRep=PickleRepo("C:/Users/Imi/Desktop/pTextFiles/pick.pickle.txt")
movieRep=PickleRepo("C:/Users/Imi/Desktop/pTextFiles/pickleMovies.txt")
rentalRep=PickleRepo("C:/Users/Imi/Desktop/pTextFiles/pickleRentals.txt")
valid=RentalValidator()
undo=UndoController()
clControl=ClientController(clientRep,undo)
mvControl=MovieController(movieRep,undo)
rentControl=RentalController(rentalRep,movieRep,clientRep,valid,undo)
inter=Ui(clControl,mvControl,rentControl,undo)
inter.MainMenu()