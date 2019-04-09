import unittest
from tema.repository.Repo import *
from tema.operations.Controller import *
#Class that defines the entity student and its getters and setters
class Student:    
    
    def __init__(self, id, name):
        """
        Constructor for Student class
        Input: id and name of the student
        """
        self.__id = id
        self.__name =name       
    
       
    def getId(self):
        """
        Getter for the id of the student
        Output: id of student
        """
        return self.__id 
    def getName(self):
        """
        Getter for the name of the student
        Output: the name of the student
        """
        return self.__name    
        
        """
        Setter for the name of the student        
        """    
    def setName(self, y):
        self.__name = y
        
        """
        Function that returns a string from the entity student        
        """    
    def __str__(self):
        r = ''
        r=str(self.__id)+'.'+self.__name        
        return r

#Class that defines the entity discipline and its getters and setters    
class Discipline:    
    
    def __init__(self, id, name):
        """
        Constructor for Discipline class
        Input: discipline id, discipline name
        """
        self.__id = id
        self.__name =name       
    
       
    def getId(self):
        """
        Getter for the id of the discipline
        Output: the id of the discipline
        """
        return self.__id 
    def getName(self):
        """
        Getter for the name of the discipline
        Output: The name of the discipline
        """
        return self.__name    
        
        """
        Setter for the name of the discipline       
        """    
    def setName(self, y):
        self.__name = y
        
        """
        Function that returns a string from the entity discipline        
        """  
    def __str__(self):
        r = ''
        r=str(self.__id)+')'+self.__name        
        return r

#Class that defines the entity discipline and its getters and setters        
class Grade:    
    
    def __init__(self, id_s,id_d,val):
        """
        Constructor for Grade class
        Input: id_student, id_discipline,grade
        """
        self.__id_student = id_s
        self.__id_discipline =id_d
        self.__val=val    
    
       
    def getIdStudent(self):
        """
        Getter for id_student of the grade
        Output: id_student of the grade
        """
        return self.__id_student 
    def getIdDiscipline(self):
        """
        Getter for id_discipline of the grade
        Output: id_discipline of the grade
        """
        return self.__id_discipline     
        
    def getValue(self):
        """
        Getter for the value of the grade
        Output: the grade
        """
        return self.__val      

    def setValue(self, y):
        """
        Setter for the value of the grade       
        """    
        self.__val = y

class Tests(unittest.TestCase):
    def test_student(self):   
        assert str(Student(1,'Popescu Vlad')) == '1.Popescu Vlad'
        assert str(Student(2,'Macrea Silvia')) == '2.Macrea Silvia'
        assert str(Student(3,'Popkins Marry')) == '3.Popkins Marry'
        assert str(Student(4,'Marc Andiniu')) == '4.Marc Andiniu'
        assert str(Student(5,'Sisoko Antonella')) == '5.Sisoko Antonella'
        assert str(Student(6,'Cuvino Ecaterina')) == '6.Cuvino Ecaterina'
        assert str(Student(7,'Feretti Kendra')) == '7.Feretti Kendra'
        assert str(Student(8,'Kovacs Iulius')) == '8.Kovacs Iulius'
        assert str(Student(9,'Turea Emanuel')) == '9.Turea Emanuel'
        
        stud=Student(1,'Macrea Silvia')
        assert stud.getId()==1
        assert stud.getName()=='Macrea Silvia'    
    
    def test_discipline(self):   
        assert str(Discipline(1,'Economie')) == '1)Economie'
        assert str(Discipline(2,'Chimie')) == '2)Chimie'
        assert str(Discipline(3,'Fizica cuantica')) == '3)Fizica cuantica'
        dis=Discipline(3,'Franceza')
        assert dis.getId()==3
        assert dis.getName()=='Franceza' 

    def test_grade(self):       
        gr=Grade(1,1,10)
        gr2=Grade(3,7,8)
        gr3=Grade(9,3,9)
        assert gr.getIdStudent()==1
        assert gr2.getIdStudent()==3
        assert gr3.getIdStudent()==9
        assert gr.getIdDiscipline()==1
        assert gr2.getIdDiscipline()==7
        assert gr3.getIdDiscipline()==3
        assert gr.getValue()==10
        assert gr2.getValue()==8
        assert gr3.getValue()==9  
    
    def testInitStudent(self):
        repo=StudentRepository()
        repod=DisciplineRepository()
        repog=GradeRepository()
        ctrl=StudentController(repo,repod,repog)
        student=Student(3, "Vasile")
        st=ctrl.addStudent(student)
        assert student.getId()==3
        assert student.getName()=="Vasile"
         

    def testAddStudent(self):
        repo=StudentRepository()
        repod=DisciplineRepository()
        repog=GradeRepository()
        ctrl=StudentController(repo,repod,repog)
        student=Student(1, "ana")
        st=ctrl.addStudent(student)
        assert len(StudentController(repo,repod,repog).getAll())==1
        assert student.getId()==1
        assert student.getName()=="ana"
    
    def testUpdateStudent(self):
        repo=StudentRepository()
        repod=DisciplineRepository()
        repog=GradeRepository()
        ctrl=StudentController(repo,repod,repog)
        student=Student(3, "Vasile")
        st=ctrl.addStudent(student)  
        st=ctrl.update(3, "Nicol")
        assert student.getId()==3
        assert student.getName()=="Nicol"
    
    def testRemoveStudent(self):
        repo = StudentRepository()
        repod=DisciplineRepository()
        repog=GradeRepository()
        ctrl=StudentController(repo,repod,repog)
        student=Student(1, "ana")
        st=ctrl.addStudent(student)       
        ctrl.remove(1)
        assert ctrl.getAll()==[]

     ###################################################################
     
    def testInitDiscipline(self):
        
        repod=DisciplineRepository()  
        repog=GradeRepository()      
        ctrl=DisciplineController(repod,repog)
        discipline=Discipline(3, "Chimie")
        dis=ctrl.addDiscipline(discipline)
        assert discipline.getId()==3
        assert discipline.getName()=="Chimie"
         

    def testAddDiscipline(self):
        repod=DisciplineRepository()  
        repog=GradeRepository()      
        ctrl=DisciplineController(repod,repog)
        discipline=Discipline(3, "Chimie")
        dis=ctrl.addDiscipline(discipline)
        assert len(DisciplineController(repod,repog).getAll())==1
        assert discipline.getId()==3
        assert discipline.getName()=="Chimie"        
    
    def testUpdateDiscipline(self):
        repod=DisciplineRepository()  
        repog=GradeRepository()      
        ctrl=DisciplineController(repod,repog)
        discipline=Discipline(3, "Chimie")
        dis=ctrl.addDiscipline(discipline)
        assert discipline.getId()==3
        assert discipline.getName()=="Chimie"          
        dis=ctrl.update(3, "Filozofie")
        assert discipline.getId()==3
        assert discipline.getName()=="Filozofie"
    
    def testRemoveDiscipline(self):
        repod=DisciplineRepository()  
        repog=GradeRepository()      
        ctrl=DisciplineController(repod,repog)
        discipline=Discipline(8, "Chineza")
        dis=ctrl.addDiscipline(discipline)
        assert len(DisciplineController(repod,repog).getAll())==1
        assert discipline.getId()==8
        assert discipline.getName()=="Chineza"              
        ctrl.remove(8)
        assert ctrl.getAll()==[]   
    
     ################################################################################
     
    def testInitGrade(self):
        repog=GradeRepository()
        repo=StudentRepository()
        repod=DisciplineRepository()        
        ctrl=GradeController(repog,repo,repod)
        grade=Grade(1,2,8)
        gr=ctrl.addGrade(grade)
        assert grade.getIdStudent()==1
        assert grade.getIdDiscipline()==2
        assert grade.getValue()==8
                 

    def testAddGrade(self):
        repog=GradeRepository()
        repo=StudentRepository()
        repod=DisciplineRepository()        
        ctrl=GradeController(repog,repo,repod)
        grade=Grade(1,2,8)
        gr=ctrl.addGrade(grade)
        assert len(GradeController(repog,repo,repod).getAll())==1
        assert grade.getIdStudent()==1
        assert grade.getIdDiscipline()==2
        assert grade.getValue()==8       
    
    def testUpdateGrade(self):
        repog=GradeRepository()
        repo=StudentRepository()
        repod=DisciplineRepository()        
        ctrl=GradeController(repog,repo,repod)
        grade=Grade(1,2,8)
        gr=ctrl.addGrade(grade)
        assert len(GradeController(repog,repo,repod).getAll())==1
        assert grade.getIdStudent()==1
        assert grade.getIdDiscipline()==2
        assert grade.getValue()==8       
        gr=ctrl.update(1,2,5)
        assert grade.getValue()==5
        
    
    def testRemoveGrade(self):
        repog=GradeRepository()
        repo=StudentRepository()
        repod=DisciplineRepository()        
        ctrl=GradeController(repog,repo,repod)
        grade=Grade(4,5,6)
        gr=ctrl.addGrade(grade)
        assert len(GradeController(repog,repo,repod).getAll())==1
        assert grade.getIdStudent()==4
        assert grade.getIdDiscipline()==5
        assert grade.getValue()==6              
        ctrl.removeAll()
        assert ctrl.getAll()==[]
   
        