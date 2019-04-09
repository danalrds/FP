class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.Add order")
        print("2.Display orders")
        print("3.Compute income by id ")
        print("0.Exit")
    def mainmenu(self):
        stop=False
        while stop==False:
            try:
                self.printmenu()
                comm=input("Enter command: ")
                if comm=="2":
                    res=self._control.getAll()
                    for r in res:
                        print(str(r))
                elif comm=="1":
                    id=int(input("Give id: "))
                    distance=int(input("Give distance: "))
                    self._control.add(id,distance)
                elif comm=="3":
                    id=int(input("Give the id to compute income: "))
                    self._control.compute(id)                    
                elif comm=="0":
                    stop=True
                else:
                    raise ValueError("Invalid command!")
            except Exception as exc:
                print(str(exc))