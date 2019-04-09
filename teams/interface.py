class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.List by group")
        print("2.Enter a match")
        print("3.Sort countries by points")
        print("0.Exit")
    def mainmenu(self):
        stop=False
        while stop==False:
            try:
                self.printmenu()
                comm=input("Enter command: ")
                if comm=="1":
                    group=input("Give a group: ")
                    for z in self._control.filterbygroup(group):
                        print(z)
                elif comm=="2":
                    str=input("Write the match with score: ")
                    self._control.solvematch(str)
                elif comm=="3":
                    for z in self._control.sorter():
                        print(z)
                elif comm=="0":
                    stop=True
                else:
                    raise ValueError("Invalid command!")
                
            except Exception as exc:
                print(exc)