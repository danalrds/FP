from tema.controller.ControllerException import *  
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
        ok=False
        for n in tot:
            ok=True
            id=n.getIdStudent()
            stud=self.__repo.find_special(id)
            
            id=n.getIdDiscipline()
            dis=self.__repod.find_special(id)
            
            val=n.getValue()
            print(stud,'~',dis,'~',val)
        if ok==False:
            print("There are no grades")
    
    def update(self,id_s,id_d, newvalue):
        '''
        Returns the updated list after the newname modification
        '''
        self.__repog.update(id_s,id_d,newvalue)        

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
    
    def sort_total(self):
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
        #print(list)
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
        
    def sort_alldisciplines(self):
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
    
    def sort_average(self,name): 
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
        if i==name:
            return i
    return -1
