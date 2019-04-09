from repository.FilmRepository import Repository
from controller.controller import Controller
from interface import Interface
repo=Repository("filme.txt")
control=Controller(repo)
ui=Interface(control)
ui.mainmenu()