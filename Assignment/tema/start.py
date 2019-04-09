from tema.repository.Repo import *
from tema.controller.StudentController import *
from tema.controller.DisciplineController import *
from tema.controller.GradeController import *
from tema.ui.menu import UI
from tema.domain.classes import *
'''Function that initialize the entity student with 10 items '''
def InitStudent():
    repo.add(Student(1,'Popescu Vlad'))
    repo.add(Student(2,'Macrea Silvia'))
    repo.add(Student(3,'Popkins Marry'))
    repo.add(Student(4,'Marc Andiniu'))
    repo.add(Student(5,'Sisoko Antonella'))
    repo.add(Student(6,'Cuvino Ecaterina'))
    repo.add(Student(7,'Feretti Kendra'))
    repo.add(Student(8,'Kovacs Iulius'))
    repo.add(Student(9,'Turea Emanuel'))
    repo.add(Student(10,'Bold Robert'))

'''Function that initialize the entity discipline with 10 items '''    
def InitDiscipline():
    repod.add(Discipline(1,'Economie'))
    repod.add(Discipline(2,'Filozofie'))
    repod.add(Discipline(3,'Fizica cuantica'))
    repod.add(Discipline(4,'Algebra'))
    repod.add(Discipline(5,'Logica'))
    repod.add(Discipline(6,'Analiza'))
    repod.add(Discipline(7,'Biologie'))
    repod.add(Discipline(8,'Geometrie'))
    repod.add(Discipline(9,'Speologie'))
    repod.add(Discipline(10,'Istorie'))

'''Function that initialize the entity grade with 10 items ''' 
def InitGrade():
    repog.add(Grade(1,1,9))
    repog.add(Grade(2,2,7))
    repog.add(Grade(2,2,4))
    repog.add(Grade(4,2,9))
    repog.add(Grade(7,2,5))
    repog.add(Grade(2,6,7))
    repog.add(Grade(6,7,3))
    repog.add(Grade(8,9,1))
    repog.add(Grade(10,9,5))
    repog.add(Grade(6,4,10))    
    
#test_student()
#test_discipline()
#test_grade()
# test=Tests(unittest.TestCase)
repo = StudentRepository()
repod=DisciplineRepository()
repog=GradeRepository()
InitStudent()
InitDiscipline()
InitGrade()
controller = StudentController(repo,repog)
controller2=DisciplineController(repod,repog)
controller3=GradeController(repog,repo,repod)
ui = UI(controller,controller2,controller3)

ui.mainMenu()
