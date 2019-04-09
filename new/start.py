from repository.OrderRepository import OrderRepository
from repository.DriverRepository import DriverRepository
from controller.Controller import Controller
from interface import Interface
repo_order=OrderRepository("orders.txt")
repod=DriverRepository("drivers.txt")
control=Controller(repo_order,repod)
ui=Interface(control)
ui.mainmenu()