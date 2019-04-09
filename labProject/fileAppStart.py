'''
Created on Dec 12, 2016

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

clientRep=ClientFileRepository('C:/Users/Imi/Desktop/pTextFiles/repo.txt')
movieRep=MovieFileRepository('C:/Users/Imi/Desktop/pTextFiles/movieRepo.txt')
rentalRep=RentalFileREpository(movieRep,clientRep,'C:/Users/Imi/Desktop/pTextFiles/rentalRepo.txt')
valid=RentalValidator()
undo=UndoController()
clientControl=ClientController(clientRep,undo)
movieControl=MovieController(movieRep,undo)
rentalControl=RentalController(rentalRep,movieRep,clientRep,valid,undo)
ui=Ui(clientControl,movieControl,rentalControl,undo)
ui.MainMenu()

#movieRep=MovieFileRepository('C/Users/Imi/Desktop/pTexFiles/repo.txt')
