class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.All films with name sorted by")
        print("2.Popular films")
        print("3.Update by 25% all with price>=given price")
        print("4.Add movie")
        print("5.List")
        print("0.Exit")
    def mainmenu(self):
        stop=False
        while stop==False:
            try:
                self.printmenu()
                comm=input("Enter command: ")
                if comm=="1":
                    name=input("Give string: ")
                    crit=input("Give criteria 1 for price*places 2 for name")
                    res=self._control.sorter(name,crit)
                    for r in res:
                        print(str(r))
                elif comm=="2":
                    res=self._control.afisaremedia()
                    for r in res:
                        print(str(r))
                elif comm=="3":
                    price=int(input("Enter price: "))
                    self._control.reduce(price)
                elif comm=="4":
                    id=int(input("Give id: "))
                    name=input("name: ")
                    price=int(input("price: "))
                    places=int(input("places: "))
                    self._control.add(id,name,price,places)
                elif comm=="5":
                    res=self._control.getAll()
                    for r in res:
                        print(str(r))
                elif comm=="0":
                    stop=True
                else:
                    raise ValueError("Invald command!")
            except MemoryError as exc:
                print(str(exc))