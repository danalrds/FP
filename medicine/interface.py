class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.List medicines")
        print("2.Delete medicine by name")
        print("3.Update medivine price with: ")
        print("0.Exit")
    def mainmenu(self):
        stop=False
        while stop==False:
            try:
                self.printmenu()
                comm=input("Enter command:")
                if comm=="1":
                    for l in self._control.listall():
                        print(l)
                elif comm=="2":
                    name=input("Enter a string name: ")
                    self._control.delete(name)
                elif comm=="3":
                    value=int(input("Give value: "))
                    cant=int(input("Give the etra quantity: "))
                    self._control.increase(value,cant)
                elif comm=="0":
                    stop=True
                else:
                    raise ValueError("Invalid command!")
            except Exception as e:
                print(e)