from studentrepository import Repository
from studentrepository import GradeRepository
from studentcontroller import Controller
from interface import Interface
repo=Repository("students.txt")
graderepo=GradeRepository("grades.txt")
control=Controller(repo,graderepo)
ui=Interface(control)
ui.mainmenu()