from repository.Repository import Repository
from controller.Controller import Controller
from  interface import Interface
repo=Repository("cars.txt")
control=Controller(repo)
ui=Interface(control)
ui.mainmenu()