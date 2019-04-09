from tema.domain.classes import *

class UI:
    def __init__(self, controller,controller2,controller3):
        self._controller = controller
        self._controller2=controller2
        self._controller3=controller3    
        
    @staticmethod
    def printMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1 - Add student \n'
        string += '\t 2 - Remove student by ID \n'
        string += '\t 3 - Remove all students \n'
        string += '\t 4 - Display students \n'
        string += '\t 5 - Reset name for ID student\n'
        string += '\t 6 - Add discipline \n'
        string += '\t 7 - Remove discipline by id \n'
        string += '\t 8 - Remove all disciplines \n'
        string += '\t 9 - Display disciplines \n'
        string += '\t 10 -Reset name for ID discipline\n' 
        string += '\t 11 -Give a grade to a student\n' 
        string += '\t 12 -List grades\n'
        string += '\t 13 -Remove grades\n'  
        string += '\t 14 -Search for id or student name\n'  
        string += '\t 15 -Show statistics\n'  
        string += '\t 16 Undo\n' 
        string += '\t 16 Redo\n'     
        string += '\t 0 - Exit\n'
        print(string)

    def mainMenu(self):
        keepAlive = True
        while keepAlive:
            try:
                UI.printMenu()
                command = input("Enter command: ").strip()
                if command == '0':
                    print("exit...")
                    keepAlive = False
                elif command == '1':
                    z = UI.readStudent()                    
                    self._controller.addStudent(z)
                elif command == '2':
                    p = self.readPositiveInteger("Please give ID: ")
                    try:                        
                        self._controller.remove(p)
                    except Exception as ve:
                        print(ve)
                elif command == '3':                    
                    self._controller.removeAll()
                elif command == '4':  
                    ok=False                        
                    for n in self._controller.getAll():
                        print(str(n))
                        ok=True
                    if ok==False:
                        print("There are no students!")   
                elif command == '5':
                    id = self.readPositiveInteger("Please give ID: ")
                    newName = input("Enter a new name: ")
                    self._controller.update(id, newName)
                elif command == '6':
                    z = UI.readDiscipline()                                   
                    self._controller2.addDiscipline(z)
                elif command == '7':
                    p = self.readPositiveInteger("Please give the ID of the discipline: ")
                    try:                        
                        self._controller2.remove(p)
                    except Exception as ve:
                        print(ve)
                elif command == '8':                    
                    self._controller2.removeAll()
                elif command == '9':
                    ok=False   
                    for n in self._controller2.getAll():
                        print(str(n))
                        ok=True
                    if ok==False:
                        print("There are no disciplines!")   
                elif command == '10':
                    id = self.readPositiveInteger("Please give ID: ")
                    newName = input("Enter a new name: ")
                    self._controller2.update(id, newName)
                elif command == '11':
                    z = UI.readGrade()
                    self._controller3.addGrade(z) 
                elif command == '12':
                    self._controller3.getAll()                        
                elif command == '13':                    
                    self._controller3.removeAll()  
                elif command == '14': 
                    print("A.Search in Students") 
                    print("B.Search in disciplines") 
                    x=input("Enter command: ") 
                    if x=='A':
                        y=input("Id or name of the student: ")
                        y=y.lower()                                            
                        list=self._controller.search(y)
                        self.display_search(list)
                    elif x=='B':
                        y=input("Id or name of the discipline: ")                        
                        y=y.lower() 
                        list=self._controller2.search(y)
                        self.display_search(list)
                    else:
                        print("Invalid option") 
                elif command == '15':
                    print("a.All students enrolled at a given discipline, sorted alphabetically")
                    print("b.All students enrolled at a given discipline, sorted by descending order of average grade")     
                    print("c.All students failing at one or more disciplines ")  
                    print("d.Students with the best school situation, sorted in descending order of their aggregated average ")    
                    print("e.All disciplines sorted in descending order of the average grade received by all students")
                    x=input("Enter option: ")   
                    if x=='a': 
                        y=input("Give discipline: ")                       
                        list=self._controller3.sort_alph(y)
                        i=1
                        if len(list)==0:
                            print("There are no students enrolled at",y)
                        for n in list:
                            print(i,n)
                            i+=1 
                    elif x=='b': 
                        y=input("Give discipline: ")                       
                        list=self._controller3.sort_average(y)
                        if len(list)==0:
                            print("There are no students enrolled at",y)
                        i=1
                        for n in list:
                            print(i,".",n[0],"~",n[3])
                            i+=1                        
                    elif x=='c':  
                        list=self._controller3.fail()
                        i=1
                        if len(list)==0:
                            print("There are no students that failed",y)
                        for n in list:
                            print(i,n[0],"~",n[1],n[2])
                            i+=1 
                    elif x=='d':  
                        list=self._controller3.sort_total()
                        i=1
                        for n in list:
                            print(i,".",n[0],"~",n[3])
                            i+=1       
                    elif x=='e':  
                        list=self._controller3.sort_alldisciplines()
                        i=1
                        for n in list:
                            print(i,".",n[0],"~",n[3])
                            i+=1       
                    else:
                        print("Invalid option!")                
                else:
                    print("Invalid commnad!")
            except Exception as exc:
                print("Error encountered - "+str(exc))

    @staticmethod
    def printList(l):
        print("List is:")
        for z in l:
            print(str(z))

    @staticmethod
    def readPositiveInteger(msg):
        """
        Reads a positive integer
        Input: -
        Output: A positive integer
        """
        result = None
        while result == None:
            try:
                result = int(input(msg))
                if result < 0:
                    raise ValueError
            except ValueError:
                print("Please input a positive integer!")
        return result


    @staticmethod
    def readStudent():        
        while True:
            try:
                id = int(input("ID= "))
                name = input("Name= ")
                return Student(id, name)
            except ValueError:
                print("ID must be an integer!")
        return []
    
    
    @staticmethod
    def readDiscipline():       
        while True:
            try:
                id = int(input("ID= "))
                name = input("Name of discipline= ")
                return Discipline(id, name)
            except ValueError:
                print("ID must be an integer!")
        return []
    
    @staticmethod
    def readGrade():       
        while True:
            try:
                id_s = int(input("ID_student= "))
                id_d = int(input("ID_discipline= "))
                value =int(input("Enter the grade= "))
                if value<=0 or value >10:
                    print("The grade must be in [1,10]")
                else:
                    return Grade(id_s,id_d,value)
            except ValueError:
                print("Values must be integers!")
        return []
    def display_search(self,list):
        if len(list)>0:
            i=1
            for l in list:
                print(i,".","Id",l[0],l[1])
                i+=1
        else:
            print("There are no items matching to your search!")
    