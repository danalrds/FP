'''
Created on Dec 1, 2016

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
clientrep=Repository()
movierep=Repository()
rentalrep=Repository()
valid=RentalValidator()
und=UndoController()
bob=Client(1,'Vladimir Putin')
art=Client(2,'Harambe')
nap=Client(3,'Napoleon Bonaparte')
nir=Client(4,'Kurt Cobain')
lop=Client(5,'Leopold Habsburg')
titanic=Movie(1,'titanic','romantic cliche', 'drama')
lotr=Movie(2,'lordOFTHeRings','long fantasy idk what', 'fantasy')
drac=Movie(3,'whoat','Exorcizamus te, omnis immundus','kk')# \n spiritus, omnis satanica potestas,\n  omnis incursio infernalis adversarii, \n omnis legio,omnis congregatio et \n secta diabolica ','horror')
wd=Movie(4,'Underworld','havent seen, dont know','nnn')
end=Movie(5,'End of the world', 'not inteterstin','idk')
rdate=datetime.strptime('2016, 12, 2','%Y, %m, %d')
ddate=datetime.strptime('2016, 12, 9','%Y, %m, %d')

ern=Rental(99, lotr, bob,rdate, ddate, None )
stl=Rental(98,lotr,nir,datetime.strptime('2016, 12, 11','%Y, %m, %d'),datetime.strptime('2016, 12, 24','%Y, %m, %d'),None)
rtl=Rental(97,wd,bob,datetime.strptime('2016, 12, 1','%Y, %m, %d'),datetime.strptime('2016, 12, 8','%Y, %m, %d'),None)
movierep.store(lotr)
movierep.store(drac)
movierep.store(titanic)
movierep.store(wd)
movierep.store(end)
clientrep.store(bob)
clientrep.store(nap)
clientrep.store(art)
clientrep.store(nir)
clientrep.store(lop)
rentalrep.store(ern)
rentalrep.store(stl)
rentalrep.store(rtl)
controll=ClientController(clientrep,und)
mcont=MovieController(movierep,und)
rcont=RentalController(rentalrep, movierep, clientrep,valid,und)
ui=Ui(controll,mcont,rcont,und)
ui.MainMenu()
        