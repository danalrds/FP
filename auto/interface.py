class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.Add car")
        print("2.Delete by id")
        print("3.Sort by price")
        print("4.Increase all the prices < the given price")
        print("5.List")
        print("0.Exit")
    def mainmenu(self):
        stop=False
        while stop==False:
            try:
                self.printmenu()
                comm=input("Enter command: ")
                if comm=="1":
                    id=int(input("Give id: "))
                    mark=input("Give mark: ")
                    price=float(input("Give price: "))
                    self._control.add(id,mark,price)
                elif comm=="2":
                    id=int(input("Give id: "))
                    self._control.delete(id)
                elif comm=="3":
                    res=self._control.sortbyprice()
                    for r in res:
                        print(str(r))
                elif comm=="4":
                    price=int(input("Give price: "))
                    self._control.modifica(price)
                elif comm=="5":
                    res=self._control.getAll()
                    for r in res:
                        print(str(r))
                elif comm=="0":
                    pass
                else:
                    raise ValueError("Invalid command!")
            except MemoryError as exc:
                print(str(exc))