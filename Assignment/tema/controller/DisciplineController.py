from tema.controller.ControllerException import *  
class DisciplineController:
    """
    Controller class for Discipline
    """
    def __init__(self, repod,repog):
        """
        calls the repository and initialize the entities
        """
        self.__repod = repod
        self.__repog = repog
        self.__undo = []

    def addDiscipline(self, discipline):
        """
        calls the repository operation of adding an element
        """
       # self.__undo = self.__repo.getAll()[:]        
        dis=discipline.getId()
        name=discipline.getName()
        if name !='':
            if self.__repod.find(dis)==-1: 
                self.__repod.add(discipline) 
            else:           
                print("Id already exists!")
        else:
            print("Discipline name is empty!")

    def remove(self, index):
        """
        calls the repository operation of removing an element
        """
        #self.__undo = self.__repo.getAll()[:]
        self.__repod.remove(index)        
        while self.__repog.find_d(index)!=-1:
            self.__repog.remove_d(index)
        

    def removeAll(self):
        """
        calls the repository operation that removes all elements
        """
        #self.__undo = self.__repo.getAll()[:]
        #while self.__repo.find(number) > -1:
            #index = self.__repo.find(number)
        self.__repod.removeAll()
        self.__repog.removeAll()

    def getAll(self):
        """
        Returns all the elements of the entity student
        """
        return self.__repod.getAll()
    
    def update(self,id, newName):
        """
        Returns the updated list after the newname modification
        """
        self.__repod.update(id, newName)   
    
    def search(self,y):
        '''
          Function that searches the id or name as strings, and if there is a discipline with the substring given id or the substring given name it prints it
        '''
        dto=[]
        tot=self.__repod.getAll()
        for n in tot:
            id=str(n.getId())
            id2=id.lower()
            name=n.getName()
            name2=name.lower()      
            if id2.find(y) !=-1 or name2.find(y)!=-1:
                dto.append((id,name))         
        return dto
    #############################################