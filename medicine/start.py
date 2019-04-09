from repository import Repository
from controller import Controller
from medicineclass import Medicine
from interface import Interface
repo=Repository("medicine.txt")
control=Controller(repo)
ui=Interface(control)
ui.mainmenu()