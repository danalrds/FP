from repository import Repository
from controller import Controller
from interface import Interface
repo=Repository("trip.txt")
control=Controller(repo)
ui=Interface(control)
ui.mainmenu()