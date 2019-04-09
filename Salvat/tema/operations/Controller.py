class StudentController:
    """
    Controller class for students
    """
    def __init__(self, repo,repod,repog):
        """
        calls the repository and initialize the entities
        """
        self.__repo = repo
        self.__repod = repod
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
        list=[]
        for n in tot:
            id=str(n.getId())
            id2=id.lower()
            name=n.getName()
            name2=name.lower()      
            if id2.find(y) !=-1 or name2.find(y)!=-1:
                list.append((id,name))    
        return list
#######################################################3

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
        tot=self.__repod.getAll()
        list=[]
        for n in tot:
            id=str(n.getId())
            id2=id.lower()
            name=n.getName()
            name2=name.lower()      
            if id2.find(y) !=-1 or name2.find(y)!=-1:
                list.append((id,name))        
        return list
    #############################################
    
class GradeController:
    """
    Controller class for Grade
    """
    def __init__(self, repog,repo,repod):
        """
        calls the repository and initialize the entities
        """
        self.__repog = repog
        self.__repo = repo
        self.__repod = repod
        self.__undo = []

    def addGrade(self, grade):
        """
         calls the repository operation of adding an element
        """
       # self.__undo = self.__repo.getAll()[:]
        self.__repog.add(grade)
    

    def removeAll(self):
        """
        calls the repository operation that removes all elements
        """
        #self.__undo = self.__repo.getAll()[:]
        #while self.__repo.find(number) > -1:
            #index = self.__repo.find(number)
        self.__repog.removeAll()

    def getAll(self):
        """
        Returns all the elements of the entity student
        """
        tot=self.__repog.getAll()
        list=[]
        ok=False
        for n in tot:
            ok=True
            id=n.getIdStudent()
            stud=self.__repo.find_special(id)
            
            id=n.getIdDiscipline()
            dis=self.__repod.find_special(id)
            
            val=n.getValue()
            list.append((stud,dis,val))
            print(stud,'~',dis,'~',val)
        if ok==False:
            print("There are no grades")
        return list
    def update(self,id_s,id_d, newvalue):
        '''
        Returns the updated list after the newname modification
        '''
        self.__repog.update(id_s,id_d,newvalue)        
    
    '''
         function that sorts alphabetically al the students with grades at a given Discipline
         Output:list with all the students sorted by the name increasingly
    '''
    def sort_alph(self,name): 
        studenti=self.__repo.getAll()  
        tot=self.__repod.getAll()
        note=self.__repog.getAll()
        for n in tot:
            if n.getName()==name:
                id=n.getId()                        
        list=[]
        for n in note:
            if n.getIdDiscipline()==id:
                id_s=n.getIdStudent()                
                name=self.__repo.find_special(id_s)                
                if este(list,name)==-1:
                    list.append(name)
        list.sort()                   
        return list
    '''
        Function that determines the averages at all disciplines for each student
        Output: list with all students with grades, the discipline and the her average
    '''
    def mediastudenti(self):
        list=[]
        discipline=self.__repod.getAll()
        note=self.__repog.getAll()
        for n in note:
            nota=n.getValue()
            dis=n.getIdDiscipline()
            stud=n.getIdStudent()
            poz=is_there(list,stud,dis)
            if poz==-1:
                list.append((stud,dis,nota,1))
            else:
                nota=nota+list[poz][2]
                c=1+list[poz][3]
                object=(stud,dis,nota,c)
                list[poz]=object
        for i in range (0,len(list)):
            l=list[i]
            media=l[2]/l[3]
            list[i]=(l[0],l[1],media,l[3])
        return list
    '''
        Function that computes the average of averages of all students
        Provides the list of all students sorted decreasingly by their agregated average
    '''
    def sort_total(self):
        list=self.mediastudenti()       
        sir=[]
        for el in list:
            id=el[0]
            stud=self.__repo.find_special(id)
            poz=search_dis(sir,stud)
            if poz==-1:
                sir.append((stud,el[2],1,0))
            else:
                nota=el[2]+sir[poz][1]
                c=1+sir[poz][2]
                object=(stud,nota,c,0)
                sir[poz]=object
        for i in range (0,len(sir)):
            s=sir[i]
            medie=s[1]/s[2]
            sir[i]=(s[0],s[1],s[2],medie)
        sort_descending(sir)                
        return(sir)       
     ###################################################
    '''
        Function that computes the average of students at all  disciplines 
        Output:a list with the name of the discipline and her grade
    '''
    def media_all_disciplines(self):
        discipline=self.__repod.getAll()
        note=self.__repog.getAll()
        list=[]
        for n in note:
            nota=n.getValue()
            dis=n.getIdDiscipline()
            stud=n.getIdStudent()
            poz=is_there(list,stud,dis)
            if poz==-1:
                list.append((stud,dis,nota,1))
            else:
                nota=nota+list[poz][2]
                c=1+list[poz][3]
                object=(stud,dis,nota,c)
                list[poz]=object
        for i in range (0,len(list)):
            l=list[i]
            media=l[2]/l[3]
            list[i]=(l[0],l[1],media,l[3])
        return list   
    '''
        Function that sorts all the disciplines by the average of all students averages
        Output:The list with the discipline and the average of the students averages    
    '''
    def sort_alldisciplines(self):
        list=[]
        list=self.media_all_disciplines()       
        sir=[]
        for el in list:
            id=el[1]
            dis=self.__repod.find_special(id)
            poz=search_dis(sir,dis)
            if poz==-1:
                sir.append((dis,el[2],1,0))
            else:
                nota=el[2]+sir[poz][1]
                c=1+sir[poz][2]
                object=(dis,nota,c,0)
                sir[poz]=object
        for i in range (0,len(sir)):
            s=sir[i]
            medie=s[1]/s[2]
            sir[i]=(s[0],s[1],s[2],medie)
        sort_descending(sir)        
        return(sir)       
        
    
    #########################################################
    '''
    Function that finds the average of a student at all disciplines
    Output:A list with the name of a student, his average and the number of grades at the discipline
    '''
    def media_bdisciplina(self,name):
        studenti=self.__repo.getAll()  
        tot=self.__repod.getAll()
        note=self.__repog.getAll()
        for n in tot:
            if n.getName()==name:
                id=n.getId()                        
        list=[]
        for n in note:
            if n.getIdDiscipline()==id:
                nota=int(n.getValue())
                id_s=n.getIdStudent()                
                name=self.__repo.find_special(id_s)                
                poz=exista(list,name)                
                if poz==-1:                                      
                    list.append((name,nota,1,0))                    
                else:                   
                    object=list[poz]
                    s=int(object[1])+nota                    
                    c=int(object[2])+1
                    av=0
                    new=(name,s,c,av)                                       
                    list[poz]=new 
        return list 
    
    '''
        Function that sorts all the students by their average at a given discipline
        Returns a list with the name,the grades, their number and the average
    '''
    def sort_average(self,name):
        list=[] 
        list=self.media_bdisciplina(name)        
        for i in range (0,len(list)):
            object=list[i]; 
            name=object[0]
            note=object[1]
            contor=object[2]          
            media=note/contor
            list[i]=(name,note,contor,media)
        sort_descending(list)
        return list
    
    #########################################################
    
    '''
    Function that finds all the students that have failed to one or more disciplines
    Provides a list with all the students failing, the discipline and its average 
    '''
    def fail(self): 
        okk=False 
        list=[]  
        studenti=self.__repo.getAll()
        discipline=self.__repod.getAll()
        list=self.mediastudenti()        
        rezults=[(t[0],t[1],t[2]) for t in list if t[2]<5]
        
        list=[]
        for r in rezults:
            name=self.__repo.find_special(r[0])      
            dis=self.__repod.find_special(r[1])      
            nota=r[2]
            list.append((name,dis,nota))
        return list
        
def sort_descending(list):
    ok=True 
    while ok==True:
        ok=False
        for i in range(0,len(list)-1):            
            if list[i][3]<list[i+1][3]:
                ok=True
                aux=list[i]
                list[i]=list[i+1]
                list[i+1]=aux

def search_dis(sir,dis):
    for i in range (0,len(sir)):
        if sir[i][0]==dis:
            return i
    return -1      

def is_there(list,stud,dis):
    for i in range (0,len(list)):
        if list[i][0]==stud and list[i][1]==dis:
            return i
    return -1      
def exista(list,name):
    for i in range (0,len(list)):
        if list[i][0]==name:
            return i
    return -1          
        
def este(list,name):
    for i in range (0,len(list)):
        if list[i]==name:
            return i
    return -1

class StudentAvg():
    def __init__(self, student, average):
        self.__student = student
        self.__average = average

    def getStudent(self):
        return self.__student
    
    def getAverage(self):
        return self.__average
    
    def __lt__(self, grade):
        """
        < operator required for sorting the list
        """
        return self.getAverage() < grade.getAverage()
    
    def __str__(self):
        return str(self.getAverage()).ljust(10) + " for car " + str(self.__student).ljust(40)




class ControllerException(Exception):
    """
    Exception class for controller errors
    """
    def __init__(self, message):
        """
        Constructor for controller exception class
        message - A string representing the exception message
        """
        self.__message = message

    def __str__(self):
        return self.__message
