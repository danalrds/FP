from repository import Repository
from controller import Controller
from interface import Interface
repo=Repository("teams.txt")
control=Controller(repo)
ui=Interface(control)
ui.mainmenu()
#Spania Norvegia 22 26