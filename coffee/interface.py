class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.Filter")
        print("2.Sort")
        print("3.List")
        print("0.Exit")
    def mainmenu(self):
        while True:
            try:
                self.printmenu()
                com=input("Enter command!")
                if com=="1":
                    country=input("Give country: ")
                    price=float(input("Give price: "))
                    self._control.filterbycountry(country,price)
                elif com=="2":
                    self._control.sort()
                elif com=="3":
                    for t in self._control.getAll():
                        print(str(t))
                elif com=="0":
                    break
                else:
                    raise ValueError("Invalid command!")
            except ValueError as exc:
                print(str(exc))