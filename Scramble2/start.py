from repository import Repository
from controller import Controller
class Interface():
    def __init__(self,control):
        self._control=control
    def start(self):
        self._control.joaca()
repo=Repository("input.txt")
control=Controller(repo)
ui=Interface(control)
ui.start()