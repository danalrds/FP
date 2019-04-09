from studentclass import Student
from gradeclass import Grade
class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.Add student")
        print("2.Delete student")
        print("3.Assign a problem")
        print("4.Assign a laboratory")
        print("5.Order students")
        print("0.Exit")
    def mainmenu(self):
        try:
            while True:
                self.printmenu()
                com=input("ENTER command: ")
                if com=="1":
                    id=int(input("Give id: "))
                    name=input("Give name: ")
                    group=input("Give group: ")
                    student=Student(id,name,group)
                    self._control.add(student)
                elif com=="2":
                    name=input("Give name: ")
                    student=self._control.findbyname(name)                    
                    if student!=None:
                        self._control.delete(student)
                elif com=="3":
                    name=input("Give name: ")
                    prob=int(input("Give nr problem: "))
                    student=self._control.findbyname(name) 
                    self._control.assign(student,prob)                   
                    
                elif com=="4":   
                    lab=int(input("Give nr lab: "))                  
                    prob=int(input("Give nr problem: "))                    
                    self._control.assignlab(prob,lab)      
                elif com=="5":                                          
                    self._control.order()                   
                    
                elif com=="0":
                    break
                else:
                    raise ValueError("Invalid command!")
        except Exception as exc:
            print(str(exc))