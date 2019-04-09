import unittest
from copy import deepcopy
from repository import Repository
from random import randint
class Controller():
    def __init__(self,repo):
        self._repo=repo
        self._undolist=''
        self._initial=''
    ''' returns all the sentences from the input.txt'''
    def getAll(self):
        return self._repo.getAll()
    ''' prints out the status of the game in the format: sentence score'''
    def tipareste(self,prop,score):
        new=prop
        new=new+" [score is "+str(score)+" ]"
        print(new)
    '''shuffle function it receives a sentence and shuffles all the letters that are not first or last in a word '''
    def shuffle(self,prop):
        prop=" "+prop+' '
        litere=[]
        for i in range(1,len(prop)-1):
            if (prop[i]!=" " and prop[i-1]!=" ") and (prop[i]!=" " and prop[i+1]!=" "):
               litere.append(prop[i]) 
        new=''
        
        for i in range(1,len(prop)-1):
            if prop[i]==" ":
                new+=" "
            elif (prop[i]!=" " and prop[i-1]==" ") or (prop[i]!=" " and prop[i+1]==" "): 
                new+=prop[i]
            elif (prop[i]!=" " and prop[i-1]!=" ") or (prop[i]!=" " and prop[i+1]!=" "):
                n=len(litere)
                idx=randint(0,n-1)
                lit=litere[idx]
                new+=lit
                litere.remove(lit)
        return new
    ''' function that starts the game it choses randomly a sentence and calls the necessary functions '''
    def joaca(self):
        n=len(self.getAll())
        idx=randint(0,n-1)
        list=self.getAll() 
        prop=str(list[idx])       
        c=0
        for p in prop:
            if p!=" ":
                c+=1
        score=c
        self._initial=prop+' '
        prop=self.shuffle(prop)
        self.tipareste(prop,score)
        self.incepe(prop,score)
    '''game is starting the user has to make a swap '''
    def incepe(self,prop,score):
        try:
            ok=False
            while True and score!=0 and prop!=self._initial:
                x=input()
                comanda=x.strip().split(" ")
                if comanda[0]=='swap':
                    prop=self.citeste_swap(prop,comanda)
                    score=score-1                    
                    if str(prop)==str(self._initial):
                        print("You won!")  
                        self.tipareste(prop,score)  
                        ok=True
                        break                 
                    if score==0:
                        print("You lost!")  
                        self.tipareste(prop,score)        
                        ok=True          
                        break
                    self.tipareste(prop,score)                   
                    
                elif comanda[0]=='undo':
                    prop=''
                    prop=self._undolist
                    self.tipareste(prop,score) 
                else:
                    break
            if ok==False:
                if str(prop)==str(self._initial):
                    print("You won!")  
                if score==0:
                    print("You lost!")                  
                           
                    
        except  Exception as exc:
            print(str(exc))
    ''' is number checks if a string is a number or not output true or false'''
    def is_number(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    def citeste_swap(self,prop,comanda):     
        if len(comanda)!=6:
            raise Exception("Invalid commnand!")
        if comanda[3]!="-":
            raise Exception("Invalid commnand!")
        cifre=['0','1','2','3','4','5','6','7','8','9']
        if self.is_number(comanda[1])==False:
            raise Exception("Invalid commnand!")
        if self.is_number(comanda[2])==False:
            raise Exception("Invalid commnand!")
        if self.is_number(comanda[4])==False:
            raise Exception("Invalid commnand!")
        if self.is_number(comanda[5])==False:
            raise Exception("Invalid commnand!")
        cuv1=int(comanda[1])
        lit1=int(comanda[2])
        cuv2=int(comanda[4])
        lit2=int(comanda[5])
        fraza=prop.strip().split(" ")
        if len(fraza[cuv1])-1==lit1 or lit1==0:
            raise Exception("Invalid indices!")
        if len(fraza[cuv2])-1==lit2 or lit2==0:
            raise Exception("Invalid indices!")
        self._undolist=''
        self._undolist=prop
        return self.swap(prop,cuv1,lit1,cuv2,lit2)
    ''' swap function input data the indices of the letters and words output data the sentence with the switched letters'''
    def swap(self,prop,cuv1,lit1,cuv2,lit2):
        fraza=prop.strip().split(" ")
        a=fraza[cuv1][lit1]
        b=fraza[cuv2][lit2]
        old=fraza[cuv1]
        nou=''
        for i in range(0,lit1):
            nou=nou+old[i]
        nou=nou+b
        for i in range(lit1+1,len(old)):
            nou=nou+old[i]
        fraza[cuv1]=nou
        
        
        old=fraza[cuv2]
        nou=''
        for i in range(0,lit2):
            nou=nou+old[i]
        nou=nou+a
        for i in range(lit2+1,len(old)):
            nou=nou+old[i]
        fraza[cuv2]=nou
        
        new=''
        for i in range(0,len(fraza)):
            new+=fraza[i]+' '        
        return new
class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("input.txt")
        self._control=Controller(self._repo)

    def testName(self):
        list=self._control.getAll()
        self.assertEqual(len(list),4)
        prop="ana are mere"
        cuv1=0
        cuv2=1
        lit1=1
        lit2=1
        prop=self._control.swap(prop,cuv1,lit1,cuv2,lit2)
        self.assertEqual(prop,"ara ane mere ")
        s='15'
        ok=self._control.is_number(s)
        self.assertEqual(ok,True)