from controller import Controller
from dictionary import Dictionary
from pip._vendor.requests.packages.chardet import langbulgarianmodel
class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.Add word")
        print("2.Spell check phrase")
        print("3.Print to file the spell checked phrase")
        print("4.List")
        print("0.Exit")
    def mainmenu(self):
        while True:
            try:
                self.printmenu()
                x=int(input("Enter command: "))
                if x==1:
                    id=int(input("Give id: "))
                    lang=self.readLanguage("Give language:")
                    word=self.readWord("Give word: ")
                    dict=Dictionary(id,lang,word)
                    self._control.add(dict)
                elif x==2:
                    lang=self.readLanguage("Give language:")
                    phrase=input("Give phrase: ")
                    self._control.check(lang,phrase)
                elif x==3:
                    entrance=input("Give input file: ")
                    exit=input("Give output file: ")
                    self._control.spell(entrance,exit)
                elif x==4:
                    for d in self._control.getAll():
                        print(str(d))
                elif x==0:
                    break
                else:
                    raise ValueError("Invalid command!")
            except Exception as exc:
                print(str(exc))
    @staticmethod
    def readLanguage(ms):
        ok=True
        while ok==True:
            ok=False
            lang=input("Give language:")
            if lang in ['Ro', 'En','Fr' ]:
                return lang
            else:
                ok=True
                print("Language must be Ro, En or Fr!")
                
    @staticmethod
    def readWord(ms):
        ok=True
        while ok==True:
            ok=False
            word=input("Give word:")
            if word!='':
                return word
            else:
                print("Word can't be empty!")
                ok=True 
             