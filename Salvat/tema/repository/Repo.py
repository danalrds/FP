from tema.domain.classes import *

class StudentRepository:

    def __init__(self):
        """
        Constructor for StudentRepository class
        """
        self.__data = []

    def add(self, student):
        """
        Add a student to the repository        
        """
        self.__data.append(student)
        
    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__data
    def __len__(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return len(self.__data)
    
    def find(self, id):
        """
        Return the first index where the given id is found
        id - The id that is searched for
        Returns- The index where the id is first found, -1 otherwise
        """
        for i in range(0, len(self.__data)):
            if self.__data[i].getId()== id:
                return i
        return -1    
    
    def find_special(self, id):
        """
        Return the name at the index where the given id is found
        id - The id that is searched for
        Returns- the name at the index where the given id is found, -1 otherwise
        """
        for i in range(0, len(self.__data)):
            if self.__data[i].getId()== id:
                return self.__data[i].getName()
        return -1
    def remove(self, id):
        """
        Remove the entry at the given index from the repository
        id - A natural number between 0 and the repo size
        RepositoryException if the provided index is invalid
        """
        poz =  self.find(id)
        if poz ==-1 :
            raise RepositoryException("Inexistent id")        
        return self.__data.pop(poz)        

    def removeAll(self):
        """
        Remove all data from repository 
        """
        self.__data.clear()
        

    def update(self, id, newName):
        """
        Replace the name of the student with the given id with a new one
        id - id that is given
        newName- The new name 
        """
        poz =  self.find(id)
        if poz==-1:
            raise RepositoryException("Inexistent student id") 
        else:
            self.__data[poz].setName(newName)      


class DisciplineRepository:

    def __init__(self):
        """
        Constructor for DisciplineRepository class
        """
        self.__data = []

    def add(self, discipline):
        """
        Add a discipline to the repository
        discipline - discipline to be added
        """
        self.__data.append(discipline)
        
    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__data
    
    def find(self, id):
        """
        Return the first index where the given id is found
        id - The id that is searched for
        Returns- The index where the id is first found, -1 otherwise
        """
        for i in range(0, len(self.__data)):
            if self.__data[i].getId()== id:
                return i
        return -1
    
    def find_special(self, id):
        """
        Return the name of the discipline with  the given id
        id - The id that is searched for
        Returns- The the name of the discipline with  the given id, -1 otherwise
        """
        for i in range(0, len(self.__data)):
            if self.__data[i].getId()== id:
                return self.__data[i].getName()
        return -1
    
    def remove(self, id):
        """
        Remove the entry at the given id from the repository
        id - A natural number between 0 and the repo size
        RepositoryException if the provided id is invalid
        """
        poz =  self.find(id)
        if poz ==-1 :
            raise RepositoryException("Inexistent id")        
        return self.__data.pop(poz)

    def removeAll(self):
        """
        Remove all data from repository 
        """
        self.__data.clear()
    

    def update(self, id, newName):
        """
        Replace the name of the discipline with the given id with a new one
        id - The given index
        newName - The new name for discipline
        """
        poz =  self.find(id)
        if poz==-1:
            raise RepositoryException("Inexistent discipline id") 
        else:
            self.__data[poz].setName(newName)       
        

class GradeRepository:

    def __init__(self):
        """
        Constructor for GradeRepository class
        """
        self.__data = []

    def add(self, grade):
        """
        Add a grade to the repository
        grade - grade to be added
        """
        self.__data.append(grade)
        
    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__data
    
    def find_both(self, id_s,id_d):
        """
        Return the first index where the given id_student and id_discipline are found
        id_s - The id of the student
        id_d - The id of the discipline
        Returns- The index where the id_s and id_d are found, -1 otherwise
        """
        for i in range(0, len(self.__data)):
            if self.__data[i].getIdStudent()== id_s:
                if self.__data[i].getIdDiscipline()==id_d:
                    return i
        return -1
    
    def find_s(self, id_s):
        """
        Return the index where a certain id_student is found
        id_s - The id of the student
        Returns- The index where the given id is first found, -1 otherwise
        """
        for i in range(0, len(self.__data)):
            if self.__data[i].getIdStudent()== id_s:
                return i
        return -1
    
    def find_d(self, id_d):
        """
        Return the index where a certain id_discipline is found
        id_s - The id of the discipline
        Returns- The index where the given id is first found, -1 otherwise
        """
        for i in range(0, len(self.__data)):
            if self.__data[i].getIdDiscipline()== id_d:
                return i
        return -1
    def remove_s(self, id_s):
        """
        Remove the entry at the given index from the repository
        id_s - A natural number between 0 and the repo size
        RepositoryException if the provided index is invalid
        """
        poz =  self.find_s(id_s)
        if poz ==-1 :
            raise RepositoryException("Inexistent id")        
        return self.__data.pop(poz)
    
    def remove_d(self, id_d):
        """
        Remove the entry at the given index from the repository
        id_d - A natural number between 0 and the repo size
        RepositoryException if the provided index is invalid
        """
        poz =  self.find_d(id_d)
        if poz ==-1 :
            raise RepositoryException("Inexistent id")        
        return self.__data.pop(poz)

    def removeAll(self):
        """
        Remove all data from repository 
        """
        self.__data.clear()
    

    def update(self, id_s,id_d,newvalue):
        """
        Replace the old grade with a new one
        id_s=the student id
        id_d=the discipline id
        newvalue - The new grade value
        """
        poz =  self.find_both(id_s,id_d)
        if poz==-1:
            raise RepositoryException("Inexistent discipline id") 
        else:
            self.__data[poz].setValue(newvalue)
                    
class RepositoryException(Exception):
    """
    Exception class for repository errors
    """
    def __init__(self, message):
        """
        Constructor for repository exception class
        message - A string representing the exception message
        """
        self.__message = message

    def __str__(self):
        return self.__message

def testStudentRepository():
    repo =StudentRepository()
    testList = [Student(1,'Popescu Vlad'), Student(2,'Macrea Silvia'), Student(3,'Popkins Marry')]
    for i in range(0, len(testList)):
        repo.add(testList[i])
        assert repo.get(i) == testList[i]
    
    for i in range(0, len(testList)):
        assert repo.remove(0) == testList[i]