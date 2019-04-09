class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.List trips")
        print("2.Postpone trip when a given value")
        print("0.Exit")
    def mainmenu(self):
        stop=False
        while stop==False:
            try:
                self.printmenu()
                comm=input("Enter command: ")
                if comm=="1":
                    list=self._control.listall()
                    for l in list:
                        print(l)
                elif comm=="2":
                    value=int(input("Enter value: "))
                    self._control.amana(value)
                elif comm=="0":
                    stop=True
                else:
                    raise ValueError("Invalid command!")
            except Exception as e :
                print(e)
                