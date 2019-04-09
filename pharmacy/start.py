from domain.medicineclass import Medicine
from repository.MedicineRepository import Repository
from controller.Controller import Controller
from interface import Interface
repo=Repository("pharmacy.txt")
control=Controller(repo)
ui=Interface(control)
ui.mainmenu()