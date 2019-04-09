from tema.controller.ControllerException import *  
class StudentController:
    """
    Controller class for students
    """
    def __init__(self, repo,repog):
        """
        calls the repository and initialize the entities
        """
        self.__repo = repo
        self.__repog = repog
        self.__undo = []

    def addStudent(self, student):
        """
        calls the repository operation of adding an element
        """
        # self.__undo = self.__repo.getAll()[:]
        stud=student.getId()
        name=student.getName()
        if name != '':
            if self.__repo.find(stud)==-1: 
                self.__repo.add(student)
            else:
                print("Id already exists!")
        else:
            print("Name is empty!")

    def remove(self, index):
        """
        calls the repository operation of removing an element
        """
        #self.__undo = self.__repo.getAll()[:]
        self.__repo.remove(index)
        while self.__repog.find_s(index)!=-1:
            self.__repog.remove_s(index)

    def removeAll(self):
        """
        calls the repository operation that removes all elements
        """
        #self.__undo = self.__repo.getAll()[:]
        #while self.__repo.find(number) > -1:
            #index = self.__repo.find(number)
        self.__repo.removeAll()
        self.__repog.removeAll()
    def getAll(self):
        """
        Returns all the elements of the entity student
        """
        return self.__repo.getAll()
    
    def update(self,id, newName):
        """
        Returns the updated list after the newname modification
        """
        self.__repo.update(id, newName)        

    
    def undo(self):
        """
        undo the last operation
        """
        if len(self.__undo) == 0:
            raise ControllerException("No undo steps available!")
        
        self.__repo.removeAll()
        for z in self.__undo:
            self.__repo.add(z)
        self.__undo.clear()
    
    def search(self,y):
        '''
          Function that searches the id or name as strings, and if there is a student with the substring given id or the substring given name it prints it
        '''
        tot=self.__repo.getAll()
        for n in tot:
            id=str(n.getId())
            id2=id.lower()
            name=n.getName()
            name2=name.lower()      
            if id2.find(y) !=-1 or name2.find(y)!=-1:
                print(id,".",name)       
    
    def fail(self): 
        okk=False   
        tot=self.__repo.getAll()
        for n in tot:
            id=n.getId()
            name=n.getName()
            list=self.__repog.getAll()
            ok=False
            for i in list:
                if i.getIdStudent()==id:
                    nota=i.getValue()
                    if nota<5:
                        ok=True                                    
            if ok==True:
                print(id,'.',name)
                okk=True
        if okk==False:
            print("0 students failed")
#######################################################3


 
