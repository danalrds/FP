import unittest
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
  