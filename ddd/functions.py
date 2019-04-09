'''APARTMENT BUILDING ADMINISTRATOR undolist.append(deepcopy(l))'''
def testInit(expenseslist):        #10 items in the list at the begining of the execution
    expenseslist.append((1, "gas", 100))
    expenseslist.append((2, "water", 80))
    expenseslist.append((2, "heating", 200))
    expenseslist.append((2, "electricity", 170))
    expenseslist.append((5, "gas", 225))
    expenseslist.append((6, "water", 400))
    expenseslist.append((7, "electricity", 855))
    expenseslist.append((8, "heating", 90))
    expenseslist.append((9, "water", 432))
    expenseslist.append((10, "gas", 184))
    #print(expenseslist)

def printmenu():                 #prints the menu   
    print("1.Add apartment")
    print("2.Remove apartment")
    print("3.Remove apartments from a to b")
    print("4.Remove apartment type")
    print("5.Replace apartment type expense with")
    print("6.List")
    print("7.List expenses for apartment:")
    print("8.List expenses <,=,> than the value:")
    print("9.Sum the expenses for the type:")
    print("10.Write the maximum amount per each expense type for apartment:")
    print("11.Sort apartments by total expenses")
    print("12.Sort the types of expenses by amountS")
    print("13.Keep only expenses for type:")
    print("14.Keep only expenses < than the value:")
    print("15.Undo the last operation")
    

def help_command():                 #prints the possible comands that the user can give
    print("\t These are the valid commands:")
    print("\t add <apartment> <type> <amount>")
    print("\t remove <apartment>")
    print("\t remove <start apartment> to <end apartment>")
    print("\t remove <type>")
    print("\t replace <apartment> <type> with <amount>")
    print("\t list")
    print("\t list <apartment>")
    print("\t list [ < | = | > ] <amount>")
    print("\t sum <type>")
    print("\t max <apartment>")
    print("\t sort apartment")
    print("\t sort type")
    print("\t filter <type>")
    print("\t filter <value>")
    print("\t undo")
    
def readCommand(cmd):                 #function that reads the command and slice it by space
        
    if cmd.find(" ") == -1:        
        command = cmd        
        '''
        Fara parametrii. help sau exit
        '''
        params = ""
        return (command, params)
    else:        
        command = cmd[0:cmd.find(" ")] #extrage comanda, ex add, remove        
        '''
        Cu parametrii
        '''
        params = cmd[cmd.find(" "):]
        params = params.split(" ")
        for i in range(1, len(params)):
            params[i] = params[i].strip()
        i=1
        while i<len(params):
            if params[i]==' ':
                params.pop(i)
                i=i-1
            i=i+1
        if params[1]=='':
            raise ValueError("Incomplete command")
        else:
            return (command, params)

def findById(expenseslist, expense_id,expense_tip):    #returns -1 if the id with the correct type is not found and the position of the element otherwise
    pos = -1
    for i in range(0, len(expenseslist)):
        exp = expenseslist[i]
        if exp[0] == expense_id:
            if exp[1]==expense_tip:
                pos = i
                break
    return pos

def findbyid(expenseslist, expense_id):    #returns -1 if the id with the correct type is not found and the position of the element otherwise
    pos = -1
    for i in range(0, len(expenseslist)):
        exp = expenseslist[i]
        if exp[0] == expense_id:            
            pos = i
            break
    return pos


def addexpense(expenseslist, expense):                    #function that adds a new expense in expenseslist 
    #if findById(expenseslist, expense[0],expense[1])== -1: # if there is no expense    
    expenseslist.append(expense)             #with the current id and the current type
      

def add_command(expenseslist, cmd,undolist):                #checks the inputs and call addexpense if it is all right
    if (len(cmd)-1)% 3 !=0:
        raise ValueError("Invalid input. Expense was not added")
    else:
        list=expenseslist[:]
        undolist.append(list)          #UNDO 
        fin=int(len(cmd)/3)
        for i in range(0,fin):        
            nrap= int(cmd[3*i+1])
            amount = int(cmd[3*i+3])
            if nrap <= 0 or len(cmd[2]) == 0 or amount<0:
                raise ValueError("Invalid input. Expense was not added") 
            else:            
                expense=(nrap, cmd[3*i+2], amount)
                addexpense(expenseslist, expense)        
    
def listall(expenseslist):      #prints the list with all the existant expenses    
    if len(expenseslist)>0:
        for exp in expenseslist:
            print("Apartment",exp[0],"type of expense",exp[1],"amount",exp[2])
    else:
        print("List is empty.")

def listbyapartment(expenseslist,id):              #prints all the axpenses of a given apartment
    if checkid(expenseslist,id)!=-1:        
        print("Apartment",id,"has the following expenses:")
        for exp in expenseslist:
            if exp[0]==id:
                print(exp[1],"amount",exp[2])
    else:
        print("Apartment",id,"does not exist")

def listbyexpenses(expenseslist,sign,money):       #prints all the apartment with total expenses <,=,> than a given value(money)
    max=maximum(expenseslist)    
    ok=False
    if sign==">":
        print("Al the apartments with total expenses",sign,money,":")    
        for i in range(1,max+1):
            results = [t[2] for t in expenseslist if t[0] == i]
            s=0
            for r in results:
                s=s+int(r)
            if s> money:
                ok=True
                print("Apartment",i)
        if ok==False:
            print("There are no apartments with total expenses",sign,money)
    elif sign=="<":
        print("Al the apartments with total expenses",sign,money,":")    
        for i in range(1,max+1):
            results = [t[2] for t in expenseslist if t[0] == i]
            s=0
            for r in results:
                s=s+int(r)
            if (s< money) and s>0:
                ok=True
                print("Apartment",i)
        if ok==False:
            print("There are no apartments with total expenses",sign,money)
    elif sign=="=":
        print("Al the apartments with total expenses",sign,money,":")    
        for i in range(1,max+1):
            results = [t[2] for t in expenseslist if t[0] == i]             
            s=0
            for r in results:
                s=s+int(r)
            if s== money:
                ok=True
                print("Apartment",i)
        if ok==False:
            print("There are no apartments with total expenses",sign,money)
    else:
        raise ValueError("Sign is no compatible")
    
def list_command(expenseslist, cmd):              #manages all the posible requirements of list and call the right functions
    if len(cmd) < 2:        
        listall(expenseslist)
    elif len(cmd)==2:        
        nrap=int(cmd[1])
        listbyapartment(expenseslist,nrap)
    elif len(cmd)==3:        
        sign=cmd[1]
        money=int(cmd[2])
        if money>0:
            listbyexpenses(expenseslist,sign,money)
        else:
            print("Money is 0")
    else:        
        raise ValueError("Invalid command")
def checkid(expenseslist, id):                  #checks if a certain id of apartment belongs to the list   
    pos=-1
    for i in range(0, len(expenseslist)):
        exp = expenseslist[i]
        if exp[0] == id:
            pos=i
            break
    return pos

def checktype(expenseslist, tip):               #checks if a certain type of expense is included in the list
    pos=-1
    for i in range(0, len(expenseslist)):
        exp = expenseslist[i]
        if exp[1] == tip:
            pos=i
            break
    return pos

def remove__expenses(expenseslist,id,undolist):      #removes all the expenses of the apartment with the given id
    if checkid(expenseslist,id)!=-1:
        list=expenseslist[:]
        undolist.append(list)                   #UNDO
        pos=checkid(expenseslist,id)
        while pos!=-1:
            expenseslist.pop(pos)
            pos=checkid(expenseslist,id)
        return True
    else:
        
        return False

def remove__expenses_type(expenseslist,tip):     #removes all expenses of a certain type
    if checktype(expenseslist,tip)!=-1:        
        pos=checktype(expenseslist,tip)
        while pos!=-1:
            expenseslist.pop(pos)
            pos=checktype(expenseslist,tip)
        return True
    else:
        
        return False

def remove_expense_fromto(expenseslist,start,stop,undolist):                     #removes all expenses from apartment start+1, stop-1        
    i=0
    list=expenseslist[:]
    undolist.append(list)                  #UNDO 
    while i<len(expenseslist):
        exp=expenseslist[i]
        if (exp[0]>start) and (exp[0]<stop):
            expenseslist.pop(i)
            i=i-1
        i+=1
    
def remove_command(expenseslist, cmd,undolist):                  #manages all the remove comands and call the appropiate functions   
    if len(cmd)>2 and cmd[1].isdigit():
        if cmd[2]=='to' :
            start=int(cmd[1])
            stop=int(cmd[3])            
            remove_expense_fromto(expenseslist,start,stop,undolist)    
    elif len(cmd) >= 2 :
        x=cmd[1]
        if x.isdigit():
            nrap= int(cmd[1])                
            if nrap <= 0:
                raise ValueError("Invalid input. Wrong id")                
            else:
                if remove__expenses(expenseslist, nrap,undolist) == False:
                    print("Inexistent apartment")          
        else:
            list=expenseslist[:]
            undolist.append(list)                   #UNDO
            for i in range(1,len(cmd)):
                tip=cmd[i]                
                if remove__expenses_type(expenseslist, tip) == False:
                    print("Inexistent type of expense")
    else:
        raise ValueError("Invalid command")
    
def replace_command(expenseslist,cmd,undolist):                          #replace the expenses of the given apartment, of a certain tipe with a given value 
    nrap=int(cmd[1])
    tip=cmd[2]
    amount=int(cmd[4])
    pos=findById(expenseslist,nrap,tip)
    if pos!=-1:
        list=expenseslist[:]
        undolist.append(list)               #UNDO
        expenseslist[pos]=(nrap,tip,amount)
    else:        
        print("There is no such apartment with such expense")
def sum_command(expenseslist,cmd): 
    tip=cmd[1]
    if checktype(expenseslist,tip)!=-1:
        s=0
        for exp in expenseslist:
            if exp[1]==tip:
                s=s+exp[2] 
        print("The total amount of",tip,"expenses is",s)
    else:
        raise ValueError("The type is inexistent")
def find(tiplist,expense_type):    
    pos = -1
    for i in range(0, len(tiplist)):
        tip = tiplist[i]
        if tip[0] == expense_type:            
            pos = i            
            break
    return pos

def max_command(expenseslist,cmd):
    if cmd[1].isdigit():
        nrap=int(cmd[1])
        if find(expenseslist,nrap)!=-1:
            tiplist=[]
            print("The maximum amounts per each expense are:")
            for exp in expenseslist:
                if exp[0]==nrap:
                    pos=find(tiplist,exp[1])
                    if pos!=-1:
                        t=tiplist[pos]
                        if exp[2]>t[1]:
                            tiplist[pos]=(exp[1],exp[2])
                    else:
                        new=(exp[1],exp[2])
                        tiplist.append(new)    
            for tip in tiplist:
                print("The maximum amount of",tip[0],"expenses is",tip[1])
        raise ValueError("Inexistent apartment")
    else:
        raise ValueError("You need an integer parameter")
def maximum(expenseslist):
    max=0
    for exp in expenseslist:
        if exp[0]>max:
            max=exp[0] 
    return max
        
def sort_apartments(expenseslist):
    sortlist=[]
    max=maximum(expenseslist) 
    for i in range(1,max+1):
        if findbyid(expenseslist,i)!=-1:
            results = [t[2] for t in expenseslist if t[0] == i]
            s=0
            for r in results:
                s=s+int(r)
            element=(i,s)
            sortlist.append(element)
    #print(sortlist)
    return sortlist
def sort(s):
    ok=True
    while ok==True:
        ok=False
        for i in range(0,len(s)-1):
            if s[i][1]>s[i+1][1]:
                aux=s[i]
                s[i]=s[i+1]
                s[i+1]=aux
                ok=True
    return s 
    
def sort_by_type(expenseslist):
    sortlist=[]
    for exp in expenseslist:
        pos=find(sortlist,exp[1])
        if pos==-1:
            new=(exp[1],exp[2])
            sortlist.append(new)
        else:
            s=sortlist[pos]
            new=(s[0],s[1]+exp[2])
            sortlist[pos]=new
    #print(sortlist)
    return sortlist
def sort_command(expenseslist,cmd):    
    cuv=cmd[1]    
    sortlist=[]
    if cuv=='apartment':
        sortlist=sort_apartments(expenseslist)
        sortlist=sort(sortlist)
        print("The apartments sorted ascending by total expenses are:")
        for s in sortlist:
            print("Apartment",s[0],"total expenses",s[1])
        
    elif cuv=='type':
        sortlist=sort_by_type(expenseslist)
        sortlist=sort(sortlist)
        print("The types of expenses sorted ascending by total amount are:")
        for s in sortlist:
            print("Expense",s[0],"total amount",s[1])
    else:
        raise ValueError("Invalid command!")

def remove(expenseslist,cash):    
    i=0
    while i<len(expenseslist):
        exp=expenseslist[i]
        if exp[2]>=cash:
            expenseslist.pop(i)
            i=i-1
        i+=1   

def remove_type(expenseslist,tip):
    if checktype(expenseslist,tip)!=-1:
        i=0
        while i<len(expenseslist):
            exp=expenseslist[i]
            if exp[1]!=tip:
                expenseslist.pop(i)
                i=i-1
            i+=1
    else:
        raise ValueError("Inexistent type")

def filter_command(expenseslist,cmd,undolist):    
    cuv=cmd[1]
    if cuv.isdigit():
        cash=int(cuv)
        list=expenseslist[:]
        undolist.append(list)                        #UNDO
        remove(expenseslist,cash)
    elif checktype(expenseslist,cuv)!=-1:
        list=expenseslist[:]
        undolist.append(list)                      #UNDO
        remove_type(expenseslist,cuv)
    else:
        raise ValueError("Invalid command")

def undo_command(undolist,expenseslist):
    if undolist !=[]:
        #print(undolist)
        n=len(undolist)-1    
        list=undolist[n]
        expenseslist=[]
        expenseslist=list
        undolist.pop(n)    
        return expenseslist
    else:
        print("There is no operation before that!")
        return expenseslist

