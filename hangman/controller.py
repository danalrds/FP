import unittest
from random import randint
from sentclass import Sentence
from repository import Repository
class Controller():
    def __init__(self,repo):
        self._repo=repo
    ''' adds a new sentence in the list'''
    def add(self,obj):
        self._repo.store(obj)    
    ''' returns all the sentences'''
    def getAll(self):
        return self._repo.getAll()
    '''checks if a sentence is in the list already '''
    def find(self,prop):
        for s in self.getAll():
            if str(s)==prop:
                return  True
        return False
    ''' procedure that starts the game
    chooses a sentence and display it in the right way'''
    def start(self):
        lista=self.getAll()
        idx=randint(0,len(lista)-1)
        prop=lista[idx]
        self.arata(prop)
    ''' procedure that takes the sentence and shows the letters as the rule asks'''
    def arata(self,prop):
        fraza=str(prop)
        fraza=' '+fraza+' '
        #print(fraza)
        initial=''
        multime=[]
        for i in range(1,len(fraza)-1):
            if fraza[i]==" ":
                initial+=" "
            elif (fraza[i]!=" " and fraza[i+1]==" ") or (fraza[i]!=" " and fraza[i-1]==" "):
                initial+=fraza[i] 
                multime.append(fraza[i])           
            else:
                initial+="_"   
        final=''
        i=1
        for s in initial:
            if s=="_":
                if fraza[i] in multime:
                    final=final+fraza[i]
                else:
                    final=final+"_"
            else:
                final=final+s 
            i+=1  
        self.tipareste(final)
        self.joaca(fraza,final,multime)
    '''print procedure it prints the sentence with spaces between words '''
    def tipareste(self,string):
        new=''
        for s in string:
            new=new+s+' '
        print(new)
    '''it checks if the game is won or not '''
    def gamewon(self,prop,acumhang):
        c=0
        if acumhang=='hangman':
            return True
        for s in prop:
            if s=="_":
                c+=1
        if c==0:
            return True
        return False
    ''' play procedure the player enter a letter if is right all its aparition are filled if not the ai completes with a letter'''
    def joaca(self,fraza,prop,multime):
        litere=[]
        hang=['h','a','n','g','m','a','n']
        acumhang='h'
        for f in fraza:
            if f!=" ":
                if f not in litere:
                    litere.append(f)        
        contor=1
        while self.gamewon(prop,acumhang)==False:
            x=input("Give a letter: ")
            if x in litere and x not in multime:
                prop=self.punex(x,fraza,prop)
                multime.append(x)                
                self.tipareste(prop)
                print(acumhang)
            else:                 
                acumhang+=hang[contor] 
                contor+=1              
                self.tipareste(prop)
                print(acumhang)
        if self.gamewon(prop,acumhang)==True:
            if acumhang!='hangman':
                print("Player has won!")
            else:
                print("Ai has won!")
    '''function that puts the right letter in all its places in the sentence '''
    def punex(self,x,fraza,prop):
        newprop=''
        i=1
        for s in prop:
            if s=="_":
                if fraza[i]==x:
                    newprop+=x 
                else:
                    newprop+="_"
            else:
                newprop+=s
            i+=1
        return newprop    
    ''' ai reveals a letter '''    
        
class Test(unittest.TestCase):

    def setUp(self):
        self._repo=Repository("sentences.txt")
        self._control=Controller(self._repo)
    def testName(self):
        list=self._control.getAll()        
        self.assertEqual(len(list),5)
        sent=Sentence("patricia has pears")
        self._control.add(sent)
        self.assertEqual(len(list),6)
        fraza='patricia has pears'
        acumhang='hang'
        self.assertEqual(self._control.gamewon(fraza,acumhang),True)
        fraza='patricia has p_ars'
        self.assertEqual(self._control.gamewon(fraza,acumhang),False)
        fraza=' anna has apples '
        prop='a__a has a__l_s'
        x='n'
        propozitie=self._control.punex(x, fraza, prop)
        new='anna has a__l_s'
        self.assertEqual(propozitie,new)
